# UTK Mechanical Engineering Senior Design Project

Task: Design and create a one-plane swing trainer to help instruct new golfers to learn
& feel the "one-plane swing"

Implementation: The team has elected to design their own weight distribution sensor by implementing load cell readings with a raspberry pi interface to display the status and tracking of the client's center of gravity in relation to space. 

The 'User' will be the Pro giving the lesson and is intended to be used as a tool to shed light on undesirable habits in beginner golfers.

The raspberry pi interface runs off the hx711 amplifier and accompanied software for use with the raspberry pi that can be downloaded [here](https://github.com/tatobari/hx711py) or by cloning this repository.

```
git clone https://github.com/tatobari/hx711py
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

The user interface is implemented with PyQt5

Installation
------------
The source code can be found in src/main.py

For compiling and running through the command line, python3 is necessary, therefore pip3 is required to install the following dependencies.

Other dependencies include:
 - PyQt5 (included in python3 installation)
 - RPi.GPIO
 - Git
 - pigpio

1. Clone or download and unpack this repository
2. In the repository directory, run
```
python3 src/setup.py install
```
If you are having an issue with permission,
```
sudo python3 src/setup.py install
```

Compilation
-----------
If running through the command line, you will need to first initiate the [pigpio](http://abyz.me.uk/rpi/pigpio/) daemon with the following command.

```
sudo pigpiod
```

Ensure you are running the program with python3 as python also comes installed on a raspberry pi, but will not work with our software. Therefore, pip3 will be used to install dependencies.

```
python3 src/main.py
```
