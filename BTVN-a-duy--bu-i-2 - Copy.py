
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
#Bài 3:
a=str(input("Nhập một chuỗi"))
b=0
c=0
for i in a:
    if i.isupper():
        b=b+1
    if i.islower():
        c=c+1
print(b)
print(c)

       
#Bài 4:
list1=[1,2,3,4,5,6,7,8,9]
c=0
for i in  list1:
    c=c+i
print(c)
#Bài 5:
list_a=["hôm nay", "là", "thứ ba"]
b=input("Nhập một số tùy thích")
for i in list_a:
    if len(i)>len(b):
        print(i)
    else:
        continue
#Bài 6:
a=list(input("Nhập một list j đó").split())
b=str(a)
for i in b:
    if b.count(i)>1:
        c=set(b)
        d=c.remove(i)
        print(d)
    else:
        break
        
#Problem cuối:
a=str(input("Nhập một số tự nhiên bất kì"))
b=str(input("Nhập một số tự nhiên bất kì"))
if a[0] and b[0] ==0:
    skip
else:
   print(str(a+b))

