#-*- coding: utf-8 -*-
import os, sys, io
import pytest
from coffee_service.iamalba import alba
from coffee_service import menupan
from basic.calculator import calculator_machine
from common.exceptions import ALBAException
from common.exceptions import CalculateException

import torch
from pytorch import model
# from pytorch.templates import ModelTestsMixin
from templates import ModelTestsMixin
from torch.utils.data import DataLoader

test_inputs = None
net = None

@pytest.fixture(scope="class")
def test_template():
    temp_template = ModelTestsMixin()
    temp_template.test_inputs = torch.randn(4, 1, 32, 32)
    temp_template.net = model.CNNVAE(input_shape=(1, 32, 32), bottleneck_dim=16)
    return temp_template

@torch.no_grad()
def test_shape(test_template):
    outputs = test_template.net(test_template.test_inputs)
    assert test_template.test_inputs.shape == outputs.shape

@torch.no_grad()
@pytest.mark.skipif(torch.cuda.is_available() != True, reason='No GPU was detected')
def test_device_moving(test_template):
    net_on_gpu = test_template.net.to('cuda:0')
    net_back_on_cpu = net_on_gpu.cpu()

    torch.manual_seed(42)
    outputs_cpu = test_template.net(test_template.test_inputs)
    torch.manual_seed(42)
    outputs_gpu = net_on_gpu(test_template.test_inputs.to('cuda:0'))
    torch.manual_seed(42)
    outputs_back_on_cpu = net_back_on_cpu(test_template.test_inputs)

    assert 0. == pytest.approx(torch.sum(outputs_cpu - outputs_gpu.cpu()), 0.01)
    assert 0. == pytest.approx(torch.sum(outputs_cpu - outputs_back_on_cpu), 0.01)

def test_batch_independence(test_template):
    inputs = test_template.test_inputs.clone()
    inputs.requires_grad = True

    # Compute forward pass in eval mode to deactivate batch norm
    test_template.net.eval()
    outputs = test_template.net(inputs)
    test_template.net.train()

    # Mask loss for certain samples in batch
    batch_size = inputs[0].shape[0]
    mask_idx = torch.randint(0, batch_size, ())
    mask = torch.ones_like(outputs)
    mask[mask_idx] = 0
    outputs = outputs * mask

    # Compute backward pass
    loss = outputs.mean()
    loss.backward()

    # Check if gradient exists and is zero for masked samples
    for i, grad in enumerate(inputs.grad):
        if i == mask_idx:
            assert torch.all(grad == 0).item() == True
        else:
            assert torch.all(grad == 0) != True





