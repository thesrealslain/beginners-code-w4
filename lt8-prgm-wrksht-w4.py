# write a Python program that: prompts the user to input a sentence and then,
# splits the sentence into words using the space character as the delimiter
# finally, it prints each word on a separate line

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    print(word)

# users to input a sentence, the program then splits the sentence into words using spaces as delimiters and counts the number of words,
# the program creates a graphical window named "Words on screen" with a size of 500x500 pixels, 
# for each word in the sentence, the program randomly selects a word,
# and displays it at the position where the user clicks within the graphical window,
# this process continues for as many words as there are in the original sentence

from graphics import *

def sentenceClick():

    sentence = input("Please enter a sentence: ")

    words = sentence.split()
    words_count = len(words)

    win = GraphWin("Words On Screen", 500, 500)

    for word in words:
        click_point = win.getMouse()
        text = Text(click_point, word)
        text.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    
    sentenceClick()

# ceate a Python program that generates a graphical window named "Coordinates on screen" with a size of 500x500 pixels, 
# the program increments the coordinates by 100 units both horizontally and vertically in a grid pattern using nested loops,
# users can click within the window to display each coordinate one at a time, 
# and the program records the coordinates from the nested loops in the "(x,y)" format and displays them on the screen


from graphics import *

def coordsWindow():

    win = GraphWin("Coordinates On Screen", 500, 500)
    win.setBackground('black')

    cell_size = 100

    for x in range(0, 500, cell_size):
        for y in range(0, 500, cell_size):
            click_point = win.getMouse()
            coords = f"({x},{y})"
            text = Text(Point(x + cell_size / 2, y + cell_size / 2), coords)
            text.setTextColor('#FFFF33')
            text.draw(win)
    
    win.getMouse()
    win.close()

if __name__ == "__main__":
    coordsWindow()