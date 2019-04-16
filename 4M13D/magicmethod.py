'''
a = int(input())
print(type(a))
print(type(a.__str__())) # str(obj) -> obg.__str__()

객체 생성 -> __init__()
print() -> __repr__()
len() -> __len__()
str() -> __str__()

'''

class cls:
    def __init__(self,a,b):
        self._a = a
        self._b = b

    def __repr__(self):
        return '{}asdf {}'.format(self._a,self._b)

    def __str__(self):
        return str(self._a) + str(self._b)

    
b = cls(1,3)

print(b)    #print 를 사용시 __repr__ 
print(str(b)) # str 사용시 __str__
