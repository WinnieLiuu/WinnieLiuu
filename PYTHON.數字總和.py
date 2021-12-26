'''請使用迴圈敘述撰寫一程式,讓使用者輸入一個正整數 a,
   利用迴圈計算從 1 到 a 之間(包含a),所有 7 的倍數數字總和'''

sum=0
num=eval(input('請輸入一個數字:'))
for i in range(num+1):
    if (i%7)==0:
        sum+=i
    i=i+1
print('從1到',num,'的總和是:',sum,sep='')
    

