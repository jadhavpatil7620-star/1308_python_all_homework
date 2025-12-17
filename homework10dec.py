n="Gopal_Jadhav"
print(n,len(n))
print(n[::2])
print(n[2::-1])
print(n[:5:3])
print(n[8:1:-2])
for i in n:
    print(i)
count=1
for i in n:
    if i=="a":
        count=count+1
print(f"Total char of a in {n}=",count)
for i in n[:5:3]:
    print(i)
for i in range(len(n)):
    print(i)
for i in n[::-2]:
    print(i)
count=0
for i in n:
    if i=="d":
        count=count+1
print(count)
print(n[::])
m=0
for i in n:
    if i=="a":
        m=m+1
print(m)