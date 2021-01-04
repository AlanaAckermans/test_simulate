#!usr/bin/env python

#INFO
__author__ = "Alana Ackermans, Fre Van Buynder"
__version__ = "0.0.1"

#LIBRARIES

#testcode voor simulate

sensordata = [2,7,5,6,8,9,5,2,3,4,1,]

def gemiddelde():
    middel = sum(sensordata)/len(sensordata)
    print(middel)

#FUNCTIONS


#MAIN FUNCTION
def main():
    gemiddelde()

#START PROGRAM
if __name__ == '__main__':
    main()
