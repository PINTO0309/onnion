import numpy as np
from onnion_runtime import LessOrEqual

from .utils import check


def test_lessorequal_00():
    opset_version = 13
    attrs = dict()

    x = np.random.randn(3, 4, 5).astype(np.float32)
    y = np.random.randn(3, 4, 5).astype(np.float32)
    inputs = [x, y]

    check(LessOrEqual, opset_version, attrs, inputs)


def test_lessorequal_01():
    opset_version = 13
    attrs = dict()

    x = np.random.randn(3, 4, 5).astype(np.float32)
    y = np.random.randn(5).astype(np.float32)
    inputs = [x, y]

    check(LessOrEqual, opset_version, attrs, inputs)
