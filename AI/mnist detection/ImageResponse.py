from pydantic import BaseModel

class ImageResponse(BaseModel):
    image_base64: str