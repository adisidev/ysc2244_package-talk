# Importing Tkinter
import tkinter as tk

# For Sound Effects (PyObjC)
from AppKit import NSSound

# Slides and their content
# postfixed with "_sub": Subject line
# postfixed with "_cont": Content of the slide

# Package name (1pt)
intro_sub = "Welcome to Adi's Package Talk!"
intro_cont = """Package name (1pt): Tkinter"""

# Why does this package exist ? (Motivation, History, still relevant...) (2pt)
package_hist_sub = "Tk has an Existential Crisis"
package_hist_cont = """
Why does this package exist ? (Motivation, History, still relevant...) (2pt)

Sometimes, I ask myself this very same question!

History: Stemmed from Tk, Tkinter just a python binding of Tk. Tk is free, open-source, cross-platform for many langauges which was initially built by John Ousterhout in 1991 as an extension for the Tcl scripting language. It was initially written in C.

Relevancy: de facto standard GUI toolkit, hence, obviously still very relevant. Included with standard OS installs of Python (for instance in Linux, Windows, macOS).
"""

# What is it for ? (2pt)
uses_sub = "Does Tkinter have any uses?"
uses_cont = """
What is it for ? (2pt)

The more I go through this presentation, the more targeted these questions become!

And yes, it does have uses; it's use is to make a Graphical User Interface (GUI), rather than having everything be text based!
"""

# Competitors ? (2pt)
comp_sub = "The Fight to Death"
comp_cont = """
Competitors ? (2pt)

PyQT5
(free, good for QT designers, GPL License)

PySide 2
(another QT for Python, main difference is licensing, LGPL License)

Others:
Kivy (free to use, MIT license)
PyGUI

"""

# How to use it (give one or two examples). (3pt + up to 2pt for simplicity)
how_to_sub = "How to use Tkinter?"
how_to_cont = """
How to use it (give one or two examples). (3pt + up to 2pt for simplicity)

Well, we're going to build our very own add point button! Live coding session!
"""


# For you, what is fun and what is not in this package? (2pt + up to 2pt for clarity)
good_bad_sub = "The Good and the Bad"
good_bad_cont = """
For you, what is fun and what is not in this package? (2pt + up to 2pt for clarity)

Bad:
- No GUI to make the GUI (recursion?).
- Rigid placement settings which can be tough to get around.
- Initial impression makes it look tough to customise a lot.

Good:
- Relatively simple to get into, not an extremely steep learning curve for basic functions.
- Well written documentation as part of docs.python.org.
- Lots of easy to follow tutorials and community support online.
"""

# Do you like or dislike it, explain why. (1pt)
like_dis_sub = "What's the verdict, Adi?"
like_dis_cont = """
Do you like or dislike it, explain why. (1pt)

Overall, I like it! 10/10 would Tkinter again

Would've preferred it to be easier but still is a good starting point for making GUI applications.
"""

# Do you like or dislike it, explain why. (1pt)
end_sub = "La Fin"
end_cont = """
Format of the slides (2pt)

Originality of the presentation (1pt)
"""

# Resources used
resources_used_sub = "Resources Used (apart from Brain, Coffee & Time)"
resources_used_cont = """
Making a Presentation with Tkinter (https://www.youtube.com/watch?v=uH127Hsj2XQ)
Learn Tkinter in 20 Minutes (https://www.youtube.com/watch?v=_lSNIrR1nZU)
Making GUI App (https://www.youtube.com/watch?v=itRLRfuL_PQ)
Getting sound to work (https://stackoverflow.com/questions/13941/python-sound-bell)
Changing initial position (https://yagisanatode.com/2018/02/23/how-do-i-change-the-size-and-position-of-the-main-window-in-tkinter-and-python-3/)
Getting Color (https://stackoverflow.com/questions/48054027/how-to-change-the-background-color-of-a-tkinter-column)
Changing Text options (https://www.tutorialspoint.com/python/tk_text.htm)
Stopwatch (https://www.youtube.com/watch?v=mdfuJPGLhPM)
About Tk (https://en.wikipedia.org/wiki/Tk_(software))
About Tkinter (https://en.wikipedia.org/wiki/Tkinter#Window)
"""

# Making slides
subjects = [intro_sub, package_hist_sub, uses_sub, comp_sub, how_to_sub, how_to_sub, good_bad_sub, like_dis_sub, end_sub]
contents = [intro_cont, package_hist_cont, uses_cont, comp_cont, how_to_cont, how_to_cont, good_bad_cont, like_dis_cont, end_cont]


# Preparing sound
sound = NSSound.alloc()
sound.initWithContentsOfFile_byReference_('./ding-sound-effect_2.mp3', True)

# Function to play sound effect
def ding() :
    sound.stop()
    sound.play()

# Counter for slide number (to display La Fin instead of next button)
counter = 0

# To move to next page
def next() :
    global counter, next_button

    # Checking whether we should change the button to say La Fin
    if counter == len(subjects) - 2:
        next_button.config(text = 'La Fin')

    # Checking whether we should exit the slideshow
    if counter == len(subjects) - 1:
        exit()

    # Adding 1 to count of slides
    counter += 1

    # Adding subject
    subject.config(text = subjects[counter])
    # subject.insert('1.0', package_hist_cont.split('\n')[counter]) # Showing next slide

    # subject.delete('1.0', tk.END) # Clearing all text from 1.0 to END
    # subject.insert('1.0', package_hist_cont.split('\n')[counter]) # Showing next slide

    # Adding content
    content.config(text = contents[counter])

# Counter for points
points = 0

# Making the add point button
def add_point() :
    global points
    points += 1
    ding()
    score_label.config(text = f"Points: {points}")

# Function to update stopwatch
minutes, seconds = 0, -1
def update():

    # Update seconds with (addition) compound assignment operator
    global minutes, seconds, stopwatch_label
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0

    # Format seconds to include leading zero
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    # Update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=f'{minutes}: {seconds_string}')

    # After each second (1000 milliseconds), call update function
    stopwatch_label.after(1000, update)

# Setting up window
root = tk.Tk()
root.title("Adi's Presentation on tkinter")

# Getting screen sizes
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Making my presentation fullscreen
root.attributes('-fullscreen', True)

# Making a frame for the text and the subject
text_frame = tk.Frame(root, bg = '#e74c3c')
text_frame.grid(column = 0, row = 0)
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

# Adding Subject to window
subject = tk.Label(text_frame, anchor=tk.CENTER, font = ("Courier", 45), height = 1, bg = '#101010', text = subjects[0])
subject.grid(row = 0, column = 0)

# Adding content to window
content = tk.Label(text_frame, anchor=tk.CENTER, font = ("Courier", 30), text = contents[0])
content.grid(row = 1, column = 0)

# Making the next button
next_button = tk.Button(root, text = 'Next', command = next)
next_button.grid(column = 2, row = 0)

# Label displaying current number of points
score_label = tk.Label(root, text = f"Points: {points}")
score_label.grid(column = 2, row = 1)

# Button to add a point
add_point_button = tk.Button(root, text = 'Add Point', command = add_point)
add_point_button.grid(column = 2, row = 2, padx = 10, pady = 10)

# Label displaying stopwatch
stopwatch_label = tk.Label(root, anchor=tk.CENTER, font = ("Courier", 25), text = '0:00')
stopwatch_label.grid(column = 0, row = 1, rowspan = 2)
update()

# Configuring text to wrap
content.configure(wraplength = int(screen_width * 0.7))

# Starting the window
root.mainloop()
