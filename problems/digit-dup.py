list1 = [202, 89, 112, 88]


def check_dup(number):
    seen = set()
    while number > 0:
        digit = number % 10
        if digit in seen:
            return True
        seen.add(digit)
        number = number // 10
    return False

for i in list1:
    print(f"{i} -> {check_dup(i)}")