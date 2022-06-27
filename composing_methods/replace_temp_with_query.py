# method 구성 - Replace temp with query
# 어떤 수식의 결과 값을 저장하기 위해서 임시 변수를 사용하고 있다면
# 수식을 뽑아내어 method로 생성한 뒤, 임시 변수를 모두 method 호출로 바꾼다.
# 새로 만든 method는 다른 곳에서도 사용될 수 있다.

# 성능 이슈
# 매번 method를 호출할 때 마다 부담이 있을 수 있다.
# 스팩에 이슈가 있을 때에는 새 method로 분리한 뒤 변수에 할당하여 사용이 가능하다.

# Replace temp with query 방법
# 1. method로 변경하고자 하는 값이 method 내에서 한 번만 변수에 할당되어야 한다.
# 그렇지 않은 경우, "Split temporary variable"을 사용하여 변수가 식의 결과 저장에만 사용되게 한다.
# 2. Extract method를 사용하여 식을 분리한다. 이 떄, 값만 반환해야 하며 값이 변경되면 안된다.
# 만약 값을 변경해야 한다면 "Separate query from modifier"를 사용해야 한다.
# 3. 모든 변수를 method로 변경한다.


quantity = 10
item_price = 10


# 임시 변수를 local 변수로 사용
def calculate_total():
    base_price = quantity * item_price
    if base_price > 1000:
        return base_price * 0.95
    else:
        return base_price * 0.98


# 임시 변수를 함수로 변경하여 사용
def new_calculate_total():
    if new_base_price() > 1000:
        return new_base_price() * 0.95
    else:
        return new_base_price() * 0.98


def new_base_price():
    return quantity * item_price
