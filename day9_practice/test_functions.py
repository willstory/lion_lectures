# 어떤 함수를 만드는데, 들어오는 문자열을 뒤집어서 리턴하는 함수
from lion_package.func import reverse_string, setting_random

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""

def test_random():
    assert setting_random()<=100 and setting_random()>=1