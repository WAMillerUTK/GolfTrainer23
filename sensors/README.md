# READ ME
The various hx711 folders in this directory should be replaced with clones of the endail repository. I have extracted one of the SimpleHX711Test.cpp files for reference. I slightly modified the file to be encoded to a specific GPio pin.

TODO
----------

Note: If you are the student who has been tasked with continuing this project, I highly recommend learning basic [Linux/Unix](https://www.geeksforgeeks.org/basic-linux-commands/) commands and git. I have a git introductory powerpoint that can get you started, but using these tools are the best way to learn and the only way you will progress in this project. I was successful in getting close to finishing, but did not have the man hours to complete it. I will briefly describe what there is left to implement.

At the current moment, each sensor can be read individually with it's own respective shell and the user interface is written in a bare-bones fashion. There are a number of things that must be implemented in order to have a fully functioning balance board. (The pigpiod.py script currently only implements the user interface with an older library. Therefore, it should only be used as a GUI template, each C++ file is within it's sensors/hx711 directory, but will require to be re-cloned since it is a git "subdirectory")

1: Implement a shell script that writes to individual files, this should be able to be run on a button press within the GUI

Write a shell script that will open all four shells and run the executable from within the main python script. Instruct each program to write to it's own individual temporary file. After all four individual files are written to (ideally within the same tmp directory), compile all four data files to one which can then be read by the main python script and processed for visualization. 

2: Convert the raw data file to a gif or other visualization medium

The raw data file will need to be manipulated with the associated math formulas to find the user's center of gravity. I recommend manipulating the data so that no values will "fall off" the sides of the "graph".

Then, it will be ideal to convert/compile the data into a medium that is useful for visualization and replaying. 

3: Implement a method that can save the gif or other medium to a desired file name

This should be implemented into the user interface by a button that can bring up a text box that the user can then enter a desired file name. If the user does not decide to save that iteration, it should be discarded to not waste memory. If the user decides to save the file, it should be directed somewhere other than a "tmp" folder. The user should be able to pull up older files for reference/demonstration.

Additional notes:
-----------------

I understand that much of what is left to do is writing not-so-straightforward C++ code and shell scripting. I apologize that this is a tall order for a group of mechanical engineers as this is largely a computer science/electrical engineering problem (if you are the CS or EE chosen to help/finish this, please spare me for I was alone in this effort and did not have much time to work). I am probably to blame for the high amount of software involved in this project as I figured I would be able to complete the project before it was passed on. But I am aware that this is outside of the breadth of the typical mechanical coursework, for that I apologize. Best of luck to you in your endeavor to fix the mess that I have created.
