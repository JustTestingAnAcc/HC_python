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
        

#================================================================#
#                                GUI                             #
#================================================================#

class ConverterGUI:
    def __init__(self, root):
        #window 
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("500x350")

        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.frames = {}

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()

        self.show_frame("MainFrame")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    # def create_main_frame():


