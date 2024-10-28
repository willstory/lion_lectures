def display_menu(menu):
    print("\n===== 메뉴 =====")
    for i, (item, price) in enumerate(menu.items(), 1):
        print(f"{i}. {item}: {price}원")
    print("0. 주문 완료")

def get_user_choice(max_choice):
    while True:
        try:
            choice = int(input("메뉴 번호를 선택하세요 (0 입력시 주문 완료): "))
            if 0 <= choice <= max_choice:
                return choice
            else:
                print("올바른 메뉴 번호를 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

def take_order(menu):
    order = {}
    while True:
        display_menu(menu)
        choice = get_user_choice(len(menu))
        if choice == 0:
            break
        item = list(menu.keys())[choice - 1]
        quantity = int(input(f"{item}의 수량을 입력하세요: "))
        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity
        print(f"{item} {quantity}개가 주문에 추가되었습니다.")
    return order

def display_order(order, menu):
    if not order:
        print("주문 내역이 없습니다.")
        return 0
    print("\n===== 주문 내역 =====")
    total = 0
    for item, quantity in order.items():
        price = menu[item] * quantity
        total += price
        print(f"{item}: {quantity}개 - {price}원")
    print(f"총 금액: {total}원")
    return total

def process_payment(total):
    while True:
        try:
            payment = int(input(f"\n총 결제 금액은 {total}원입니다. 지불할 금액을 입력하세요: "))
            if payment >= total:
                change = payment - total
                print(f"결제가 완료되었습니다. 거스름돈: {change}원")
                break
            else:
                print("금액이 부족합니다. 다시 입력해주세요.")
        except ValueError:
            print("올바른 금액을 입력해주세요.")

def run_kiosk():
    menu = {
        "햄버거": 5000,
        "치즈버거": 5500,
        "프렌치 프라이": 3000,
        "콜라": 2000,
        "밀크쉐이크": 3500
    }
    
    print("키오스크에 오신 것을 환영합니다!")
    order = take_order(menu)
    total = display_order(order, menu)
    if total > 0:
        process_payment(total)
    print("이용해주셔서 감사합니다. 안녕히 가세요!")

if __name__ == "__main__":
    run_kiosk()