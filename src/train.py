from ultralytics import YOLO


def main():
    model = YOLO("weights/yolov8n.pt")
    results = model.train(data="data.yaml", epochs=100, imgsz=640, save_period=5)
    model.save("weights/yolov8n_trained.pt")


if __name__ == "__main__":
  main()
