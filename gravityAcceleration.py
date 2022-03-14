import math 



class GravityAcceleration:

    def __init__(self, t1, t3):
        self.t1 = t1
        self.t3 = t3

    def setdata(self, t1, t3):
        self.t1 = t1
        self.t3 = t3

    def gravityAcceleration(self):


        v1 = 0.1 * 2 / self.t1
        a = v1 / self.t1

        S = 1 / (a * 0.5) 

        t2 = math.sqrt(S)
        result = f'{t2 + self.t3:.4f}'
        return result
        # print(f'{result:.4f}')

a = GravityAcceleration(0.3792, 0.0807)
print(a.gravityAcceleration())
print(1.3757+1.2311+1.3168+1.2922+1.2798)
print(6.4956/5)
print(1.2991**2)
print(1.6876*0.08)
print(2/0.1350)