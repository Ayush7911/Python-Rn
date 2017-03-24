point1=int(input('x: '))

point2=int(input(' y: '))

x=point1
y=point2

if x == 0 and y == 0 :
    print('origin')

elif x>0 and y>0:
    print('First quadrant')

elif x<0 and  y>0:
    print('2nd quadrant')

elif  x<0 and  y<0:
    print('3rd quadrant')

elif  x>0 and  y<0:
    print('4th quadrant')
