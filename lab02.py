import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Заданные параметры
n = 4.7
s = 16.9
fi = 3 * math.pi / 4

# Функция, описывающая движение катера береговой охраны
def f(r, tetha):
    dr = r / math.sqrt(n * n - 1)
    return dr

# Начальные условия для 1-го случая 
r0 = s / (n + 1)
tetha = np.arange(0, 2 * math.pi, 0.01)

# Начальные условия для 2-го случая 
r0 = s / (n - 1)
tetha = np.arange( -1 * math.pi, math.pi, 0.01)

r = odeint(f, r0, tetha)

# Функция, описывающая движение лодки браконьеров
def f2(t):
    xt = math.tan(fi) * t
    return xt 

t = np.arange(1, 10, 1)

r1= np.sqrt(t * t + f2(t) * f2(t))
tetha1 = np.arctan(f2(t) / t)

#Вывод графиков
plt.polar(tetha, r, 'b')
plt.polar(tetha1, r1, 'c')

# Нахождение точки пересечения катера и лодки
tmp = 0
for i in range (len(tetha)):
     if round(tetha[i],2) == round(fi + math.pi, 2): #1-й случай
     if round(tetha[i],2) == round(fi - math.pi, 2): #2-й случай
        tmp = i

print("Вывод координат:")
print("Точка пересечения в полярных координатах: tetha = ", tetha[tmp], ", r = ", r[tmp][0])
print("Точка пересечения в декартовых координатах: x = ", r[tmp][0] * math.cos(fi), ", y = ", r[tmp][0] * math.sin(fi))