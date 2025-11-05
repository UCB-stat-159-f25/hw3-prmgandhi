from ligotools import readligo as rl
import pytest

def test_read_frame_raises_typeerror_for_ifoNone():
    with pytest.raises(TypeError):
        rl.read_frame("dummyfile.gwf", ifo=None)

def test_dq2segs_raises_keyerror_when_dic_missing_DEFAULT():
    bad_input = {"MISSING_DEFAULT": [0, 1, 0, 1]}
    gps_start = 1000000000
    with pytest.raises(Exception):
        rl.dq2segs(bad_input, gps_start)

