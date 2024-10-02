import unittest

import torch

from pytorch import dataset
import templates

class TestMNIST(unittest.TestCase, templates.DatasetTestsMixin):
    def setUp(self):
        self.data = dataset.MyMNIST()
        self.data_shape = torch.Size((1, 32, 32))
