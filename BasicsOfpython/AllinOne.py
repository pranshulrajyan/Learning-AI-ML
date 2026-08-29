print("Hii", "Welcome to Python Programming")
name = "Pranshul" #name is a variable which stores the name of the user
print("My name is", name)
print(type(name)) #type() is a function which tells the type of variable
age = 18
print(name, age)
#Print Sum
a = 1
b= 2
sum = a + b
print("The sum of", a, "and", b, "is", sum)
 #input() is a function which takes input from the user
#the type of input() is always string, so we need to convert it into int or float if we want to perform any mathematical operation on it
country = input("enter your country name: ")
print("I am from", country)
print("The length of the country name is:", len(country)) #len() is a function which tells the length of the string
#Slicing of string
string = "Python Programming"
print(string[0:6]) #prints the first 6 characters of the string
print(string[7:18]) #prints the characters from index 7 to 17
#ending index is not included in the output

#slicing with negative index
print(string[-11:0]) #prints the characters from index -11 to -1

#String Functions
string1 = "Python is a programming language"
print(string1.upper()) #converts the string to uppercase
print(string1.lower()) #converts the string to lowercase
print(string1.replace("Python", "Java")) #replaces the word Python with Java
print(string1.split(" ")) #splits the string into a list of words
print(string1.find("programming")) #finds the index of the word programming
print(string1.count("a")) #counts the number of occurrences of the word a  
print(string1.startswith("Python")) #checks if the string starts with Python    
print(string1.endswith("language")) #checks if the string ends with language
print(string1.isalpha()) #checks if the string contains only alphabets
print(string1.isdigit()) #checks if the string contains only digits
print(string1.capitalize()) #capitalizes the first letter of the string

#Conditional Statements
age = int(input("Enter your age: "))
if(age >= 18):
    if(age >= 80):
        print("You are eligible to vote and also you are senior citizen")
    else:
        print("You are eligible to vote")
else:
    print("You are not eligible to vote")  