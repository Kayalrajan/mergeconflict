num=int(input("Please enter the value "))
# fact1=1
# for i in range(1,num+1):
#     fact1*=i

# print(f"The factorial of {num} is {fact1}")
# sum=1
# for i in range(1,num+1):
#     sum+=i

# print(f"The sum of {num} is {sum}")

def fac(num):
    if num==1 or num==0:
        return 1
    else:
        return(num*fac(num-1))

a=fac(num)
print("The factorial is ",a)
