import base64
import io
import pytest
from fastapi.testclient import TestClient
from PIL import Image
from main import app 

def create_base64_image():
    image = Image.new('RGB', (100, 100), color = (73, 109, 137))
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

client = TestClient(app)

@pytest.mark.parametrize("valid_input", [
    {"image_base64": create_base64_image()}
])
def test_process_image(valid_input):
    response = client.post("/process-image", json=valid_input)
    
    assert response.status_code == 200
    response_json = response.json()
    assert "image_base64" in response_json
    
    assert response_json["image_base64"] != ""

def test_invalid_base64():
    invalid_input = {"image_base64": "not_a_valid_base64_string"}
    
    response = client.post("/process-image", json=invalid_input)
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid image data"}

