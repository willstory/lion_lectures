"""
# step 1
# 읽기
with open("data.txt", 'r', encoding='utf8') as f:
    content = f.read()
print(content)
print("-"*30)

# 쓰기
with open("data.txt", 'a', encoding='utf8') as f:
    msg = input("내용을 입력하세요")
    f.write("\n"+msg)
print("-"*30)

with open("data.txt", 'r', encoding='utf8') as f:
    content = f.read()
print(content)
print("-"*30)
"""

# step1 함수를 통해서 코드 재사용성을 높이자!!
# import show

from show import show_content

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