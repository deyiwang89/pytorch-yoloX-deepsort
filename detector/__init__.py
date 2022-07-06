from .yolox import yolo
from .yolox.yolo import YOLO


__all__ = ['build_detector']

def build_detector():
    return YOLO()
