# 여기가 중심 파일
# from lion_module import msg
# from lion_module import *
import lion_module
import lion_module2

txt = "hello"
# print(lion_module.msg)
# lion_module2.get_topic()

import pandas as pd

name = ["임종한", "일론머스크", "샘 알트먼"]
company = ["멋사","기사식당", "현대 백화점"]

df = pd.DataFrame({"name":name, "company":company})
print(df)