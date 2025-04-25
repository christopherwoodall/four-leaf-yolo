from ultralytics import YOLO


def main(weight_path="weights/yolov8n.pt", data_path="data.yaml", epochs=10, imgsz=640, batch=16, device=0):
    """
    Train a YOLOv8 model.
    Args:
        weight_path (str): Path to the YOLOv8 model file.
        data_path (str): Path to the dataset configuration file.
    """
    # Load the YOLOv8 model
    model = YOLO(weight_path)

    # Train the model
    model.train(data=data_path, epochs=epochs, imgsz=imgsz, batch=batch, device=device)

    # Save the model
    model.save("trained_model.pt")


if __name__ == "__main__":
  main()
