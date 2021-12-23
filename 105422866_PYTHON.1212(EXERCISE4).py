#exercise4
#請撰寫一程式
#將使用者輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式,此函式將回傳x和y的乘積。

def compute(x=10,y=25):
    x=eval(input('請輸入x:'))
    y=eval(input('請輸入y:'))
    z=x*y
    print(z)

compute()

