# Raspberry Pi Interface
The 2022-2023 GolfSwingTrainer Team utilizes a raspberry pi to be the in-house computer in order to successfully read the load cell data from the weight sensor. 

## How to Operate

The user interface has two buttons: 

Run - The "Run" button initializes the weight distribution deck to begin collecting inputs, stand on the board, press the button and wait until notified to swing. When the board begins to run, the user has 12 seconds to complete the swing, at which point a gif of the change in center of gravity over time will be displayed and an additional button to save will be displayed.

Exit - The "Exit" button will close the window and kill the program, but it cannot be initiated while "running". If you believe the board to be "frozen" attempt to close the window or reboot the raspberry pi.

Save - After running, the balance board will display a gif of the user's center of balance throughout the duration of their swing. An option to save will appear and if selected, a prompt will appear for a name, by default, the date will be name, followed by the number of saved gifs that day.
