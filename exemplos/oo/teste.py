from calculadora import Calculadora, Calculadora_v2
from user import User

c = Calculadora(128, 2)
print('Soma:', c.soma())

c2 = Calculadora_v2()
print('Soma:', c2.soma(1, 1))

u1 = User('Regis', 35)
u1.save()
u2 = User('Fabio', 20)
u2.save()
print(User.all())


'3-12':[0,4,8],
'3-2':[0,1,8],
'3-3':[0,2,8],
'3-4':[0,1,8],
'3-5':[0,2,8],
'3-6':[0,4,8],
'3-7':[0,2,8],
