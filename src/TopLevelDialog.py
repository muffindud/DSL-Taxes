from typing import Union, Tuple, Optional

from customtkinter.windows.widgets import CTkLabel
from customtkinter.windows.widgets import CTkEntry
from customtkinter.windows.widgets import CTkButton
from customtkinter.windows.widgets.theme import ThemeManager
from customtkinter.windows.ctk_toplevel import CTkToplevel
import tkinter as tk


class TopLevelDialog(CTkToplevel):
    """
    Dialog with extra window, message, entry widget, cancel and ok button.
    For detailed information check out the documentation.
    """

    def __init__(self,
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 text_color: Optional[Union[str, Tuple[str, str]]] = None,
                 button_fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 button_hover_color: Optional[Union[str, Tuple[str, str]]] = None,
                 button_text_color: Optional[Union[str, Tuple[str, str]]] = None,
                 entry_fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 entry_border_color: Optional[Union[str, Tuple[str, str]]] = None,
                 entry_text_color: Optional[Union[str, Tuple[str, str]]] = None,

                 title: str = "CTkDialog",
                 text: str = "CTkDialog"):
        super().__init__(fg_color=fg_color)

        self._fg_color = ThemeManager.theme["CTkToplevel"]["fg_color"] if fg_color is None else self._check_color_type(
            fg_color)
        self._text_color = ThemeManager.theme["CTkLabel"][
            "text_color"] if text_color is None else self._check_color_type(button_hover_color)
        self._button_fg_color = ThemeManager.theme["CTkButton"][
            "fg_color"] if button_fg_color is None else self._check_color_type(button_fg_color)
        self._button_hover_color = ThemeManager.theme["CTkButton"][
            "hover_color"] if button_hover_color is None else self._check_color_type(button_hover_color)
        self._button_text_color = ThemeManager.theme["CTkButton"][
            "text_color"] if button_text_color is None else self._check_color_type(button_text_color)
        self._entry_fg_color = ThemeManager.theme["CTkEntry"][
            "fg_color"] if entry_fg_color is None else self._check_color_type(entry_fg_color)
        self._entry_border_color = ThemeManager.theme["CTkEntry"][
            "border_color"] if entry_border_color is None else self._check_color_type(entry_border_color)
        self._entry_text_color = ThemeManager.theme["CTkEntry"][
            "text_color"] if entry_text_color is None else self._check_color_type(entry_text_color)

        self._user_input: Union[str, None] = None
        self._running: bool = False
        self._text = text

        self.title(title)
        self.lift()  # lift window on top
        self.attributes("-topmost", True)  # stay on top
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.after(10,
                   self._create_widgets)  # create widgets with slight delay, to avoid white flickering of background
        self.resizable(False, False)
        self.grab_set()  # make other windows not clickable

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self._label = CTkLabel(master=self,
                               width=300,
                               wraplength=300,
                               fg_color="transparent",
                               text_color=self._text_color,
                               text=self._text, )
        self._label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        self._entry1 = CTkEntry(master=self,
                                width=110,
                                fg_color=self._entry_fg_color,
                                border_color=self._entry_border_color,
                                text_color=self._entry_text_color,
                                placeholder_text="Income",
                                textvariable=tk.StringVar(value="0.0"))
        self._entry1.grid(row=1, column=0, columnspan=1, padx=(20, 10), pady=(0, 20), sticky="ew")

        self._entry2 = CTkEntry(master=self,
                                width=110,
                                fg_color=self._entry_fg_color,
                                border_color=self._entry_border_color,
                                text_color=self._entry_text_color,
                                placeholder_text="Rate",
                                textvariable=tk.StringVar(value="0.0"))
        self._entry2.grid(row=1, column=1, columnspan=1, padx=(10, 20), pady=(0, 20), sticky="ew")

        self._ok_button = CTkButton(master=self,
                                    width=100,
                                    border_width=0,
                                    fg_color=self._button_fg_color,
                                    hover_color=self._button_hover_color,
                                    text_color=self._button_text_color,
                                    text='Ok',
                                    command=self._ok_event)
        self._ok_button.grid(row=2, column=0, columnspan=1, padx=(20, 10), pady=(0, 20), sticky="ew")

        self._cancel_button = CTkButton(master=self,
                                        width=100,
                                        border_width=0,
                                        fg_color=self._button_fg_color,
                                        hover_color=self._button_hover_color,
                                        text_color=self._button_text_color,
                                        text='Cancel',
                                        command=self._cancel_event)
        self._cancel_button.grid(row=2, column=1, columnspan=1, padx=(10, 20), pady=(0, 20), sticky="ew")

        self.after(150, lambda: self._entry1.focus())  # set focus to entry with slight delay, otherwise it won't work
        self._entry1.bind("<Return>", self._ok_event)
        self._entry2.bind("<Return>", self._ok_event)

    def _ok_event(self, event=None):
        try:
            float(self._entry1.get())
            float(self._entry2.get())
            self._user_input = self._entry1.get() + ' ' + self._entry2.get()
            self.grab_release()
            self.destroy()
        except ValueError:
            self._label.configure(text="Please enter a valid number!", text_color="red")

            try:
                float(self._entry1.get())
            except ValueError:
                self._entry1.configure(
                    fg_color="red",
                )

            try:
                float(self._entry2.get())
            except ValueError:
                self._entry2.configure(
                    fg_color="red",
                )

    def _on_closing(self):
        self.grab_release()
        self.destroy()

    def _cancel_event(self):
        self.grab_release()
        self.destroy()

    def get_input(self):
        self.master.wait_window(self)
        return self._user_input
