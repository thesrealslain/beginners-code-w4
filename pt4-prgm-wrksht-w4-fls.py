# first: basic function
# Write a fileInCaps function which prints the contents of a file in capital letters, 
# the name of the input file should be typed in by the user, try your function with our quotation.txt file

def fileInCaps(fileName):
    try:
        with open(fileName, 'r') as file:
            fileContents = file.read()
            fileContentsInCaps = fileContents.upper()
            print(fileContentsInCaps)
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

file_name = input("Enter the name of the input file: ")

fileInCaps(file_name)

# second: basic function 
# jenny uses a text file to write down how much she spends on food every day of the week, 
# open the spending.txt file that she wrote last week and save it. See the content of this file, 
# observe, for example, that Jenny spent £29.10 on Wednesday, 
# then write a function called totalSpending that reads the spending.txt file and prints the total sum of money spent that week

def totalSpending(file_name):
    try:
        with open(file_name, 'r') as file:
            total_sum = 0
            for line in file:
                words = line.split()
                for word in words:
                    try:
                        number = float(word)
                        total_sum += number
                    except ValueError:
                        pass  

            print(f"Sum of all numbers in the file: £{total_sum}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

file_name = "spending.txt" 

totalSpending(file_name)

# third: harder function
# the file rainfall.txt contains rainfall data in millimetres (mm) for several UK cities for a particular day, 
# open it to see the format of this file and download it, 
# write a function rainfallChart that displays this data as a textual bar chart using one asterisk for each mm of rainfall, 
# for instance, the first three lines of the output should be:
# Portsmouth *********
# London *****
# Southampton ************

def rainfallChart(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                city, rainfall_mm = line.strip().split(" ")
                chart = '*' * int(rainfall_mm)
                print(f"{city} {chart}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

file_name = "rainfall.txt"  

rainfallChart(file_name)

# now write a graphical version graphicalRainfallChart that displays a similar bar chart in a graphical window but uses filled rectangles,
# instead of sequences of asterisks

from graphics import *

def graphicalRainfallChart(file_name):
    try:
        win = GraphWin("Graphical Rainfall Chart", 500, 300)
        
        with open(file_name, 'r') as file:
            y = 20
            for line in file:
                city, rainfall_mm = line.strip().split(" ")
                rainfall_mm = int(rainfall_mm)

                bar = Rectangle(Point(10, y), Point(10 + rainfall_mm * 10, y + 20))
                bar.setFill('purple')
                bar.setOutline('white')
                bar.draw(win)
              
                text = Text(Point(40, y + 10), city)
                text.setTextColor('white')
                text.setSize(8)
                text.draw(win)
                y += 30
        
        win.getMouse() 
        win.close()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

file_name = "rainfall.txt"  

graphicalRainfallChart(file_name)

# fourth: harder function 
# write a rainfallInInches function that reads the rainfall.txt file, 
# and outputs the data to a file rainfallInches.txt where all the mm values are converted to inches (there are 25.4 mm in an inch), 
# the inch values should be given to two decimal places, so the Portsmouth line above will become: 
# Portsmouth 0.35 

def rainFallInInches(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            with open(output_file, 'w') as output:
                for line in file:
                    city, rainfall_mm = line.strip().split(" ")
                    rainfall_mm = float(rainfall_mm)
                    rainfall_inches = round(rainfall_mm / 25.34, 2)
                    output.write(f"{city} {rainfall_inches: .2f}\n")
        print("Conversion to inches is completed. Output written to", output_file)
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

input_file = "rainfall.txt"
output_file = "rainfallininches.txt"

rainFallInInches(input_file, output_file)

# fifth: harder function
# in Linux, there is a command called wc which reports the number of characters, words, and lines in a file, 
# write a function wc which performs the same task, the name of the file should be entered by the user

def wc(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            char_count = len(content)
            word_count = len(content.split())
            line_count = content.count('\n') + 1

            print(f"Character count: {char_count}")
            print(f"Word count: {word_count}")
            print(f"Line count: {line_count}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occured: {str(e)}")

file_name = input("Enter the name of the file: ")

wc(file_name)