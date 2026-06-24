def number():
    while True:
        try:
            num = float(input('Enter a number: '))
            return num
        except ValueError:
            print('Only the entered number is accepted!')


def choice():
    ch = ('+', '-', '/', '*')
    while True:
        c = input("Choose any arithmetic operation: '+', '-', '/', '*' : ")
        try:
            if c not in ch:
                raise ValueError  
            return c
        except ValueError:
            print("Only these operations are allowed:", ch)


def result():
    x = number()
    c = choice()
    y = number()
    
    if c == '+':
        res = x + y
        return f"{x} + {y} = {res}"
    elif c == '-':
        res = x - y
        return f"{x} - {y} = {res}"
    elif c == '*':
        res = x * y
        return f"{x} * {y} = {res}"
    elif c == '/':
        while True:
            try:
                if y == 0:
                    raise ZeroDivisionError  
                res = x / y
                return f"{x} / {y} = {res}"
            except ZeroDivisionError:
                print("A number is not divisible by 0!")
                y = number()

               
print(result())
    
   

    
