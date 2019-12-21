from pynput.keyboard import Key, Controller
import serial
import sys
import time
import serial.tools.list_ports
from random import *

#Marche po
ports = list(serial.tools.list_ports.comports())
port="/dev/ttyACM0"
for p1 in ports:
    print(p1)
    if "Arduino" in p1:
        print("ok")
        port = p1
    

"""
try:
except:
    print("Something went wrong when finding the arduino port")
"""
keyboard = Controller()
ser = serial.Serial(port)

def bit():
    while 1:
        a = ser.read()
        #print("Read from com")
        #print(a)
        keyboard.press(a) 
        keyboard.release(a)

def ascii():
    while 1:
        word = ""
        while len(word) < 7:
            word += ser.read()#`randint(0,1)`
            print(word[len(word)::-1]) # method 1

        word=word[len(word)::-1]
        trueBin = int(word, base=2)
        trueBin = chr(trueBin)

        try:
            if trueBin == '\n':
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            elif trueBin == '\b': #Might change
            else:       
                keyboard.press(trueBin)
                keyboard.release(trueBin)
            
        except:
            pass



def test():
    while 1:
        print("writing to com")
        ser.write(0)
        time.sleep(2)
        ser.write(1)
        time.sleep(2)

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'bit':
            bit()
        elif sys.argv[1] == 'ascii':
            ascii()
        elif sys.argv[1] == 'test':
            test()
    else:
        print("You must choose a mode (bit or ascii)")

main()

#Useless for now
'''
def switch(i):
        switcher={
                0:'0',
                1:'Monday',
             }
         return switcher.get(i,"Invalid char received")
'''
