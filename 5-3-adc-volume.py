import RPi.GPIO as GPIO
import time 

def dec_to_bin(number):
    return [int(element) for element in  bin(number)[2:].zfill(8)]

def adc():
    for value in range (0, 256):
        bin_num = dec_to_bin(value)
        GPIO.output (dac, bin_num)
        time.sleep(0.001)
        comparator_value = GPIO.input(comp)
        if comparator_value == 1 :
            break
    print ('return value = ', value)
    return int(value)

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup (dac, GPIO.OUT)

led = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup (led, GPIO.OUT)

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
        voltage = value / 256 * 3.3
        print ('value = ',value , 'input voltage = ', voltage)
        bin_num = dec_to_bin(value)
        GPIO.output (led, bin_num)
except ArithmeticError:
    print ("program cancle\n")
finally :
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.cleanup()