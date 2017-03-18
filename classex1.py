a= input("input your maths marks:")
b= input("input your science marks:")
c= input("input your social marks:")
d= input("input your history marks:")
e = input("input your health marks:")

total_marks=float(a)+float(b)+float(c)+float(d)+float(e)
percentage =(float(total_marks) / 500)* 100
print("total marks = {}".format( total_marks) )
#{:.2f} means to print in new style and to show .00 and % is to show % at last
print("\nPercentage = {:.2f} %".format(percentage))



