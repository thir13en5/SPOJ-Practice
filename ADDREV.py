t = int(input())

for t_i in range(t):
    num1, num2 = map(int, input().split())
    divisor = 10
    rev_num1 = []
    rev_num2 = []
    while(num1//10 >= 0 and num2//10 >= 0):
        rev_num1.append(num1%10)
        num1 = num1//10
        rev_num2.append(num2%10)
        num2 = num2//10
    print(rev_num1)