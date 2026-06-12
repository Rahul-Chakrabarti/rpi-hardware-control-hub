# Written by Rahul Chakrabarti
import button_helper
import display_helper
from time import sleep

"""
A Calculator PoC application, running on the
TM!638 Integrated Circuit button and display chip.

Can perform simple addition, for numbers outside
of the direct scope, a sum is required to input them on either
side of the operand.
"""
DIO = 10
CLK = 11
STB = 9

# Global variables to store inputs and state
operand1 = None
operand2 = None
operator = None
current_input = ""

def handle_buttons(button_num):
    # Helps handle button presses before handoff
    global operand1, operand2, operator, current_input
    if 1 <= button_num <= 6:  # Numbers 1-6
        current_input += str(button_num)
        display_helper.display_button(int(current_input))  # Display the current input
    elif button_num == 7:  # Addition
        if current_input:
            operand1 = int(current_input)
            operator = "+"
            current_input = ""  # Clear current input for the next operand
            display_helper.display_button(0)  # Clear the display
    elif button_num == 8:  # Equals
        if operand1 is not None and current_input:
            operand2 = int(current_input)
            result = operand1 + operand2  # Perform addition
            display_helper.display_button(result)  # Display the result
            reset_calculator()  # Reset for a new calculation
    sleep(0.2)

def reset_calculator():
    # Resets calculator to do another calculation if wanted
    global operand1, operand2, operator, current_input
    operand1 = None
    operand2 = None
    operator = None
    current_input = ""

def main():
    print("TM1638 Addition Calculator")
    print("Press buttons 1-6 for numbers, 7 for '+', 8 for '='.")
    try:
        while True:
            buttons = button_helper.TM1638_Button(DIO, CLK, STB)
            print("Waiting for button press...")
            buttons.wait_for_input(handle_buttons)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

