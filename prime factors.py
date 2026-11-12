import math
m_list = []
def is_prime(number):
    for i in range(1,int(math.sqrt(number))+1):
        m_list.append(number/i)

    if 0 in m_list:
        return False
    else:
        return True

factor_list = []
x = int(input("enter your number"))
while x > 1:
    if x % 2 == 0:
        factor_list.append(2)
        x = x//2
    for i in range(3,x+1,2):
        if is_prime(i):
            if x % i == 0:
                factor_list.append(i)
                x = x // i
        else:
            break


print(sorted(factor_list))
