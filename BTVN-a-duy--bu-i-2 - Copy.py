
#Bài 2:
n = int(input("Nhập số cần tính giai thừa: "))
 
def giaithua(n):
    a=1
    if n==0 or n==1:
        return a
    else:
        for i in range (2, n+1):
            a=a*i
        return a
giaithua(n)
print(giaithua(n))
#Bài 4:
list1=[1,2,3,4,5,6,7,8,9]
c=0
for i in  list1:
    c=c+i
print(c)
#Bài 5:
list_a=["hôm nay", "là", "thứ ba"]
b=input("Nhập một cái gì đó tùy thích")
for i in list_a:
    if len(i)>len(b):
        print(i)
    else:
        continue
#Bài 6:
a=list(input("Nhập một chuỗi j đó").split())
def cau_moi(a):
    chuỗi=''
    for từ in a:
        if từ not in chuỗi:   
           chuỗi = chuỗi +' '+ từ
    return chuỗi
b=list(cau_moi(a).split())
print(b)


