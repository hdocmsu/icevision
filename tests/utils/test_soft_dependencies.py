from mantisshrimp.soft_dependencies import *


def test_soft_import():
    has_module = soft_import("collections")
    assert has_module


def test_soft_import_fail():
    has_module = soft_import("non_existent_module")
    assert not has_module


def test_soft_dependencies():
    assert SoftDependencies.check() == {
        "fastai2": True,
        "pytorch_lightning": True,
        "albumentations": True,
        "effdet": True,
    }
