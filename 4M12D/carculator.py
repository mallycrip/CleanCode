class carculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        if self.second == 0:
            return 'No'
        else:
            result = self.first / self.second
            return result

input1 = input()
input2 = input()

a = carculator(int(input1), int(input2))

input_car = input()

'''
if input_car == 'sum':
    print(a.sum())
elif input_car == 'sub':
    print(a.sub())
elif input_car == 'mul':
    print(a.mul())
elif input_car == 'div':
    print(a.div())
else:
    print("No")
'''


while(1):
