#202 Happy Number
n = 19
def happy_number(n):
    seen=set()
    while n!=1:
        if n in seen:
            print("true")
        seen.add(n)
        total =0
        while n>0:
            digit =n%10
            total = total + (digit**2) 
            n=n//10
        n=total
    print("false")       
print(happy_number(n))