from __future__ import division
import os.path as osp

import numpy as np
from scipy.misc import imread
import yaml

import rospkg


PKG = 'apc2015_common'
PKG_PATH = rospkg.RosPack().get_path(PKG)


def load_object_data():
    data_path = osp.join(PKG_PATH, 'data/object_data.yaml')
    return yaml.load(open(data_path))


def _resize_with_max_size(src, max_height, max_width):
    import cv2
    src_h, src_w = src.shape[:2]
    scale = min([max_height / src_h, max_width / src_w])
    dst_h, dst_w = int(scale * src_h), int(scale * src_w)
    dst = cv2.resize(src, (dst_w, dst_h))
    return dst


def visualize_object_set(objects=None, height=2560, width=2560,
                         tile_x=5, tile_y=5):
    if objects is None:
        objects = [obj['name'] for obj in load_object_data()]

    if tile_x * tile_y < len(objects):
        msg = ('tile size should be over number of objects {}.'
               '\nActual size: {} x {} = {}')

        raise ValueError(msg.format(len(objects), tile_x, tile_y,
                                    tile_x*tile_y))

    img_shape = (height, width, 4)
    max_h, max_w = height // tile_y, width // tile_x
    img = np.zeros(img_shape, dtype=np.uint8)

    for i, obj_name in enumerate(objects):
        x, y = i % tile_x, i // tile_x

        obj_img = imread(osp.join(PKG_PATH, 'models', obj_name, 'image.png'))
        obj_img = _resize_with_max_size(obj_img, max_h, max_w)

        h, w = obj_img.shape[:2]
        x_min, y_min = max_w * x, max_h * y
        x_max, y_max = x_min + w, y_min + h
        img[y_min:y_max, x_min:x_max] = obj_img
    return img
