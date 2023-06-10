import tkinter as tk
import customtkinter as ctk


def main():
    # Set the appearance of the GUI
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Create the GUI
    app = ctk.CTk()
    app.geometry('500x500')
    app.title('TaxIt')



    # Run the GUI
    app.mainloop()
