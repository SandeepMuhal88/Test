# find factorial of a number ?

def factorial(num):
    fact=1
    if num<0:
        print("NOt exist that factoriyal")
    elif num==0:
        print("Factoriyal :-",num)
    else:
        while(num!=1):
            fact*=num
            num-=1
        print(fact)
            
factorial(4)

