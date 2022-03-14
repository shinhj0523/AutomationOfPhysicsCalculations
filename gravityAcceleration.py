import math 


t1 = 0.3638
t3 = 0.0807
class GravityAcceleration:

    def __init__(self, t1, t3):
        self.t1 = t1
        self.t3 = t3

    def setdata(self, t1, t3):
        self.t1 = t1
        self.t3 = t3

    def gravityAcceleration(self):
        self.t1 = t1
        self.t3 = t3

        v1 = 0.1 * 2 / self.t1
        a = v1 / self.t1

        S = 1 / (a * 0.5) 

        t2 = math.sqrt(S)
        result = f'{t2 + self.t3:.4f}'
        return result
        # print(f'{result:.4f}')

a = GravityAcceleration(0.3638, 0.0807)
print(a.gravityAcceleration())
# print(gravityAcceleration(t1, t3))