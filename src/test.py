from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import PySimpleGUI as sg
import time

#Home Sreen

def main(): 
    app =QApplication([]) # create a window
    window = QWidget()

    W = 1800 # Setting Window Dimensions 
    H = 900
    window.setStyleSheet("background-color: grey;")

    swingimage = QImage("swing.png")
    swing = swingimage.scaled(QSize(10000,1000))
    swing = QLabel(window) # just trying to block this freaking image 
    swing.show()
    swing.move(int(W/2.6),int(.2*H))
    swing.resize(340,400)
    swing.setStyleSheet("color:white;background-color:none; background-image: url(swing);")

    title = QLabel(window) # Title 
    title.setText("Level Swing")
    title.show()
    title.move(int(W/2.8), int(.3*H))
    title.setFont(QFont('Times',70))
    title.resize(int(W/3),int(H/3))
    title.setStyleSheet("color:white;background-color:none;")
    title.setAlignment(QtCore.Qt.AlignCenter)

    # run button
    runButton = QPushButton(window)
    runButton.setText("Press to Record Weight Shift")
    runButton.setStyleSheet("""
        QPushButton {
            background-color: orange; 
            color:black;
            border-radius : 20;
        }
        QPushButton:hover {
            background-color: white;
        }
        QPushButton:click {
        background-color:blue;
        }
    """)
    runButton.setGeometry(int(.31*W),int(.6*H),740,60)
    runButton.setFont(QFont('Arial',30))
    runButton.clicked.connect(record_weight_shift)
    #runButton.animateClick(200)

    #settings button
    settingsButton = QPushButton(window)
    settingsButton.setText("Settings")
    settingsButton.setStyleSheet("""
        QPushButton {
            background-color: orange; 
            color:black;
            border-radius : 30;
        }
        QPushButton:hover {
            background-color: white;
        }
    """)
    settingsButton.setGeometry(int(.86*W),int(.03*H),250,60)
    settingsButton.setFont(QFont('Arial',30))
    #settingsButton.animateClick(200)

    #exit button
    exitButton = QPushButton(window)
    exitButton.setText("Exit")
    exitButton.setStyleSheet("""
        QPushButton {
            background-color: orange; 
            color:black;
            border-radius : 20;
        }
        QPushButton:hover {
            background-color: white;
        }
    """)
    exitButton.setGeometry(int(.45*W),int(.7*H),220,60)
    exitButton.setFont(QFont('Arial',30))
    #exitButton.animateClick(200)
    exitButton.clicked.connect(window.close)

     # creating a command link button

    window.setWindowTitle("Golf balance window")
    window.show() # show window
    app.exec_()

def record_weight_shift(window):
    time.sleep(3)
    while True:
        # End program if user closes window or
        # presses the OK button
        # THE FOUR VALUES BELOW REPRESENT THE LIVE WEIGHTS PULLED FROM THE 4 PRESSURE SENSORS (THE FOUR CORNERS OF
        # THE BOARD. FOR NOW THEY ARE SET TO AN EMPTY LIST SO LATER WE CAN ASSIGN RANDOM NUMBERS TO EACH SENSOR
        LTL = [50, 35, 20, 10, 30, 55, 85, 120, 110]
        LHL = [50, 40, 30, 15, 20, 50, 75, 70, 85]
        RTL = [50, 65, 75, 80, 45, 55, 20, 5, 2.5]
        RHL = [50, 60, 75, 95, 105, 40, 20, 5, 2.5]

        LTLP = [50, 45, 30, 15, 35, 60, 95, 110, 90]
        LHLP = [50, 50, 30, 15, 35, 55, 65, 80, 90]
        RTLP = [50, 75, 80, 90, 75, 45, 25, 5, 5]
        RHLP = [50, 50, 60, 80, 75, 40, 15, 5, 5]

        # THESE ARE OPTIONAL FOOTPRINT IMAGES FOR THE BACKGROUND OF OUR PLOT`
        img = plt.imread("LFP.jpg")
        img2 = plt.imread("RFP.jpg")

        # HERE WE ARE DEFINING AN ANIMATE FUNCTION. THIS ALLOWS US TO WATCH THE PLOT CHANGE IN REAL TIME

            # UNTIL WE GET ACTUAL READINGS FROM OUR SENSORS, I AM GENERATING RANDOM NUMBERS
            # (FOR NOW WE CAN CONSIDER THESE POUNDS)
            # I AM GENERATING 4 RANDOM NUMBER OF POUNDS, 1 FOR EACH SENSOR, RANGING FROM 0 TO 25
            # LTL is Left toe, RHL is right heel, etc...
        """
        LTL.append(random.randint(0, 25))
        LHL.append(random.randint(0, 25))
            RTL.append(random.randint(0, 25))
            RHL.append(random.randint(0, 25))
            """
            # THOSE NUMBERS ABOVE ARE GENERATED AS A LIST, HERE I AM CONVERTING THEM TO AN ARRAY IN ORDER TO MAKE CALCULATIONS
        LT = np.array(LTL)
        LH = np.array(LHL)
        RH = np.array(RHL)
        RT = np.array(RTL)

        LTP = np.array(LTLP)
        LHP = np.array(LHLP)
        RHP = np.array(RHLP)
        RTP = np.array(RTLP)

            # W IS EQUAL TO THE TOTAL WEIGHT, CALCULATED BY SUMMING ALL 4 PRESSURE READINGS
        w = LT + LH + RH + RT
        wP = LTP + LHP + RHP + RTP

            # BELOW ARE THE X AND Y VALUES OF OUR PLOT. X REPRESENTING LEFT TO RIGHT CENTER OF GRAVITY,
            # Y REPRESENTING HEEL TO TOE CENTER OF GRAVITY
            # (I SUBTRACTED .5 TO SIMPLY PLACE OUR ORIGIN IN THE MIDDLE, SEE PLOT)
            # NOTE: X = .5 WILL OCCUR WHEN 100% OF WEIGHT IS ON RIGHT FOOT, X = -.5 IF ALL ON LEFT FOOT

        x = ((RT + RH) / w) - .5
        y = ((LT + RT) / w) - .5

        xP = ((RTP + RHP) / wP) - .5
        yP = ((LTP + RTP) / wP) - .5

        plt.cla()  # formatting
        plt.scatter(x, y, label="You", color="blue")  # scatter plots each (x,y) point
        plt.plot(x, y)  # connects the scatter plot in order
        plt.scatter(xP, yP, label="Our Pro Average", color="orange")  # scatter plots each (x,y) point
        plt.plot(xP, yP)  # connects the scatter plot in order
        plt.xlim([-.5, .5])  # formatting
        plt.ylim([-.5, .5])  # formatting

            # MORE FORMATTING, PUTS 0,0 AT CENTER OF PLOT RATHER THAN BOTTOM LEFT
        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')

            # LINES 66 - 75 IS HOW I GOT THE DIRECTION ARROWS ON THE PLOT, THIS WILL BE BOTH USEFUL
            # AND ADD BETTER AESTHETICS ONCE WE CAN GET SWINGING ON OUR BOARD

        df = pd.DataFrame.from_dict({'x': x,
                                         'y': y})
        x = df['x'].values
        y = df['y'].values

        u = np.diff(x)
        v = np.diff(y)
        pos_x = x[:-1] + u / 2
        pos_y = y[:-1] + v / 2
        norm = np.sqrt(u ** 2 + v ** 2)

        dfP = pd.DataFrame.from_dict({'xP': xP,
                                          'yP': yP})
        xP = dfP['xP'].values
        yP = dfP['yP'].values

        uP = np.diff(xP)
        vP = np.diff(yP)
        pos_xP = xP[:-1] + uP / 2
        pos_yP = yP[:-1] + vP / 2
        normP = np.sqrt(uP ** 2 + vP ** 2)

            # BELOW I AM BASICALLY PLOTTING OUR ARROWS  AND BACKGROUND ON TOP OF THE PLOT I MADE ABOVE

        plt.cla()  # formatting
        plt.imshow(img, extent=[-.4, -.15, -.2, .2])  # puts image in background of plot
        plt.imshow(img2, extent=[.15, .4, -.2, .2])  # puts image in background of plot
        plt.scatter(x, y, label="You")
        plt.plot(x, y)
        plt.scatter(xP, yP, label="Average Pro")
        plt.plot(xP, yP)
        plt.quiver(pos_x, pos_y, u / norm, v / norm, angles="xy", zorder=5, pivot="mid", color="grey")  # arrows
        plt.quiver(pos_xP, pos_yP, uP / norm, vP / normP, angles="xy", zorder=5, pivot="mid",
                       color="grey")  # arrows

        plt.xlim([-.5, .5])
        plt.ylim([-.5, .5])
        plt.xticks([])
        plt.yticks([])
        plt.title("Center of Gravity Throughout Swing")
        plt.legend(loc="upper right")

        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.set_facecolor("white")

        plt.show()

        # FINALLY, I AM CALLING THE ANIMATE FUNCTION SO THE PLOT CAN BE WATCHED, INTERVAL MEANS I AM GETTING A NEW VALUE
        # EVERY X (HERE SET TO 5) MILLISECONDS,
        # FRAMES IS HOW MANY DIFFERENT POINTS I AM REQUESTING (HERE REQUESTING 10), REPEAT = FALSE TERMINATES THE FUNCTION

        #ani = FuncAnimation(plt.gcf(), animate, interval=1000, frames=10, repeat=False)
        #plt.show()
        break




if __name__ == '__main__':
    main()
