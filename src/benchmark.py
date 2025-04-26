import argparse

from ultralytics import YOLO
from ultralytics.utils.benchmarks import benchmark


def benchmark_model(model, data, imgsz=640, half=False, device=0):
    """
    Benchmark a YOLOv8 model.

    Args:
        model (str): Path to the YOLOv8 model file.
        data (str): Path to the dataset configuration file.
        imgsz (int): Image size for inference.
        half (bool): Use half precision for inference.
        device (int): Device ID for GPU inference.
    """
    # Load the YOLOv8 model
    model = YOLO(model)

    # Run the benchmark
    benchmark(model, data=data, imgsz=imgsz, half=half, device=device)


def main():
  parser = argparse.ArgumentParser(description="Run a benchmark on a YOLOv8 model.")
  parser.add_argument("--model", type=str, required=True, help="Path to the YOLOv8 model file.")
  parser.add_argument("--data", type=str, required=True, help="Path to the dataset configuration file.")
  parser.add_argument("--imgsz", type=int, default=640, help="Image size for inference.")
  parser.add_argument("--half", action="store_true", help="Use half precision for inference.")
  parser.add_argument("--device", type=int, default=0, help="Device ID for GPU inference.")

  args = parser.parse_args()

  benchmark_model(args.model, args.data, args.imgsz, args.half, args.device)


if __name__ == "__main__":
  main()
