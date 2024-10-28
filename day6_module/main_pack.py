# package 사용하기
# likelion 패키지에 있는 show_lion.py 모듈을 사용하기
# 혹시 여기도 아까 모듈 임포트 했던 것처럼, 직접 변수나 함수도 불러와서 쓸수 있나??
# from likelion import show_lion # 이 부분이 이 형태로만 될까??
from likelion.show_lion import show_content
import pandas
def like():
    show_content()
    insert_msg()
    show_content()

def insert_msg():
    with open("data.txt", 'a', encoding='utf8') as f:
        msg = input("내용을 입력하세요")
        f.write("\n"+msg)
    print("-"*30)

like()