# first: basic function
# write a personalGreeting function which, after asking for the user’s name, outputs a personalised greeting, 
# e.g., for user input Sam, the function should output the greeting Hello Sam, nice to see you! Note the details of the spaces and punctuation

import os

def personalGreeting():
    userName = input("Please enter your name: ")
    greeting = f"Hello {userName}, nice to see you!"
    return greeting

print(personalGreeting())

# second: basic function
# write a formalName function which asks the user to input their given name and family name, and then outputs a more formal version of their name,
# e.g., on input Sam and Brown, the function should output S. Brown, again note the spacing and punctuation 

import os

def formalName():
    givenName = input("Please enter your given name: ")
    familyName = input("Please enter your family name: ")

    formalName = f"{givenName[0]}. {familyName}"

    return formalName

print(formalName())

# third: basic function
# copy the kilos2Ounces conversion function from your pract1.py file into your pract4.py file, 
# modify this function so that its output takes the form of a message such as s “12.34 kilos is equal to 435.28 ounces”, 
# where both the user’s kilos value and the calculated ounces values are displayed to two decimal places

import os

def kilos2Ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274

    conversion = f"{kilos:.2f} kilos is equal to {ounces:.2f} ounces"

    return conversion

print(kilos2Ounces())

# fourth: basic function
# suppose the university decides that students’ email addresses should be made up of the first 4 letters of their surname, 
# the first letter of their forename, and the final two digits of the year they entered the university, separated by dots, 
# write a function called generateEmail that outputs an email address given a student’s details, (e.g., if the user enters the following information: 
# Sam, Brown and 2023, the function should output:
# brow.s.23@myport.ac.uk

import os

def emailName():
    foreName = input("Please enter your given name: ")
    surName = input("Please enter your family name: ")
    yearEnAtUni = int(input("Please enter the year you joined the university: "))

    sNmPt = surName[:4].lower()
    fNmPtFl = foreName[:1].lower()
    yRAtUniEnd = str(yearEnAtUni)[:-2]

    email = f"{sNmPt}.{fNmPtFl}.{yRAtUniEnd}@myport.ac.uk"

    return email

print(emailName())

# fifth: basic function
# a teacher awards letter grades for test marks as follows: 8, 9 or 10 marks give an A, 6 or 7 marks give B, 4 or 5 marks give C, and 0, 1, 2 or 3 marks all give F,
# using string indexing, write a function gradeTest which asks the user for a mark (between 0 and 10) and displays the corresponding grade

def gradeTest():
    mark = int(input("Enter your test mark (between 0 and 10): "))

    if mark < 0 or mark > 10:
        print("Invalid input. Please enter a mark between 0 and 10.")
    else:
        grades = "FFFFCCBBAAA"
        grade = grades[mark]
        print(f"Your grade is: {grade}")

gradeTest()

# sixth: basic function
# write a function graphicLetters which first asks the user to enter a word, opens a graphics window, 
# and then allows the user to display the letters of the word at different locations by clicking the mouse once for each letter, 
# (use the setSize method of the Text class to make the letters appear big)

from graphics import *

def graphicLetters():
    word = input("Enter a word: ")
    
    win = GraphWin("Graphic Letters", 600, 400)
    win.setBackground('black')

    for letter in word:
        click_point = win.getMouse()
        
        text = Text(click_point, letter)
        text.setSize(36)
        text.setTextColor('white')
        text.draw(win)
    
    win.getMouse()
    win.close()

graphicLetters()

# seventh: basic function
# write a singASong function which outputs a “song” based on a single word, the user should be asked for the song’s word, how many lines long the song should be, 
# and how many times the word should be repeated on each line, for example, if the user enters the word “dum” and the numbers 2 and 4, 
# the function should then output the following song (note that the spaces are important):
# dum dum dum dum 
# dum dum dum dum

def singASong():
    word = input("Enter the word for your song: ")

    numOfLines = int(input("How many lines should the song have? "))

    repetitions = int(input("How many times should the word be repeated on each line? "))

    for x in range(numOfLines):
        line = " ".join([word] * repetitions)
        print(line)

singASong()

# eighth: basic function
# write a function exchangeTable that gives a table of euros values and their equivalent values in pounds, 
# using an exchange rate of 1.17 euros to the pound, the euro values should be 0, 1, 2, …, 20, and should be right justified, 
# the pound values should be right justified and given to two decimal places (i.e. with decimal points lined up and with pence values after the points)

def exchangeTable():
    exchangeRate = 1.17
    print(f"{'Euros':>10} {'Pounds':>10}")
    
    for euros in range(21):
        pounds = euros * exchangeRate
        print(f'{euros:>10} {pounds:.2f}')
        
exchangeTable()

# ninth: basic function
# write a makeInitialism function that allows the user to enter a phrase, and then displays the first letters of the words in capitals for that phrase, 
# for example, if the user enters “University of Portsmouth”, the function should display UOP, 
# (hint: first use the split method to find the words in the inputted string) 

def makeInitialism(phrase):
    words = phrase.split()
    
    initialism = ""
 
    for word in words:
        initialism += word[0].upper()
  
    print(initialism)

user_input = input("Enter a phrase: ")

makeInitialism(user_input)

# tenth: harder function
# harder: Write a nameToNumber function that asks the user for their name and converts it into a numerical value by adding up the “values” of its letters,
# (where ‘a’ is 1, ‘b’ is 2, …, ‘z’ is 26), so, for example, “Sam” has the value 19 + 1 + 13 = 33

def nameToNumber(name):
    letterValues = {letter: ord(letter) - ord('a') + 1 for letter in 'abcdefghijklmnopqrstuvwxyz'}
    
    name = name.lower()
    
    totalValue = 0
    
    for char in name:
        if char.isalpha():
            totalValue += letterValues[char]
    
    print(f"The numerical value of '{name}' is: {totalValue}")

userName = input("Enter your name: ")

nameToNumber(userName)


