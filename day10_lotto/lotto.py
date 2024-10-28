from packages.utils import Lotto

def main():
    lotto = Lotto()
    lotto.get_all_datas()
    print(lotto.dataList)

if __name__=="__main__":
    main()