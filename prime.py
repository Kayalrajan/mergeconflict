def prime(num):
    if (num==1 or num==2 or num==3):
        print("Prime")
    elif num%2==0:
        print("Not a prime")
    else:
        for i in range(3,num,2):
            if (num%i==0):
                print("Not a prime")
                break
            else:
                print("Prime")
            break
num=int(input())
prime(num)
