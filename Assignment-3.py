# Trey Wallace
# Professor: Md Ali 
# Olive-Harvey College
# CIS 103
# 09/21/2024
#-----------------
#Working with Lists
my_list = []

my_list.append("apple")
my_list.append("banana")
my_list.append("orange")
my_list.append("grape")
print(my_list)
my_list.remove("banana")
print(my_list)
my_list.append("strawberry")

print(my_list)
#Expected Output:
# ['apple', 'banana', 'orange', 'grape']
# ['apple', 'orange', 'grape']
# ['apple', 'orange', 'grape', 'strawberry']
#-----------------
#Using Tuples
colors = ("red", "green", "blue", "yellow")
print(colors)
print(colors[0])
print(colors[3])
#colors[1] = "perrywinkle" Tuples are immutable and are unable to be changed
#Traceback (most recent call last):
  #File "c:\Users\conta\OneDrive\Documents\CIS 103\Assignments\Assignment-3.py", line 29, in <module>
    #colors[1] = "perrywinkle"
    #~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
#-----------------
#Working with Sets
student_names = ["John", "Emma", "Sophia", "James"]
print(student_names)
student_names.append("Oliver")
print(student_names)
student_names.remove("Sophia")#Removes sophia
print(student_names)
student_names.append("John")#Add John again, no error happens it lets another John come in. Maybe because sets are mutable
print(student_names)
#------------------
#Using Dictionaries
student_scores = {
    "John":85, 
    "Emma":92, 
    "Sophia":78, 
    "James":89}
print(student_scores)
print("Emma's score:" + str(student_scores["Emma"]))#Just prints emmas score
student_scores["Oliver"]= 95 #Adds in Oliver
student_scores.update({"Sophia":82}) #Updates Sophia
print(student_scores)
#--------------------