# READ ME
The various "hx711" folders in this directory should be replaced with clones of the [endail](https://github.com/endail/hx711) repository (or whichever sensor repository you choose). I have extracted one of the [SimpleHX711Test.cpp](https://github.com/WAMillerUTK/GolfTrainer23/blob/main/src/SimpleHX711Test.cpp) files for reference and slightly modified the file to be hard coded to a specific GPio pin and reference unit. Re-clone the hx711 repository and replace the SimpleHX711Test.cpp file fouind in the [src](https://github.com/WAMillerUTK/GolfTrainer23/tree/main/src) folder.


Note: 
-------

Please understand that from this point on, this project is largely software and good programming techniques are essential.

If you are the student who has been tasked with continuing this project, I highly recommend learning basic [Linux/Unix](https://www.geeksforgeeks.org/basic-linux-commands/) commands and [git](https://github.com/WAMillerUTK/GolfTrainer23/blob/main/literature/github.pdf). I was successful in getting close to finishing, but did not have the man hours to complete it. I will briefly describe what there is left to implement. 

At the current moment, each sensor can be read individually with it's own respective shell and the user interface is written in a bare-bones fashion. There are a number of things that must be implemented in order to have a fully functioning balance board. (The gui-test.py script can be used as a GUI template, each sensor's C++ file is within it's sensors/hx711 directory) 

The Issue:
--------

The problem to solve is reading all four values simultaneously fast enough and how to store the data efficiently. For example: printing, regardless of if it is to a file or directly to the screen, takes lots of computational time and can ruin the reading rate of the data, this can be mitigated by only printing/writing at the optimal time to balance your memroy usage and compute time.

It is imperative that you keep the rate at which you are reading data in mind as well as run time of the code you are executing. This is the issue with using a language like Python as it was my experience that Python did not offer enough control over memory, nor was it fast enough reading data.

TO DO
--------

Using the implementation I have been building on, you can proceed by:

1: Implement a shell script that writes to individual files, this should be able to be run on a button press within the GUI

Write a shell script that will open all four shells and run the executable from within the main python script. Instruct each program to write to it's own individual temporary file. After all four individual files are written to (ideally within the same tmp directory), compile all four data files to one which can then be read by the main python script and processed for visualization. 

2: Convert the raw data file to a gif or other visualization medium

The raw data file will need to be manipulated with the associated math formulas to find the user's center of gravity. I recommend manipulating the data so that no values will "fall off" the sides of the "graph".

Then, it will be ideal to convert/compile the data into a medium that is useful for visualization and replaying. 

3: Implement a method that can save the gif or other medium to a desired file name

This should be implemented into the user interface by a button that can bring up a text box that the user can then enter a desired file name. If the user does not decide to save that iteration, it should be discarded to not waste memory. If the user decides to save the file, it should be directed somewhere other than a "tmp" folder. The user should be able to easily pull up older files for reference/demonstration.

Additional notes:
-----------------

You are welcome to try using python, but I found the speed to be insufficient and with a lack of experience with python data structures and difficulty managing memory in python, I was incapable of reading data simulataneously or even close to an appropriate speed.

I understand that much of what is left to do is writing not-so-straightforward C++ code and shell scripting. I apologize that this is a tall order for a group of mechanical engineers as this is largely a computer science/electrical engineering problem . I certainly would have maintained a cleaner structure to what I was working on, but I did not expect to pass this work on to anybody and I am aware that this is outside of the breadth of the typical mechanical coursework, therefore, smart use of data structures and awareness of your clock cycles and runtime will be important. Best of luck. 
