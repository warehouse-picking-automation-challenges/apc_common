#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path as osp
from scipy.misc import imsave

import apc2015_common


if __name__ == '__main__':
    img = apc2015_common.visualize_object_set(
        height=2560, width=2560, tile_x=5, tile_y=5)
    img_file = 'apc2015_object_set.png'
    imsave(img_file, img)
    print('Wrote to {0}'.format(osp.realpath(img_file)))
