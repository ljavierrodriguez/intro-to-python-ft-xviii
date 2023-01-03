# functions

""" 

def funcName():
    pass


funcName = lambda (): print("Hello")


"""

def saludo():
    print("Hello")

saludo()

def sumar(a, b):
    return a + b

sumar2 = lambda a, b: a + b

def restar(a, b = 10):
    return a - b

restar(30)
restar(10, 5)