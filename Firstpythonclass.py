
class Myfirstclass(object):
    def add(self,a,b):
        return a+b;
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

def main():
    myobj = Myfirstclass()
    c = myobj.add(4,5)
    d = myobj.subtract(6,7)
    e = myobj.multiply(8,9)
    f = myobj.divide(200,5)
    print (c,d,e,f)

if __name__ == '__main__':
    main()    
