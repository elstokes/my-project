import RPi.GPIO as GPIO #We add the GPIO library to our script so we can use the pins on our RPi.
import time #Remember from our GoPiGo times, we need to use time.sleep() to control the flow of our code (so it isn't all executed at once!)

GPIO.setwarnings(False) #If RPi.GPIO detects that a pin has been configured to something other than the default (input), you get a warning when you try to configure a script; we don't want to be warned, we know what we are doing (hopefully)!

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT) #You need to set up every pin you are using as an input or an output; here we let the RPi know we will be using GPIO pin 18 as an output.


print "Welcome to morse code simulator 2018!"
print "Press:\n\tq:Send secret code\n\tw:On\n\ta:Off\n\tz:Exit"
while True:
    print "Enter the Command:",
    a=raw_input()   # Fetch the input from the terminal
    
    if a=='w':
       	    print "LED On"
       	    GPIO.output(18,GPIO.HIGH)
		
    elif a=='s': 
        print "LED Off"
        GPIO.output(18,GPIO.LOW)
		
    elif a=='q':

		print "." #.-.
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(0.25)

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.1)

		print "-" 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(0.75) 

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.1)

		print "." 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(.25)

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.5)

		print "." #.
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(.25)

		GPIO.output(18,GPIO.LOW)
		time.sleep(.5)

		print "-"#-.. 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(0.75)

		GPIO.output(18,GPIO.LOW)
		time.sleep(.1)

		print "." 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(.25)

		GPIO.output(18,GPIO.LOW)
		time.sleep(.1)

		print "." 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(.25)

		GPIO.output(18,GPIO.LOW)
		time.sleep(.5)

		print "." #.-.
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(0.25) 

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.1)

		print "-" 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(0.75) 

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.1)

		print "." 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(.25)

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.5)

		print "." #..-
		GPIO.output(18,GPIO.HIGH)
		time.sleep(.25)

		GPIO.output(18,GPIO.LOW)
		time.sleep(.1)

		print "." 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(0.25) 

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.1)

		print "-" 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(0.75)

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.5)

		print "-" #--
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(0.75) 

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.1)

		print "-" 
		GPIO.output(18,GPIO.HIGH) 
		time.sleep(0.75) 

		GPIO.output(18,GPIO.LOW)
		time.sleep(0.5)
		
		print "Dun"

    elif a=='z':
        print "Exiting"     # Exit
	sys.exit()
    else:
	print "Wrong Command, Please Enter Again"
	time.sleep(.1)
	GPIO.cleanup() #At the end of a program, it is good practice to clean up any resources you might have used; by returning all channels you have used back to inputs, you can avoid accidental damage to your RPi by shorting out the pins.