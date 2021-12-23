#exercise2
#假設一賽跑選手在X分Y秒的時間跑完Z公里,請撰寫一程式,輸入X、Y、Z數值,最後顯示此選手
#每小時的平均英哩速度(1英哩等於1.6公里)。
#請輸出浮點數到小數點後第一位。
x=eval(input('請輸入幾分鐘:'))
y=eval(input('請輸入幾分秒:'))
z=eval(input('請輸入幾公里:'))

hr=((y/60)+(x))/60
mile=z/1.6

#1.336小時完成62.5英哩
speed=mile/hr
print('speed=','{:.1f}'.format(speed))

