import RPi.GPIO as GPIO
import time
# Adafruit_CharLCD
from Adafruit_CharLCD import Adafruit_CharLCD
# python
import pygame
pygame.mixer.init()
pygame.mixer.music.load("ring.mp3")
# setting
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.OUT)
lcd = Adafruit_CharLCD()
lcd.clear()
RUNNING = True
try:
    while True:
        inputValue = GPIO.input(8)
        if inputValue == False:
            h = 0
            m = 0
            s = 5
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
                    pygame.mixer.music.play()
                    time.sleep(3)
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
            print("pressed")
            time.sleep(5)
except KeyboardInterrupt:
    RUNNING = False
    print "\nQuitting"
finally:
    lcd.clear()
    GPIO.cleanup()
