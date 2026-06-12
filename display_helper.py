from time import sleep
import pytm1638

"""
This file exists to help the display by running a novel light sequence.

This file exists to help extend the display.py file.

"""
DIO = 10  # GPIO/BCM 10
CLK = 11  # GPIO/BCM 11
STB = 9  # GPIO/BCM 9

display = pytm1638.TM1638(DIO, CLK, STB)

display.enable(1)

def lightup(pos):
    display.set_led(pos - 1, 1)
    sleep(0.1)
    display.set_led(pos - 1, 0)
    return None

def led_sequence(lst, lvl):
    speed_level = [1.5, 1.5, 1.0, 1.0, 0.75, 0.75, 0.5, 0.5, 0.25, 0.25]

    for pos in lst:
        print(pos)
        display.set_led(pos - 1, 1)
        sleep(speed_level[lvl])
        display.set_led(pos - 1, 0)
        sleep(speed_level[lvl])
    
    return None

def display_rdy():
    display.send_char(0, 128)
    display.send_char(1, 128)
    display.send_char(2, 128)
    display.send_char(3, 128)
    display.send_char(4, 128)
    display.send_char(5, 128)
    display.send_char(6, 128)
    display.send_char(7, 128)
    return None

