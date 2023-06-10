import tkinter as tk
import customtkinter as ctk
import os


class GUI:
    app = ctk.CTk()
    brackets = {}
    targets = {}
    path = ''
    window_width = 800
    window_height = 600

    def __init__(self, brackets=None, targets=None, path=''):
        self.brackets = brackets
        self.targets = targets
        self.path = path
        if brackets is None:
            self.brackets = {}
        if targets is None:
            self.targets = {}

        print(self.brackets)
        print(self.targets)
        print(self.path)

        self.main()

    def exit(self):
        self.app.quit()
        self.app.destroy()

    def new_bracket(self):
        pass

    def delete_bracket(self):
        pass

    def new_target(self):
        pass

    def delete_target(self):
        pass

    def save(self):
        pass

    def compute(self):
        pass

    def main(self):
        # Appearance settings
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.app.title('TaxIt')
        self.app.protocol("WM_DELETE_WINDOW", self.exit)
        self.app.resizable(False, False)

        # Brackets frame
        brackets_frame = ctk.CTkFrame(self.app)
        brackets_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky='nsew')

        # Brackets list
        brackets_option_menu = ctk.CTkOptionMenu(brackets_frame, values=list(self.brackets.keys()), variable=tk.StringVar(), font=('Arial', 20))
        brackets_option_menu.pack(padx=12, pady=10)

        # New bracket button
        new_bracket_button = ctk.CTkButton(brackets_frame, text='New Bracket', font=('Arial', 20), command=self.new_bracket)
        new_bracket_button.pack(padx=12, pady=10)

        # Delete bracket button
        delete_bracket_button = ctk.CTkButton(brackets_frame, text='Delete Bracket', font=('Arial', 20), command=self.delete_bracket)
        delete_bracket_button.pack(padx=12, pady=10)

        # Targets frame
        targets_frame = ctk.CTkFrame(self.app)
        targets_frame.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

        # Targets list
        targets_option_menu = ctk.CTkOptionMenu(targets_frame, values=list(self.targets.keys()), variable=tk.StringVar(), font=('Arial', 20))
        targets_option_menu.pack(padx=12, pady=10)

        # New target button
        new_target_button = ctk.CTkButton(targets_frame, text='New Target', font=('Arial', 20), command=self.new_target)
        new_target_button.pack(padx=12, pady=10)

        # Delete target button
        delete_target_button = ctk.CTkButton(targets_frame, text='Delete Target', font=('Arial', 20), command=self.delete_target)
        delete_target_button.pack(padx=12, pady=10)

        # Save button frame
        save_button_frame = ctk.CTkFrame(self.app)
        save_button_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky='nsew')

        # Save button
        save_button = ctk.CTkButton(save_button_frame, text='Save', font=('Arial', 20), command=self.save)
        save_button.pack(padx=12, pady=10)

        # Compute button frame
        compute_button_frame = ctk.CTkFrame(self.app)
        compute_button_frame.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

        # Compute button
        compute_button = ctk.CTkButton(compute_button_frame, text='Compute', font=('Arial', 20), command=self.compute)
        compute_button.pack(padx=12, pady=10)

        # Run app
        self.app.mainloop()
