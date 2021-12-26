'''請設計一程式,執行時會先要求要輸入的次數,再接著輸入每次要顯示的
個數(1~10),程式會列印出該對應數量的*號'''

times=eval(input('請輸入要輸入的次數：'))
for i in range(times):
    num=eval(input('請輸入第{:d}個數值(數值介於1~10之間)：'.format(i+1)))
    while num<1 or num>10:
        num=eval(input('輸入錯誤，請重新輸入：'))
    else:
        print('*'*num)
print('程式已執行完畢')    





