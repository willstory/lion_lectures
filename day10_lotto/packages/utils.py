import requests

class Lotto:
  def __init__(self):
    self.dataList = []

  def get_all_datas(self):
    drwNo=1141 # Debug용 변수 설정
    while True:
      data = self.getData(drwNo)
      if data['returnValue'] == 'fail':break
      self.dataList.append(data)
      drwNo+=1  

  def getData(self, drwNo):
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={drwNo}"
    response = requests.get(url)
    return response.json()