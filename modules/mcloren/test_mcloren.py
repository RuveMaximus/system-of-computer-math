from . import mcloren

def test_exp():
    assert mcloren.exp(0) == 1
    assert mcloren.exp(1) == 2
    assert mcloren.exp(2) == 5

def test_sin():
    assert mcloren.sin(0) == 0
    assert mcloren.sin(1) == 0.8333333333333334
    assert mcloren.sin(2) == 0.9333333333333333

def test_cos():
    assert mcloren.cos(0) == 1
    assert mcloren.cos(1) == 0.5
    assert mcloren.cos(2) == -0.33333333333333337

def test_arcsin():
    assert mcloren.arcsin(0) == 1
    assert mcloren.arcsin(1) == 1.1666666666666667
    assert mcloren.arcsin(2) == 1.2416666666666667

def test_arccos():
    assert mcloren.arccos(0) == 0.5707963267948966
    assert mcloren.arccos(1) == 0.4041296601282298
    assert mcloren.arccos(2) == 0.32912966012822986