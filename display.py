import button_helper
import display_helper
from time import sleep

"""
This file handles the 7-segment display that exist on the TM1638 IC.

This file exists to extend the PYTM1638 file.

"""

DIO = 10
CLK = 11
STB = 9

def handle_buttons(button_num):
    # Handles button presses: lights up the LED corresponding to the button 
    # and displays the button number on the 7-segment display.
    display_helper.lightup(button_num)
    display_helper.display_button(button_num)
    sleep(0.2)
    return None

def main():
    print("TM-1638 Button and Display Program")
    print("Press a button to light it up and display its number.")
    try:
        while True:
            buttons = button_helper.TM1638_Button(DIO, CLK, STB)
            print("Waiting for button press...")
            buttons.wait_for_input(handle_buttons)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
