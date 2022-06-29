# method 구성 - Split Temporary Variable
# 관계없는 값을 같은 변수로 재사용할 시 다양한 문제가 발생할 수 있다.
# 각 변수는 사용 사례에 맞춰 정의되어야 한다.

# 이득
# * 프로그램 코드의 각 구성요소는 독립적이고 한 가지 역할을 갖는 것이 좋다.
# 구성 요소를 독립적으로 유지하면 특정 부분을 교체할 때 의도하지 않은 영향을 피할 수 있다.
# * 코드가 읽기 쉬워진다. 변수의 이름에 아무런 의미를 두지 않고 a, b 처럼 부여하는 것은
# 나중에 의미를 파악하기 어려워진다.

# Refactoring 방법
# 1. 코드에서 변수의 값이 처음 지정된 것을 찾는다. 그리고 해당 값에 알맞는 변수 이름으로 교체한다.
# 2. 하단에 이전 변수 이름을 사용하던 부분을 새 변수 이름으로 교체한다.
# 3. 1, 2의 작업을 반복하며 변수를 독립적으로 선언한다.

height = 100
width = 200

# method 또는 코드에 여러 값을 저장하는 같은 이름의 변수가 존재 (반복문에서 사용되는 변수 제외)
temp = 2 * (height + width)
print(temp)
temp = height * width
print(temp)

# 다른 값에 대해서는 다른 이름의 변수를 사용하게 만듦
perimeter = 2 * (height + width)
print(perimeter)
area = height * width
print(area)