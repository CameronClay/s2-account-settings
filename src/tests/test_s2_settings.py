import pytest
from src.s2_settings import *

def test_dir_path_valid():
    try:
        assert(dir_path('.') == '.')
    except Exception as e:
        pytest.fail(e)

def test_dir_path_invalid():
    with pytest.raises(argparse.ArgumentTypeError):
        dir_path('.__TEST___/hello')