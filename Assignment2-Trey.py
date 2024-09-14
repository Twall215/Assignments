# Trey Wallace
# Professor: Md Ali 
# Olive-Harvey College
# CIS 103
# 09/07/2024

#While loop#
y = 0
while y<= 10:
    if y == 7:
       break
    else:
        y += 1
        print(y)
##########

#Forloop#
product = "CIS103Lab3"
for index in range(len(product)):
    print(product[index])
########

#NestedLoop#
for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()

#BreaknContinue#
y = 0
while y<= 10:
    if y == 7:
       break
    if y == 5:
       y += 1
       continue #needs to skip 5
    print(y)
    y += 1

#####

#String Reversal#

def reverse_string(s):
    return s[::-1]

my_string = "Lec2Python"
print(reverse_string(my_string))

######

#List Operations#
my_list = [10, 20, 30, 40, 50]

my_list.append(60) # 10, 20, 30, 40, 50, 60
 
my_list.pop(2)     # 10, 20, 40, 50, 60 

# Sort in descending order
my_list.sort(reverse=True) # 60, 50, 40, 20, 10

print(my_list)

########

#Tuples#
my_tuple = (4, 5, 6, 7, 8)

# Print first and last elements
print("First element:", my_tuple[0]) # 4 
print("Last element:", my_tuple[-1]) # 8

# Attempt to modify the second element
try:
    my_tuple[1] = 10
except TypeError as e:
    print("Error:", e)

#######

#Dictionary#
student_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Add Burrow
student_dict['Burrow'] = 'Brooklyn'

# Modify age
student_dict['age'] = 27

# Remove major
student_dict.pop('city') #we know the city if you mention the burrow

# Print all keys and values
for key, value in student_dict.items():
    print(f"{key}: {value}")

#######