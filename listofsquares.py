#create a list of squares upto 10

squares=[x**2 for x in range(10)]
print('squares:',squares)

#you can create list using exiting list

numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[x for x in numbers if x % 2 == 0]
odd_numbers =[x for x in numbers if x % 2 !=0]
print('Numbers: ',numbers)
print('Even numbers:',even_numbers)
print('odd_numbers', odd_numbers)