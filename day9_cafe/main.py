# 매장이용, 포장 선택 화면 -> lion 개발자
# 고객이 접속하면(파이썬 파일 실행하면)
# "멋사 카페에 오신것을 환영합니다" 메시지 출력
from cafe_package.lion import title
greeting = title()

print(greeting)


# "매장/포장 선택" 메시지 출력
# 응답을 받기 (매장 or 포장) -> 문자열              cf. 딕셔너리, 구조...
choice = input("매장 또는 포장 을 선택해 주세요 : ")


"""
# 고객 선택 과정 -> tiger 개발자
# 응답 분석 ( 매장 or 포장 인지 확인, 문자열...)

# "매장 or 포장 을 선택하셨습니다" 메시지 출력
print(f"{choice}를 선택하셨습니다.")
"""