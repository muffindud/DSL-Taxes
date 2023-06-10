import tkinter as tk
import customtkinter as ctk
from src.InputDialog import CTkInputDialog
import os
import time
from src import GUI
from src import analyzer


class Menu:
    app = ctk.CTk()
    selected_file = 'New File'

    def __init__(self):
        self.main()

    def exit(self):
        self.app.quit()
        self.app.destroy()

    def new_file(self):
        # TODO: Replace when Cancel button is fixed
        dialog = CTkInputDialog(text="File name:", title="New File")
        # dialog = ctk.CTkInputDialog(text="File name:", title="New File")

        text = dialog.get_input()

        if text is None:
            pass
        elif text == '':
            # self.app.quit()
            self.exit()
            GUI.GUI(path=time.strftime("%Y%m%d-%H%M%S") + '.txit')
        else:
            # self.app.quit()
            self.exit()
            GUI.GUI(path=text)

    def open_file(self):
        if self.selected_file == 'New File':
            self.new_file()
        else:
            # self.app.quit()
            self.exit()
            analyzer.main(self.selected_file, 'gui')

    def select_option(self, option):
        self.selected_file = option

    def main(self):
        # Appearance settings
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.app.title('TaxIt Menu')
        self.app.protocol("WM_DELETE_WINDOW", self.exit)
        self.app.geometry('300x100')

        file_list = ['New File']
        for file in os.listdir("saves/"):
            if file.endswith(".txit"):
                file_list.append(file)

        option_menu = ctk.CTkOptionMenu(self.app, values=file_list, command=self.select_option, font=('Arial', 20))
        option_menu.pack(padx=12, pady=10)

        confirm_button = ctk.CTkButton(self.app, text='Confirm', command=self.open_file, font=('Arial', 20))
        confirm_button.pack(padx=12, pady=10)

        # Run app
        self.app.mainloop()
