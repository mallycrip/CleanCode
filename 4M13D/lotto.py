import random

class lotto:
    def __init__(self,input_):
        self.save = input_

    def rand_(self):
        if self.save <= 0:
            return 'No'
        else:
            return random.randrange(1, (self.save+1))

a = lotto(int(input()))
print(a.rand_())
