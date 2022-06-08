from cmath import sqrt
import math
import numpy as np
l1 = 57.2
l2 = 40.5
l3= 0
d2= 42.5 ## base from ground
x=int(input("input the x co-ordinate: "))
y=int(input("input the y co-ordinate: "))
z=int(input("input the z co-ordinate: "))

theta_1_up = math.degrees(math.atan(y/x))
print('Theta_1: {}'.format(theta_1_up))

d1= y - l3
d9= z - d2
d6 = (math.sqrt((d1*d1)+(d9*d9)))
theta_2= (math.degrees(math.acos(d1/d6))) + math.degrees(math.acos(((l1*l1)+(d6*d6)-(l2*l2))/(2*l1*d6))) 
theta_2_up = theta_2 + 20.5
print('Theta_2: {}'.format(theta_2_up))

theta_3 = math.degrees(math.acos(((l1*l1)+(l2*l2)-(d6*d6))/(2*l1*l2)))
theta_3_updated = theta_3 - 11.5
print('Theta_3: {}'.format(theta_3_updated))

gg = np.cos(theta_3_updated)
act2=math.sqrt((9.5*9.5)+(38.5*38.5)-(2*9.5*38.5*gg))
pot_of_act2= (11.3418*act2) +176.299
print(act2)

print("pot_of_actuator 2: {}".format(pot_of_act2))

gg2 = np.cos(theta_2_up)
act1=math.sqrt((9.1*9.1)+(40*40)-(2*9.1*40*gg2))
pot_of_act1= 18.0472*act1 -32.5536	
print(act1)
print("pot_of_actuator 1: {}".format(pot_of_act1))
