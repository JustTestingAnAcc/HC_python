from tkinter import *

ABS_ZERO_FARENHIET = -459.67
ABS_ZERO_CELSIUS = -273.15

class TemperatureConverter:

    def calculate_to_c(self, temp):

        try:
            temp = float(temp)
            if temp >= ABS_ZERO_FARENHIET:
                result = (float(temp)-32) * 5 / 9
                return f'{result:.1f} degrees Centigrade'
            else:
                return "Temperature too low"
        except ValueError:
            return "Please enter a number"
        
    def calculate_to_f(self, temp):
        
        try:
            temp = float(temp)
            if temp >= ABS_ZERO_CELSIUS:
                result = (float(temp * 9 / 5) + 32)
                return f'{result:.1f} *F'
            return "Below Absolute Zero!"
        except ValueError:
            return "Enter a valid number"
        