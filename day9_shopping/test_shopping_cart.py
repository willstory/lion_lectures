# 쇼핑 카트가 있고
# 거기에 항목 추가한다
# 항목이라함은 상품명과 가격, 수량이다
# 딕셔너리 형태 정의 {name:상품명, price:가격, quantity:수량}

from shopping_cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("macbook", 5000000, 1)
    assert len(cart.items) == 1 # 하나 추가하면 하나 등록되야지
    assert cart.items[0] == {"name":"macbook", "price":5000000, "quantity":1} # 이 형식을 갖춰야지
    cart.add_item("마우스", 50000, 3)
    assert len(cart.items) == 2 # 하나 더 추가하면 두개 돼야지    

