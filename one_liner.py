def check_armstrong(num):
    return True if num == sum(list(map(lambda x:x**3,list(map(int,str(num)))))) else False

x = 123
print(check_armstrong(x))
