# method 구성 - method 추출
# method에 많은 code가 있을수록 파악이 어려워진다. 이것이 method 추출의 주된 이유이다.
# 코드 중복이 적어지고, method를 재활용할 수 있다.
# 코드를 독립적인 부분으로 격리함으로서 오류가 발생할 가능성이 줄어든다.

# Extract method 방법
# 1. 새로운 method를 만들고, 목적을 명확하게 표현하는 이름을 부여한다.
# 2. 관련 코드를 잘라내어 새로운 method에 붙여넣고, 이전 위치에서 새로운 method를 호출한다.
# 관련 코드에 사용된 모든 변수를 찾아내야 한다. 관련 코드에서만 선언되고 외부에서 사용되지 않는 경우
# 변경하지 않고 그대로 두면 method의 local 변수가 된다.
# 3. 추출한 코드 이전에 선언된 변수를 사용하려 한다면 새 method의 parameter로 넘겨줘야 한다.
# 때로는 Replace Temp with Query 방법을 사용하여 변수를 처리할 수도 있을 것이다.
# 4. 추출한 코드에서 local 변수가 어떤 식으로든 변경된다면
# 해당 변수는 나중에 main method에서 필요할 수도 있다.
# 잘 검토하여 main method에 필요하다면 해당 변수를 main method로 옮겨놓아야 한다.


# print_info method를 보면 추출할 수 있는 부분이 존재한다.
class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f"name: {self.name}")

    def print_info(self):
        self.print_name()

        # 나이 출력
        print(f"age: {self.age}")


# 새로운 method를 만들고 명확한 이름을 부여한다.
class NewGuest:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f"name: {self.name}")

    def print_age(self):
        print(f"age: {self.age}")

    def print_info(self):
        self.print_name()
        self.print_age()
