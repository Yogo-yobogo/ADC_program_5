import RPi.GPIO as GPIO
import time 

def dec_to_bin(number):
    return [int(element) for element in  bin(number)[2:].zfill(8)]

def adc():
        step = 128
        value = 0
        i = 0
        while i != 8:
            value += int(step)
            bin_num = dec_to_bin(value)
            GPIO.output (dac, bin_num)
            time.sleep(0.01)
            comparator_value = GPIO.input(comp)
            if comparator_value == 1:
                value -= int(step)
            step /= 2
            i += 1
        print ('return value = ', value)
        return value

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup (dac, GPIO.OUT)
comp = 14
troyka = 13
GPIO.setup (troyka, GPIO.OUT)
GPIO.setup (comp, GPIO.IN)
GPIO.output (troyka, 1)

number_of_values = 255
max_voltage = 3.3
try:
    while (True):
        value = adc()
        voltage = value / number_of_values * max_voltage
        print ('value = ',value , 'input voltage = ', voltage)
        #time.sleep(5)
except ArithmeticError:
    print ("program cancle\n")
finally :
    GPIO.output(dac, 0)
    GPIO.cleanup()
GPIO.output(dac, 0)
GPIO.cleanup()