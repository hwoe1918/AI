#1
letters = 'python'
print(letters[0] + ' ' + letters[2])

#2
string = "PYTHON"
for i in range(6):
    print(string[5-i])

#3
x = ' '
x = input("url 입력: ")
for i in range(len(x)):
    if(x[-(i+1)] == 'r'):
        if(x[-(i+2)] == 'k'):
           print('index = ',len(x)-i-1, ' ', x[-(i+2)], x[-(i+1)], sep='')

#4
file_name = "보고서.xlsx"
suffix = "xlsx"
print(file_name.endswith(suffix))

#5
file_name2 = "2020_보고서.xlsx"
print(file_name2.startswith('2020'))

#6
a = int(input("성적 입력 : "))
if (a >= 81 and a <= 100) :
    print("학점 A")
elif (a >= 61 and a <= 80) :
    print("학점 B")
elif (a >= 41 and a <= 60) :
    print("학점 C")
elif (a >= 21 and a <= 40) :
    print("학점 D")
elif (a >= 0 and a <= 20) :
    print("학점 E")

#7
cook= ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print(len(cook))

#8
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
b = input("투자 종목 : ")
c = ' '

#print(type(bool_warn))
for i in range(len(warn_investment_list)):
    if(b == warn_investment_list[i]):
        print("투자 경고 종목입니다")
        c = 'T'
        break
    
    else:
        print(c)
        c = 'F'

if c == 'F' :
    print("투자 경고 종목이 아닙니다")


#9
sales_list = [100, 200, 300]
for i in sales_list:
    print(i+10)

#10
list2 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in list2:
    print(len(i))
