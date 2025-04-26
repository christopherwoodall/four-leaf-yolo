import argparse

from ultralytics import YOLO


def train_model(weight_path="weights/yolov8n.pt", data_path="data.yaml", epochs=10, imgsz=640, batch=16, device=0):
    """
    Train a YOLOv8 model.
    Args:
        weight_path (str): Path to the YOLOv8 model file.
        data_path (str): Path to the dataset configuration file.
        epochs (int): Number of training epochs.
        imgsz (int): Image size for training.
        batch (int): Batch size for training.
        device (int): Device ID for GPU training.
    """
    # Load the YOLOv8 model
    model = YOLO(weight_path)

    # Train the model
    model.train(data=data_path, epochs=epochs, imgsz=imgsz, batch=batch, device=device, save_period=5)

    # Save the model
    model.save("trained_model.pt")


def main():
  parser = argparse.ArgumentParser(description="Train a YOLOv8 model.")
  parser.add_argument("--weight", type=str, default="weights/yolov8n.pt", help="Path to the YOLOv8 model file.")
  parser.add_argument("--data", type=str, default="data.yaml", help="Path to the dataset configuration file.")
  parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs.")
  parser.add_argument("--imgsz", type=int, default=640, help="Image size for training.")
  parser.add_argument("--batch", type=int, default=16, help="Batch size for training.")
  parser.add_argument("--device", type=int, default=0, help="Device ID for GPU training.")

  args = parser.parse_args()

  train_model(args.weight, args.data, args.epochs, args.imgsz, args.batch, args.device)


if __name__ == "__main__":
  main()
