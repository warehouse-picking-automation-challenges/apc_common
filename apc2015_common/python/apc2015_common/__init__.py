import os.path as osp

import yaml

import rospkg


PKG = 'apc2015_common'
PKG_PATH = rospkg.RosPack().get_path(PKG)


def load_object_data():
    data_path = osp.join(PKG_PATH, 'data/object_data.yaml')
    return yaml.load(open(data_path))
