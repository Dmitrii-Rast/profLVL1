# def summa():
#     a=5
#     b=10
#     c=a+b
#     print(" СУММА",c)
# summa()
# def summa2(a,b):
#     c=a+b
#     print(" СУММА2",c)
# summa2(500,400)
# def mult():
#     def dele1():
#         a=10
#         b=2
#         c=a/b
#         print("Result1",c)
#     dele1()
#     def dele2():
#         a=100
#         b=2
#         c=a/b
#         print("Result2",c)
#     dele2()
# mult()

def decorator_func(func) :
    def obertka():
        print("Функция обертка")
        print("Выполняем обернутую функциию")
        d=1000
        func(d)
        print("Выходим из обертки")
    return obertka
@decorator_func
def summa(d):
     a=5
     b=10
     c=a+b+d
     print(" СУММА",c)
summa()
@decorator_func
def dele(d):
    c=d/5
    print("Деление",c)
dele ()
@decorator_func
def umno(d):
    c=d*2
    print ("Умножение",c)
umno ()