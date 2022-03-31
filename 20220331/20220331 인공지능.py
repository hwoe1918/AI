#import numpy
#1
price_list = [32100, 32150, 32000, 32500]
for i in range(0, 4):
    print(i, price_list[i])

#2    
for i in range(1, 4):
    print(90+10*i, price_list[i])

#3
for i in range(2002, 2051, 4):
    print(i)

#4
#python IDLE에서 numpy가 import되지 않습니다
#float_list = numpy.arange(0, 1, 0.1)
f_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for i in f_list:
    print(i)

#5
ticker = "btc_krw"
ticker_upper = ticker.upper()
print(ticker_upper)

#6
file_name = "보고서.xlsx"
suffix = "xlsx"
print(file_name.endswith(suffix))

#7
a = "hello world"

x = a.split()

print(x)

#8
date = "2020-05-01"
s_date = date.split('-')
print(s_date)

#9
상장주식수 = "5,969,782,550"
replace1 = int(상장주식수.replace(",",""))
print(replace1, type(replace1))

#10
#7번과 같은 문제입니다.

#11
price = ['20180728', 100, 130, 140, 150, 160, 170]

print(price[1:])

#12
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1:10:2])

#13
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if(i%3 == 0):
        print(i)
