from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# PIN-Assignment
A=18
B=23
C=24
D=25
time = 0.001
# defining the PINs
GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)
GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)
# driving the motor
def Step1():
GPIO.output(D, True)
sleep (time)
GPIO.output(D, False)
def Step2():
GPIO.output(D, True)
GPIO.output(C, True)
sleep (time)
GPIO.output(D, False)
GPIO.output(C, False)
def Step3():
GPIO.output(C, True)
sleep (time)
GPIO.output(C, False)
def Step4():
GPIO.output(B, True)
GPIO.output(C, True)
sleep (time)
GPIO.output(B, False)
GPIO.output(C, False)

def Step5():
GPIO.output(B, True)
sleep (time)
GPIO.output(B, False)
def Step6():
GPIO.output(A, True)
GPIO.output(B, True)
sleep (time)
GPIO.output(A, False)
GPIO.output(B, False)
def Step7():
GPIO.output(A, True)
sleep (time)
GPIO.output(A, False)
def Step8():
GPIO.output(D, True)
GPIO.output(A, True)
sleep (time)
GPIO.output(D, False)
GPIO.output(A, False)

# start one complete turn
for i in range (512):
Step1()
Step2()
Step3()
Step4()
Step5()
Step6()
Step7()
Step8()
GPIO.cleanup()