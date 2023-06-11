import tkinter as tk
import customtkinter as ctk
import os
from src.InputDialog import CTkInputDialog
from src.TopLevelDialog import TopLevelDialog


class GUI:
    app = ctk.CTk()

    brackets = {}
    targets = {}
    path = ''

    selected_bracket = None
    selected_target = None

    ranges_option_menu = None
    income_entry = None
    target_bracket_option_menu = None
    target_standard_deduction_entry = None
    target_donation_deduction_entry = None
    brackets_option_menu = None

    def __init__(self, brackets=None, targets=None, path=''):
        self.brackets = brackets
        self.targets = targets
        self.path = path
        if brackets is None:
            self.brackets = {}
        else:
            self.selected_bracket = list(self.brackets.keys())[0]
        if targets is None:
            self.targets = {}
        else:
            self.selected_target = list(self.targets.keys())[0]

        print(self.brackets)
        print(self.targets)
        print(self.path)

        self.main()

    def exit(self):
        self.app.quit()
        self.app.after(100, self.app.destroy)

    def new_bracket(self):
        # TODO: Replace when Cancel button is fixed
        dialog = CTkInputDialog(text="Bracket name:", title="New Bracket")
        # dialog = ctk.CTkInputDialog(text="Bracket name:", title="New Bracket")

        text = dialog.get_input()

        if text is not None and text != '':
            self.brackets[text] = []
            self.update_brackets('new')

    def delete_bracket(self):
        if self.selected_bracket is not None:
            del self.brackets[self.selected_bracket]
            self.update_brackets('delete')

    def update_brackets(self, flag):
        if flag == 'new':
            self.select_bracket(list(self.brackets.keys())[-1])
            self.brackets_option_menu.configure(
                values=list(self.brackets.keys()),
                variable=tk.StringVar(value=list(self.brackets.keys())[-1])
            )
        elif flag == 'delete':
            if len(self.brackets.keys()) > 0:
                self.select_bracket(list(self.brackets.keys())[0])
                self.brackets_option_menu.configure(
                    values=list(self.brackets.keys()),
                    variable=tk.StringVar(value=list(self.brackets.keys())[0])
                )
            else:
                self.select_bracket(None)
                self.brackets_option_menu.configure(
                    values=list(self.brackets.keys()),
                    variable=tk.StringVar(value='')
                )
        self.update_target_bracket()

    def new_target(self):
        pass

    def delete_target(self):
        pass

    def save(self):
        for bracket in self.brackets.keys():
            print(bracket, self.brackets[bracket])
        for target in self.targets.keys():
            print(target, self.targets[target])
        pass

    def compute(self):
        pass

    def new_range(self):
        if self.selected_bracket is not None:
            dialog = TopLevelDialog(text="Range value and rate:", title="New Range")

            text = dialog.get_input()

            if text is not None and text != '':
                text = text.split(' ')
                self.brackets[self.selected_bracket].append((float(text[0]), float(text[1])))
                self.update_ranges()

    def delete_range(self):
        if self.selected_bracket is not None:
            # delete the selected range in ranges_option_menu
            selected_range = self.ranges_option_menu.get()
            selected_range = selected_range.split('->')
            selected_range = (float(selected_range[0]), float(selected_range[1]))
            self.brackets[self.selected_bracket].remove(selected_range)
            self.update_ranges()

    def select_bracket(self, bracket):
        self.selected_bracket = bracket
        self.update_ranges()
        self.brackets_option_menu.configure(
            variable=tk.StringVar(value=bracket)
        )

    def select_target(self, target):
        self.selected_target = target
        self.update_income()
        self.update_target_bracket()
        self.update_standard_deduction()
        self.update_donation_deduction()

    def update_ranges(self):
        if self.selected_bracket is not None:
            if len(self.brackets[self.selected_bracket]) > 0:
                self.ranges_option_menu.configure(
                    values=[str(i[0]) + ' -> ' + str(i[1]) for i in self.brackets[self.selected_bracket]],
                    variable=tk.StringVar(value=str(list(self.brackets[self.selected_bracket])[0][0]) + '->' + str(
                        list(self.brackets[self.selected_bracket])[0][1]))
                )
            else:
                self.ranges_option_menu.configure(
                    values=[],
                    variable=tk.StringVar(value='')
                )
        else:
            self.ranges_option_menu.configure(
                values=[],
                variable=tk.StringVar(value='')
            )

    def update_income(self):
        if self.selected_target is not None:
            self.income_entry.configure(
                textvariable=tk.StringVar(value=self.targets[self.selected_target]['income'])
            )
        else:
            self.income_entry.configure(
                textvariable=tk.StringVar(value='0.00')
            )

    def update_target_bracket(self):
        if self.selected_target is not None:
            self.target_bracket_option_menu.configure(
                variable=tk.StringVar(value=self.targets[self.selected_target]['bracket'])
            )
        else:
            self.target_bracket_option_menu.configure(
                variable=tk.StringVar(value='')
            )

        self.target_bracket_option_menu.configure(
            values=list(self.brackets.keys())
        )

    def update_standard_deduction(self):
        if self.selected_target is not None:
            self.target_standard_deduction_entry.configure(
                textvariable=tk.StringVar(value=self.targets[self.selected_target]['standard_deduction'])
            )
        else:
            self.target_standard_deduction_entry.configure(
                textvariable=tk.StringVar(value='0.00')
            )

    def update_donation_deduction(self):
        if self.selected_target is not None:
            self.target_donation_deduction_entry.configure(
                textvariable=tk.StringVar(value=self.targets[self.selected_target]['donation_deduction'])
            )
        else:
            self.target_donation_deduction_entry.configure(
                textvariable=tk.StringVar(value='0.00')
            )

    def main(self):
        # Appearance settings
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.app.title('TaxIt')
        self.app.protocol("WM_DELETE_WINDOW", self.exit)
        self.app.resizable(False, False)

        # Brackets frame
        brackets_frame = ctk.CTkFrame(
            self.app
        )
        brackets_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky='nsew')

        # Brackets list
        self.brackets_option_menu = ctk.CTkOptionMenu(
            brackets_frame,
            values=list(self.brackets.keys()),
            variable=tk.StringVar(value=self.selected_bracket),
            font=('Arial', 20),
            command=self.select_bracket
        )
        self.brackets_option_menu.pack(padx=12, pady=10)

        # Ranges list
        self.ranges_option_menu = ctk.CTkOptionMenu(
            brackets_frame,
            values=[],
            variable=tk.StringVar(value=''),
            font=('Arial', 20),
        )
        self.ranges_option_menu.pack(padx=12, pady=10)
        self.update_ranges()

        # New range button
        new_range_button = ctk.CTkButton(
            brackets_frame,
            text='New Range',
            font=('Arial', 20),
            command=self.new_range
        )
        new_range_button.pack(padx=12, pady=10)

        # Delete range button
        delete_range_button = ctk.CTkButton(
            brackets_frame,
            text='Delete Range',
            font=('Arial', 20),
            command=self.delete_range
        )
        delete_range_button.pack(padx=12, pady=10)

        # New bracket button
        new_bracket_button = ctk.CTkButton(
            brackets_frame,
            text='New Bracket',
            font=('Arial', 20),
            command=self.new_bracket
        )
        new_bracket_button.pack(padx=12, pady=10, side=tk.BOTTOM)

        # Delete bracket button
        delete_bracket_button = ctk.CTkButton(
            brackets_frame,
            text='Delete Bracket',
            font=('Arial', 20),
            command=self.delete_bracket
        )
        delete_bracket_button.pack(padx=12, pady=10, side=tk.BOTTOM)

        # Targets frame
        targets_frame = ctk.CTkFrame(
            self.app
        )
        targets_frame.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

        # Targets list
        targets_option_menu = ctk.CTkOptionMenu(
            targets_frame,
            values=list(self.targets.keys()),
            variable=tk.StringVar(value=self.selected_target),
            font=('Arial', 20),
            command=self.select_target
        )
        targets_option_menu.pack(padx=12, pady=10)

        # Target frame
        target_frame = ctk.CTkFrame(
            targets_frame
        )
        target_frame.pack(padx=12, pady=10)

        # TODO:Target info
        self.income_entry = ctk.CTkEntry(
            target_frame,
            textvariable=tk.StringVar(value='0.00'),
            font=('Arial', 20),
            placeholder_text='Income'
        )
        self.income_entry.pack(padx=12, pady=10)
        self.update_income()

        self.target_bracket_option_menu = ctk.CTkOptionMenu(
            target_frame,
            values=list(self.brackets.keys()),
            variable=tk.StringVar(value=''),
            font=('Arial', 20),
        )
        self.target_bracket_option_menu.pack(padx=12, pady=10)
        self.update_target_bracket()

        self.target_standard_deduction_entry = ctk.CTkEntry(
            target_frame,
            textvariable=tk.StringVar(value='0.00'),
            font=('Arial', 20),
            placeholder_text='Standard Deduction'
        )
        self.target_standard_deduction_entry.pack(padx=12, pady=10)
        self.update_standard_deduction()

        self.target_donation_deduction_entry = ctk.CTkEntry(
            target_frame,
            textvariable=tk.StringVar(value='0.00'),
            font=('Arial', 20),
            placeholder_text='Donation Deduction'
        )
        self.target_donation_deduction_entry.pack(padx=12, pady=10)
        self.update_donation_deduction()

        # New target button
        new_target_button = ctk.CTkButton(
            targets_frame,
            text='New Target',
            font=('Arial', 20),
            command=self.new_target
        )
        new_target_button.pack(padx=12, pady=10, side=tk.BOTTOM)

        # Delete target button
        delete_target_button = ctk.CTkButton(
            targets_frame,
            text='Delete Target',
            font=('Arial', 20),
            command=self.delete_target
        )
        delete_target_button.pack(padx=12, pady=10, side=tk.BOTTOM)

        # Save button frame
        save_button_frame = ctk.CTkFrame(
            self.app
        )
        save_button_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky='nsew')

        # Save button
        save_button = ctk.CTkButton(
            save_button_frame,
            text='Save',
            font=('Arial', 20),
            command=self.save
        )
        save_button.pack(padx=12, pady=10)

        # Compute button frame
        compute_button_frame = ctk.CTkFrame(
            self.app
        )
        compute_button_frame.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

        # Compute button
        compute_button = ctk.CTkButton(
            compute_button_frame,
            text='Compute',
            font=('Arial', 20),
            command=self.compute
        )
        compute_button.pack(padx=12, pady=10)

        # Run app
        self.app.mainloop()
