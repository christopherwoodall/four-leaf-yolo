import argparse

from ultralytics.utils.benchmarks import benchmark


def main(model, data, imgsz=640, half=False, device=0):
    """
    Run a benchmark on a YOLOv8 model.

    Args:
        model (str): Path to the YOLOv8 model file.
        data (str): Path to the dataset configuration file.
        imgsz (int): Image size for inference.
        half (bool): Use half precision for inference.
        device (int): Device ID for GPU inference.
    """
    benchmark(model=model, data=data, imgsz=imgsz, half=half, device=device)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Run a benchmark on a YOLOv8 model.")
  parser.add_argument("--model", type=str, required=True, help="Path to the YOLOv8 model file.")
  parser.add_argument("--data", type=str, required=True, help="Path to the dataset configuration file.")
  parser.add_argument("--imgsz", type=int, default=640, help="Image size for inference.")
  parser.add_argument("--half", action="store_true", help="Use half precision for inference.")
  parser.add_argument("--device", type=int, default=0, help="Device ID for GPU inference.")

  args = parser.parse_args()
  main(args.model, args.data, args.imgsz, args.half, args.device)
