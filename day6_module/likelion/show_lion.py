# 함수, 변수, 클래스

def show_content():
    with open("data.txt", 'r', encoding='utf8') as f:
        content = f.read()
    print(content)
    print("-"*30)