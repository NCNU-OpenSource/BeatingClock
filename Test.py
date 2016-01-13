import RPi.GPIO as GPIO
import time
# Adafruit_CharLCD
from Adafruit_CharLCD import Adafruit_CharLCD
#random music
import random
import pygame
music_list=["/home/pi/music/bb.mp3","/home/pi/music/test.mp3","/home/pi/music/ttt.mp3"]
pygame.mixer.init()
# setting
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(10,GPIO.OUT)
lcd = Adafruit_CharLCD()
lcd.clear()
# print setting time
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
def Alarmprint():
    lcd.clear()
    lcd.home()
    lcd.message("    Beating\n")
    lcd.message("     Alarm")
#enter(button)
#up(button)
#down
#setting time
def ok():
    lcd.clear()
    lcd.home()
    lcd.message("       OK")
def start():
    lcd.clear()
    lcd.home()
    lcd.message("     start")
RUNNING = True
try:
    while True:
        Alarmprint()
        time.sleep(1)
        first = 0
        second = 0
        third = 0
        forth = 0
        enter = GPIO.input(8)
        if enter == False:
            time.sleep(2)
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
            ok()
            time.sleep(2)
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
            ok()
            time.sleep(2) 
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
            ok()
            time.sleep(2)
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
            ok()
            time.sleep(2)
            enter = True
            while enter:
                myprint(first,second,third,forth)
                enter = GPIO.input(8)
                if enter == False:
                    break
                time.sleep(0.5)
            start()
            time.sleep(2)
            h = first * 10 + second
            m = third * 10 + forth
            s = 0
            while RUNNING:
                time.sleep(1)
                lcd.clear()
                lcd.home()
                lcd.message("   Count down\n")
                lcd.message("     ")
                lcd.message(str(h))
                lcd.message(":")
                lcd.message(str(m))
                lcd.message(":")
                lcd.message(str(s))
                if h == 0 and m == 0 and s == 0:
                    lcd.clear()
                    lcd.home()
                    lcd.message("    Wake Up!")
                    time.sleep(3)
                    music=random.choice(music_list)
                    pygame.mixer.music.load(music)
                    pygame.mixer.music.play()
                    break
                if s == 0:
                    if m == 0:
                        if h == 0:
                            m = 0
                        else:
                            h = h - 1
                            m = 59
                    else:
                        m = m - 1
                    s = 59
                else:
                    s = s - 1
            p = GPIO.PWM(10,50)
            p.start(4.5)
            inputValue = True
            while inputValue == True:
                p.ChangeDutyCycle(10.5)
                time.sleep(0.5)
                p.ChangeDutyCycle(4.5)
                time.sleep(0.5)
                inputValue = GPIO.input(8)
                if inputValue == False:
                    break
            p.stop()
            pygame.mixer.music.stop()
            print("end")
            time.sleep(5)
except KeyboardInterrupt:
    RUNNING = False
    print "\nQuitting"
finally:
    lcd.clear()
    GPIO.cleanup()
