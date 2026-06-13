def number():
    while True:
        try:
            number = float(input('Enter a number:'))
            return number
        except ValueError:
            print('Only the entered number is accepted!')


def choice():
    ch = ('+','-', '/', '*')
    c = input("Choose any arithmetic operation:'+', '-', '/', '*'")
    try:
        if c not in ch:
            raise Exception
    except:
        print("only", ch)
        c = input("'+', '-', '/', '*'") 

    return c 

def result():
    x = number()
    c = choice()
    y= number()
    if c == '+':
        res = x + y
        return f"{x} + {y} = {res}"
    elif c == '-':
        res = x-y
        return f"{x} - {y} = {res}"
    elif c == '*':
        res = x*y
        return f"{x} * {y}={res}"
    elif c == '/':
        while True:
            try:
                if y==0:
                    raise Exception
                res= x/y
                return f" {x}/{y}={res}"
            except Exception:
                print("A number is not divisible by 0!")
                y=number()
               
print(result())                


    