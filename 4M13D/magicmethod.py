'''
a = int(input())
print(type(a))
print(type(a.__str__())) # str(obj) -> obg.__str__()
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

print(b)
print(str(b))