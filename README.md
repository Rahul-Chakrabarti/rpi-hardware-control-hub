# Raspberry Pi Hardware Control Hub

A multi peripheral hardware control system built on a Raspberry Pi, integrating an ultrasonic distance sensor, a stepper motor, and an integrated circuit handling button input and a 7 segment display. All hardware facing functionality, including GPIO control, SPI communication, and PWM signaling, was implemented from scratch in Python, with helper functions abstracting common setup and control logic away from the higher level program code.

The Pi was accessed from a host machine through a UART serial console using PuTTY, with Linux shell scripting used to run and test programs directly on the device.

## Overview

This project explores coordinating multiple independent hardware components through a single Raspberry Pi controller. Each peripheral is supported by its own set of function(s), which if applicable are then combined into standalone programs demonstrating practical use cases, notably including an arithmetic addition PoC calculator built using a IC's buttons and display.

## Hardware Components

In this project, three main peripherals are connected and defined for operation.
- The ultrasonic distance sensor (HCSR04) performs distance measurement using PWM based echo timing. 
- The stepper motor (28BYJ-48)is controlled through GPIO step and direction signaling. 
- The integrated circuit (TM1638) communicates over SPI, with its buttons used for digit and operator input and its 7 segment display used for real time output. The lights from the display are driven through the same IC, serving as a status indicator.

## Software Requirements

This project requires Python 3 along with the RPi.GPIO library to run the software.
For connection to a PC, PuTTY is an open source software that was used for connection to the Pi, via a USB TTL serial cable.

## Hardware Requirements

The following is a non-exhaustive list of what hardware was required to create a function hardware hub.

- A raspberry Pi microcomputer. The exact Pi model used for this project was a Raspberry Pi Zero W.
- A microSD card for the raspberry Pi.
- A breadboard
- Resistors
- Wires (pins), predominately using Male - Female wires, though a combination of Male - Male, Female - Female and Male - Female should do the trick for an inquistive assembler.
- USB TTL serial cable for SPI connection via PuTTY to a PC
- A operational PC with atleast 1 USB port open for connection.
- The HCSR04 ultrasonic distance sensor / rangefinder.
- The TM1638 integrated circuit controller chip.
- The 28BYJ-48 stepper motor.
- A flash drive to store Python programs and the Linux operating system.
- A USB drive hub connected via micro USB to the Pi.
- A waveform generator and/or a oscilloscope to view the echo and trigger pulse from the ultrasonic distance sensor.
- A digital multimeter capable of reading DC voltage, DC current and subsequently resistance to ensure proper wiring and smooth operation of the electronics before power turns on.


## Project Highlights

All GPIO, SPI, and PWM hardware interfacing functions were written from scratch, without relying on high level abstraction libraries beyond RPi.GPIO. Helper functions remove repetitive setup and cleanup logic for further expansion later, allowing the program level code to focus on application behavior. The project culminates with a hub capable of multiple functions, including a working proof of concept calculator that uses physical button input and displays results in real time using the 7 segment display.

## License

No license chosen as of now