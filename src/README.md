# Raspberry Pi

The 2022-2023 SwingTrainer team has elected to utilize a Raspberry Pi to be the internal computer for the weight distribution deck. 

## Setup and use

For instructions on how to operate the software, please refer to the [Literature](https://github.com/wbuz24/GolfTrainer23/tree/main/literature) directory.

If you are setting up a brand new raspberry pi, you must first load the [Raspbian](https://www.raspberrypi.com/software/) operating system onto your microSD card.
 - Insert your microSD into your computer and download the [Pi Imager] software for your computer's OS
 - Install the package and open the Pi Imager application
 - Select your desired Raspbian OS (for raspberry pi 4, be sure to download the 64 bit version)
 - Select your microSD as your destination and write
 - Remove your microSD and insert into your raspberry pi

Gather your materials for setting up your raspberry pi
 - keyboard
 - monitor
 - mouse
 - powersupply
 - Raspberry Pi hdmi connector
 - microSD with Raspbian OS
 
 ## Pull your desired hx711 repository
 
 You will need to pull your desired hx711 repository and use it's provided code, assuming you do not want to write your own GPio sensor library, in which case, please reach out to me because I would like to know what you do. 
 
 This is a reminder that I have extracted the hx711/src/SimpleHX711Test.cpp file from the repository to show you the adjustments I hard coded into the file, the file structure that I used is in the [sensors directory](https://github.com/WAMillerUTK/GolfTrainer23/tree/main/sensors). But those will need to be re-cloned from the [source directory](https://github.com/endail/hx711).

If you are looking for a place to start
-------

I recommend you get sensors reading through a button press on your Graphical User Interface and then get each individual sensor's designated C++ file to write to it's own tmp/ file.

Next, refer [here](https://github.com/WAMillerUTK/GolfTrainer23/tree/main/sensors).
