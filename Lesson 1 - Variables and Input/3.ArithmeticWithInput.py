#In this lesson we are looking at how python treats different types of variables.
print()

#Here we have 2 variables that are given "5" and "6". Since the numbers are in quotations python treats these as WORDS and NOT as numbers.
numberOne = "5"
numberTwo = "6"

#Since our variables are words python will simply put the words next to eachother. Run this code and youll see instead of printing 5 + 6 which is 11, python will print 56
newNumber = numberOne + numberTwo

print("This is the variables added together without conversion:")
print(newNumber)
print()

#The function 'int()' converts wrods to numbers. To use it you put the words you want to convert inside the brackets. For example int(numberOne)
testNumber = int(numberOne) + 3

print("This is after the variables are converted:")
print(testNumber)
print()

#--------------------------------------------EDIT THIS CODE---------------------------------------------------------


#Add and edit the code to convert numberOne and numberTwo into numbers. Add them together and store the result into the newNumber variable.

newNumber = numberOne + numberTwo


#--------------------------------------------EDIT THIS CODE---------------------------------------------------------

print("This is my converted variable, it should equal 11:")
print(newNumber)
print()