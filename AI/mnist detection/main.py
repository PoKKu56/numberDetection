from ultralytics import YOLO
import cv2

def main():
    # Load a model
    model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data="data.yaml", epochs=100, imgsz=640)

    print(results)

    model.save("mnist.pt")

def test():

    model = YOLO("mnist.pt")
    results = model.predict(source='2.png')
    if results[0].boxes:
        # Save the image with detections
        annotated_image = results[0].plot()  # Get the annotated image
        cv2.imwrite('2.png', annotated_image)
    

if __name__ == '__main__':
    test()