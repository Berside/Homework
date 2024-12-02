import re
a = '152-783-614 14'
b = '126-029-036 24'
c = '111-222-333-44'
d = '123-45-789 100'
g = '167-695 478-00'
bv = '187-220-276 69'

listSnilc = [a,b,c,d,g,bv]


def Correct(str):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{3} \d{2}$')
    lastTwo = str[-2:]
    total_sum = 0

    if pattern.match(str):
        l = str.replace("-", "")
        for i in range(0, len(l) - 3):
            total_sum = int(l[i]) * (9 - i) + total_sum

        if total_sum < 100 and total_sum == int(lastTwo):
            return "Correct"

        if total_sum in (100, 101) and total_sum == int(lastTwo):
            return "Correct"

        if total_sum > 101 and total_sum % 101 == int(lastTwo):
            return "Correct"

    return "Incorrect"


for i in range(len(listSnilc)):
    result = Correct(listSnilc[i])
    print(f'Номер СНИЛСа: {listSnilc[i]} --> {result}')