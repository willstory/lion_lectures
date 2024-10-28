from packages.utils import Lotto

def test_getData():
    lt = Lotto()
    assert lt.getData(1)['returnValue']=='success'