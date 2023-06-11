import tkinter as tk
import customtkinter as ctk
from src.InputDialog import CTkInputDialog
from src.TopLevelDialog import TopLevelDialog
from src import calculator
from src import convertor


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
    targets_option_menu = None
    results_window = None

    def __init__(self, brackets=None, targets=None, path=''):
        self.brackets = brackets
        self.targets = targets
        self.path = path
        if brackets is None or len(brackets.keys()) == 0:
            self.brackets = {}
        else:
            self.selected_bracket = list(self.brackets.keys())[0]
        if targets is None or len(targets.keys()) == 0:
            self.targets = {}
        else:
            self.selected_target = list(self.targets.keys())[0]

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
        # TODO: Replace when Cancel button is fixed
        dialog = CTkInputDialog(text="Target name:", title="New Target")
        # dialog = ctk.CTkInputDialog(text="Target name:", title="New Target")

        text = dialog.get_input()

        if text is not None and text != '':
            self.targets[text] = {'income': 0, 'bracket': None, 'standard_deduction': 0, 'donation_deduction': 0, 'tax': 0}
            self.update_targets('new')

    def delete_target(self):
        if self.selected_target is not None:
            del self.targets[self.selected_target]
            self.update_targets('delete')

    def update_targets(self, flag):
        if flag == 'new':
            self.select_target(list(self.targets.keys())[-1])
            self.targets_option_menu.configure(
                values=list(self.targets.keys()),
                variable=tk.StringVar(value=list(self.targets.keys())[-1])
            )
        elif flag == 'delete':
            if len(self.targets.keys()) > 0:
                self.select_target(list(self.targets.keys())[0])
                self.targets_option_menu.configure(
                    values=list(self.targets.keys()),
                    variable=tk.StringVar(value=list(self.targets.keys())[0])
                )
            else:
                self.select_target(None)
                self.targets_option_menu.configure(
                    values=[],
                    variable=tk.StringVar(value='')
                )
        self.update_income()
        self.update_target_bracket()
        self.update_standard_deduction()
        self.update_donation_deduction()

    # TODO: Finish this function
    def save(self):
        content = convertor.main(self.brackets, self.targets)
        try:
            file = open("saves/" + self.path, 'x')
        except FileExistsError:
            file = open("saves/" + self.path, 'w')
        file.write(content)

    def compute(self):
        print(self.targets)
        print(self.brackets)
        self.targets = calculator.main(self.brackets, self.targets, 'gui')

        if self.results_window is None or not self.results_window.winfo_exists():
            self.results_window = ctk.CTkToplevel(self.app)

        self.app.after(100, self.results_window.focus)
        self.results_window.title('Results')
        self.results_window.resizable(False, False)

        targets = []
        results = []
        for target in self.targets.keys():
            targets.append(
                ctk.CTkLabel(
                    self.results_window,
                    text=target + ' :   ',
                    width=20,
                    anchor=tk.W,
                    font=('Arial', 24)
                )
            )
            results.append(
                ctk.CTkLabel(
                    self.results_window,
                    text=str(self.targets[target]['tax']),
                    width=20,
                    anchor=tk.E,
                    font=('Arial', 24)
                )
            )
            targets[-1].grid(row=len(targets), column=0, sticky=tk.W)
            results[-1].grid(row=len(results), column=1, sticky=tk.E)

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
        if target is not None and target != '':
            self.update_income()
            self.update_target_bracket()
            self.update_standard_deduction()
            self.update_donation_deduction()
            self.targets_option_menu.configure(
                variable=tk.StringVar(value=target)
            )
            self.income_entry.configure(
                state=tk.NORMAL
            )
            self.target_bracket_option_menu.configure(
                state=tk.NORMAL
            )
            self.target_standard_deduction_entry.configure(
                state=tk.NORMAL
            )
            self.target_donation_deduction_entry.configure(
                state=tk.NORMAL
            )
        else:
            self.income_entry.configure(
                state=tk.DISABLED
            )
            self.target_bracket_option_menu.configure(
                state=tk.DISABLED
            )
            self.target_standard_deduction_entry.configure(
                state=tk.DISABLED
            )
            self.target_donation_deduction_entry.configure(
                state=tk.DISABLED
            )
            self.targets_option_menu.configure(
                variable=tk.StringVar(value='')
            )
        self.confirm_target()

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

    def confirm_target(self):
        if self.selected_target is not None:
            self.targets[self.selected_target]['income'] = float(self.income_entry.get())
            self.targets[self.selected_target]['bracket'] = self.target_bracket_option_menu.get()
            self.targets[self.selected_target]['standard_deduction'] = float(self.target_standard_deduction_entry.get())
            self.targets[self.selected_target]['donation_deduction'] = float(self.target_donation_deduction_entry.get())
            self.update_target_bracket()
            self.update_standard_deduction()
            self.update_donation_deduction()
            self.update_income()
            self.update_ranges()
        else:
            self.targets_option_menu.configure(
                variable=tk.StringVar(value='')
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
        self.targets_option_menu = ctk.CTkOptionMenu(
            targets_frame,
            values=list(self.targets.keys()),
            variable=tk.StringVar(value=self.selected_target),
            font=('Arial', 20),
            command=self.select_target
        )
        self.targets_option_menu.pack(padx=12, pady=10)

        # Target frame
        target_frame = ctk.CTkFrame(
            targets_frame
        )
        target_frame.pack(padx=12, pady=10)

        self.income_entry = ctk.CTkEntry(
            target_frame,
            textvariable=tk.StringVar(value='0.00'),
            font=('Arial', 20),
            placeholder_text='Income',
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
            placeholder_text='Standard Deduction',
        )
        self.target_standard_deduction_entry.pack(padx=12, pady=10)
        self.update_standard_deduction()

        self.target_donation_deduction_entry = ctk.CTkEntry(
            target_frame,
            textvariable=tk.StringVar(value='0.00'),
            font=('Arial', 20),
            placeholder_text='Donation Deduction',
        )
        self.target_donation_deduction_entry.pack(padx=12, pady=10)
        self.update_donation_deduction()

        confirm_target_button = ctk.CTkButton(
            target_frame,
            text='Confirm',
            font=('Arial', 20),
            command=self.confirm_target
        )
        confirm_target_button.pack(padx=12, pady=10)

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
