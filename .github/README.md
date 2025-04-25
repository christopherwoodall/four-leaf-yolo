# 4 Leaf YOLO - WIP

Training a [YOLO model](https://github.com/WongKinYiu/yolov9/releases) to detect 4 leaf colvers in the browser.

## Examples

![features](assets/stage0_Conv_features.png)

## Usage

After cloning the repository, initialize and update the submodules:

```bash
git submodule update --init --recursive
git submodule update --recursive --remote
```

You will also need to grab the dataset from Adam on Roboflow [here](https://universe.roboflow.com/adam-fonagy/hunting-for-four-leaf-clovers) and place it in the `data` directory.

Additional models and weights can be downloaded from Wong's initial release [here](https://github.com/WongKinYiu/yolov9). There is also a `download.sh` script in the `weights` that can be used.

Roboflow also has a [great notebook](https://github.com/roboflow/notebooks/blob/main/notebooks/train-yolov9-object-detection-on-custom-dataset.ipynb) on how to train YOLO models.

### Installation

```bash
venv .venv
source .venv/bin/activate
pip install -r yolov9/requirements.txt
```

### Training

```bash
python train.py \
--device 0 --batch 16 --epochs 3 --img 640 --min-items 0 --close-mosaic 15 --save-period 1 \
--data data/data.yaml \
--weights weights/gelan-c-base.pt \
--cfg models/detect/gelan-c.yaml \
--hyp hyp.scratch-high.yaml
```

### Object Detection

```bash
python yolov9/detect.py \
--conf 0.1 --device 0 \
--source data/valid/images/20230516_170625_png_jpg.rf.be6bcd914015b6dcd9cbf92c1d90d674.jpg \
--weights runs/train/exp/weights/best.pt
```


## To Do

- [ ] Create a more robust dataset - see [FLC Dataset](https://biomedicalcomputervision.uniandes.edu.co/publications/finding-four-leaf-clovers-a-benchmark-for-fine-grained-object-localization/).
- [ ] Fix data augmentation issues in `yolov9`.
- [ ] Quantize the model for use in the browser.
- [ ] Convert to ONNX/TensorFlow
- [ ] [Serve with `tensorflow.js`](https://github.com/Hyuto/yolov8-tfjs)
