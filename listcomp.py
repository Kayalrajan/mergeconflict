##if __name__ == '__main__':
##    x = int(input())
##    y = int(input())
##    z = int(input())
##    n = int(input())
##    res=[]
##    for i in range(x):
##        for j in range(y):
##            for k in range(z):
##                if i+j+k !=n:
##                    res.append([i,j,k])
##print(res)

##if __name__ == '__main__':
##    x = int(input())
##    y = int(input())
##    z = int(input())
##    n = int(input())
##res = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
## 
##print(res)


##class teacher:
##    def __init__(self,name,reg):
##        self.name=name
##        self.reg_no=reg
##    def display(self):
##        print("Name:", self.name)
##        print("registration",self.reg_no)
##
##t1=teacher('kayal','5555')
##t2=teacher('kalai','7777')
##
##t1.display()
##t2.display()

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)

c1=calculator(10,5)

c1.add()
c1.sub()
c1.mul()
c1.div()
    
