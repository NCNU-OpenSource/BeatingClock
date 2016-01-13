import RPi.GPIO as GPIO
import time
from Adafruit_CharLCD import Adafruit_CharLCD

#init
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
lcd = Adafruit_CharLCD()

#enter(button)
#up(button)
#down

#setting
first = 0
second = 0
third = 0
forth = 0
lcd.clear()
def myprint(f,s,t,f4):
    lcd.clear()
    lcd.home()
    lcd.message("   time setting\n")
    lcd.message("   ")
    lcd.message(str(f))
    lcd.message(str(s))
    lcd.message(":")
    lcd.message(str(t))
    lcd.message(str(f4))
try:
    while True:
        enter = GPIO.input(8)
        if enter == False:
            time.sleep(1)
            enter = True
            while enter:
                myprint(first,second,third,forth)
                up = GPIO.input(11)
                if up == False:
                    if first == 9:
                        first = 0
                    else:
                        first = first + 1
                down = GPIO.input(13)
                if down == False:
                    if first == 0:
                        first = 9
                    else:
                        first = first - 1
                enter = GPIO.input(8)
                if enter == False:
                    break
                time.sleep(0.5)
            time.sleep(1)
            enter = True
            while enter:
                myprint(first,second,third,forth)
                up = GPIO.input(11)
                if up == False:
                    if second == 9:
                        second = 0
                    else:
                        second = second + 1
                down = GPIO.input(13)
                if down == False:
                    if second == 0:
                        second = 9
                    else:
                        second = second - 1
                enter = GPIO.input(8)
                if enter == False:
                    break
                time.sleep(0.5)
            time.sleep(1) 
            enter = True
            while enter:
                myprint(first,second,third,forth)
                up = GPIO.input(11)
                if up == False:
                    if third == 5:
                        third = 0
                    else:
                        third = third + 1
                down = GPIO.input(13)
                if down == False:
                    if third == 0:
                        third = 5
                    else:
                        third = third - 1
                enter = GPIO.input(8)
                if enter == False:
                    break
                time.sleep(0.5)
            time.sleep(1)
            enter = True
            while enter:
                myprint(first,second,third,forth)
                up = GPIO.input(11)
                if up == False:
                    if forth == 9:
                        forth = 0
                    else:
                        forth = forth + 1
                down = GPIO.input(13)
                if down == False:
                    if forth == 0:
                        forth = 9
                    else:
                        forth = forth - 1
                enter = GPIO.input(8)
                if enter == False:
                    break
                time.sleep(0.5)
            time.sleep(1)
        myprint(first,second,third,forth)
except KeyboardInterrupt:
    RUNNING = False
    print "\nQuitting"
finally:
    lcd.clear()
    GPIO.cleanup()
