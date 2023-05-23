# UTK Mechanical Engineering Senior Design Project

Task: Design and create a one-plane swing trainer to help instruct new golfers to learn
& feel the "one-plane swing"

Implementation: The team has elected to design their own weight distribution sensor by implementing load cell readings with a raspberry pi interface to display the status and tracking of the client's center of gravity in relation to space. 

The 'User' will be the Pro giving the lesson and is intended to be used as a tool to shed light on undesirable habits in beginner golfers.

The raspberry pi interface runs off the hx711 amplifier and accompanied software for use with the raspberry pi that can be downloaded [here](https://github.com/endail/hx711). (All four repository instances are currently in the "sensors" folder of this repository, upon cloning this repository, those folders will need to be re-cloned from the original repository)

```
git clone https://github.com/endail/hx711
```

## Advisor

Dr. William Miller

## Members

Christian White

Robert Vandergriff

Job Dooley

Chilo Espinoza

[Will Buziak](https://github.com/wbuz24/Undergrad-Repo/blob/master/S23/will-buziak-resume.pdf)

## Sponsor
[Fairways and Greens](https://fairwaysandgreens.com/)


## HX711 for Raspberry Py
----

This repository has utilized a number of different libraries in an attempt to gather many sensor inputs and display them at an appropriate sampling rate in order to accurately display the change in weight distribution during the golf swing. The intent is to display the user's shift in center of gravity throughout the duration of the swing as an instruction tool accompanied by examples of trained professionals.

After successfully utilizing an arduino to read digital signals from four separate load cells attached through HX711 amplifiers, the UT Golf Swing Trainer 2022/2023 team attempted to use the RPi.GPio libraries. This was successful in reading all sensor values, however, the sampling rate was far too slow to give an accurate representation of each variation in weight. 

Next, the team was successful in increasing the reading frequency by using the pigpio libraries implemented in C using python wrappers. However, it introduced a multitude of issues reading all four sensors simultaneously. Therefore, the UTK team began to collect the reading using an arduino and do the post-processing with a raspberry pi. 

The team was advised to then utilize the endail/hx711 libraries in C. This was successful in quickly reading all four input readings individually and by running four different shells simulatenously with different files could read all four sensors in parallel. By this time it was the end of the year and there was no more time to finish working out the rest of the kinks associated with the project. What is left to implement is detailed below.

The user interface is implemented with PyQt5

Installation
------------
The source code can be found in src/main.py

For compiling and running through the command line, python3 is necessary, therefore pip3 is required to install the following dependencies.

Other dependencies include:
 - PyQt5 (included in python3 installation)
 - RPi.GPIO
 - Git
 - make

1. Clone or download and unpack this repository
2. In the repository directory, run
```
python3 src/setup.py install
```
If you are having an issue with permission,
```
sudo python3 src/setup.py install
```

For the hx711 repositories, you will need to create separate instances of the directory and name them for easy identification. Modify each src/SimpleHX711Test.cpp file to designate your desired GPio pins.

Compilation
-----------

Ensure you are running the program with python3 as python also comes installed on a raspberry pi, but will not work with our software. Therefore, pip3 will be used to install dependencies.
```
python3 src/main.py
```
If you are compiling the executable for the C++ code, you will need to compile with make and run the executable associated. To run in parallel, open multiple shell instances and run the respective directories' executable.

```
./bin/simplehx711test
```
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
