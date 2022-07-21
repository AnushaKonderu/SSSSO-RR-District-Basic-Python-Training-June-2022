def add1(num):
    sum = 0
    while num:
        r = int(num % 10)
        sum += r  # 235=2+3+5
        num = int(num/10)
    return sum

def subtract1(num):
   
    lst = []
    while num:
        r = int(num % 10)
        num = int(num/10)
        lst.append(r)
    difference = lst[-1]
    for i in lst[:-1]:
        diff -= i 
    return diff


def multiply1(num):
    product = 1
    while num:
        product = product*int(num % 10)  
        num = int(num/10)
    return product

def divide1(num):
  
    lst = []
    while num:
        r = int(num % 10)
        num = int(num/10)
        lst.append(r)
    divide = lst[-1]
    for i in lst[:-1]:
        divide /= i  # 123=1/2/3
    return divide


with open("input.txt", 'r') as f:
    n = f.read()
num = int(n)
sum = add(num)
difference = subtract(num)
product = multiply(num)
result = divide(num)
lines = {"sum": sum, "difference": difference,
         "product": product, "division result": result}
string = str(lines)


with open("output.txt", "w") as f:
    f.write(string)