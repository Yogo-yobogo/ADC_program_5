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

led = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup (led, GPIO.OUT)

num_list = [32, 64, 96, 128, 160, 192, 224, 250]
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
        num = 0
        for i in num_list:
            if i > value:
                num = i
                break
        if num == 250 or value > 224:
            bin_num = dec_to_bin(255)
        elif value <= 10:
            bin_num = dec_to_bin(0)
        else:
            bin_num = dec_to_bin(2**int(num/32)-1)
        print ('bin_num =', bin_num, 'num = ', num)
        GPIO.output (led, bin_num)
except ArithmeticError:
    print ("program cancle\n")
finally :
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.cleanup()