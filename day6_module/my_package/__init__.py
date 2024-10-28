from .module_a import function_a
from .module_b import function_b


# 패키지 수준의 변수 정의
package_variable = "이 변수는 my_package 전체에서 사용 가능합니다."

# 공용 함수 정의
def common_function():
    print("my_package의 공용 함수입니다.")
    
print("my_package 패키지가 임포트되었습니다.")