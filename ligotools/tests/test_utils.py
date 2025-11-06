from ligotools import utils
import pytest
import numpy as np
from scipy.io import wavfile

def test_write_wavfile_length_and_max():
    fs = 44100
    t = np.linspace(0, 1, fs, endpoint=False)
    data = 0.5 * np.sin(2 * np.pi * 440 * t)
    filename = "test.wav"
    utils.write_wavfile(str(filename), fs, data)

    fs_read, data_read = wavfile.read(filename)

    assert fs_read == fs
    assert len(data_read) == len(data)

    max_val = np.max(np.abs(data_read))
    assert np.isclose(max_val, int(32767 * 0.9), atol=1)


def test_reqshift_basic_properties():
    fs = 1024
    t = np.arange(0, 1, 1/fs)

    f0 = 50
    data = np.sin(2*np.pi*f0*t)

    fshift = 100
    shifted = utils.reqshift(data, fshift=fshift, sample_rate=fs)

    assert len(shifted) == len(data)

    shifted_fft = np.fft.rfft(shifted)
    nbins_expected = int(fshift / (1.0 / (len(data)/fs)))
    assert np.allclose(shifted_fft[:nbins_expected], 0, atol=1e-12)