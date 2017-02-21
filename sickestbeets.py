import RPi.GPIO as GPIO #We add the GPIO library to our script so we can use the pins on our RPi.
import time #Remember from our GoPiGo times, we need to use time.sleep() to control the flow of our code (so it isn't all executed at once!)

GPIO.setmode(GPIO.BCM) #This means that you are referring to the pins by the numbers after "GPIO".
#The first answer here goes into more detail --> http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering

GPIO.setwarnings(False) #If RPi.GPIO detects that a pin has been configured to something other than the default (input), you get a warning when you try to configure a script; we don't want to be warned, we know what we are doing (hopefully)!

GPIO.setup(18,GPIO.OUT) #You need to set up every pin you are using as an input or an output; here we let the RPi know we will be using GPIO pin 18 as an output.

GPIO.setup(2,GPIO.OUT)

GPIO.setup(3,GPIO.OUT)

GPIO.setup(4,GPIO.OUT)

print "Welcome to sick beet simulator 2018!"
print "Press:\n\tq:Send secret code\n\tw:8th note\n\te:quarter note\n\tr:half note\n\t:whole note\n\tz:Exit"
while True:
    print "Enter the Command:",
    
       
   
    a=raw_input()   # Fetch the input from the terminal
    
    if a=='w':
       	    print "LEDs On"
       	    GPIO.output(18,GPIO.HIGH)  
       	    GPIO.output(4,GPIO.HIGH)
       	    GPIO.output(3,GPIO.HIGH)
       	    GPIO.output(2,GPIO.HIGH)

       	    print "Dun"
	
    elif a=='s': 
            print "LED Off"
            GPIO.output(18,GPIO.LOW)
            GPIO.output(4,GPIO.LOW)
       	    GPIO.output(3,GPIO.LOW)
       	    GPIO.output(2,GPIO.LOW)		
    
    elif a=='e':
            print "Half beat"
   	    GPIO.output(18,GPIO.HIGH)
       	    time.sleep(Whole/2)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(0.1)
   	    print "Dun"
    
    elif a=='r':
            print "Quarter beat"
   	    GPIO.output(18,GPIO.HIGH)
       	    time.sleep(Whole/4)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(0.1)
   	    print "Dun"
    
    elif a=='t':
            print "Eighth beat"
   	    GPIO.output(18,GPIO.HIGH)
       	    time.sleep(Whole/8)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(0.1)
   	    print "Dun"
   	    	
    elif a=='q':
            print "SEIZURE WARNING"
            print "1"
            GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(2,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(2,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(3,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(3,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(4,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(4,GPIO.LOW)
       	    time.sleep(.12)
       	    GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(4,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(4,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
       	    GPIO.output(3,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(3,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(2,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(2,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(2,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(2,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(3,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(3,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(4,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(4,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(4,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(4,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(3,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(3,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(4,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(4,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(18,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    print "1"
            GPIO.output(4,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(4,GPIO.LOW)
       	    time.sleep(.48)
       	    GPIO.output(3,GPIO.HIGH)
       	    time.sleep(.48)
       	    GPIO.output(3,GPIO.LOW)
       	    time.sleep(.48)
       	    
       	    GPIO.output(18,GPIO.HIGH)
       	    GPIO.output(4,GPIO.HIGH)
       	    GPIO.output(3,GPIO.HIGH)
       	    GPIO.output(2,GPIO.HIGH)
       	    
    
    elif a=='z':
        print "Exiting"     # Exit
	sys.exit()
    else:
	print "Wrong Command, Please Enter Again"
	time.sleep(.1)
	GPIO.cleanup() 
