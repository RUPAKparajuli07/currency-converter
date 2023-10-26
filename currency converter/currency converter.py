import tkinter as tk
import requests

class App:
    def __init__(self, url): 
        self.window = tk.Tk()
        self.window.title("Currency Converter")
        self.from_currency = tk.StringVar(self.window)
        self.to_currency = tk.StringVar(self.window)
        self.amount = tk.StringVar(self.window)
        self.converted_amount = tk.StringVar(self.window)
        self.url = url

        self.from_currency_label = tk.Label(self.window, text="From Currency")
        self.from_currency_label.grid(column=0, row=0, padx=5, pady=5)
        self.from_currency_options = sorted(self.get_currency_options())
        self.from_currency_dropdown = tk.OptionMenu(self.window, self.from_currency, *self.from_currency_options)
        self.from_currency_dropdown.grid(column=1, row=0, padx=5, pady=5)

        self.to_currency_label = tk.Label(self.window, text="To Currency")
        self.to_currency_label.grid(column=0, row=1, padx=5, pady=5)
        self.to_currency_options = sorted(self.get_currency_options())
        self.to_currency_dropdown = tk.OptionMenu(self.window, self.to_currency, *self.to_currency_options)
        self.to_currency_dropdown.grid(column=1, row=1, padx=5, pady=5)

        self.amount_label = tk.Label(self.window, text="Amount")
        self.amount_label.grid(column=0, row=2, padx=5, pady=5)
        self.amount_entry = tk.Entry(self.window, textvariable=self.amount)
        self.amount_entry.grid(column=1, row=2, padx=5, pady=5)

        self.converted_amount_label = tk.Label(self.window, text="Converted Amount")
        self.converted_amount_label.grid(column=0, row=3, padx=5, pady=5)
        self.converted_amount_entry = tk.Entry(self.window, textvariable=self.converted_amount)
        self.converted_amount_entry.grid(column=1, row=3, padx=5, pady=5)

        self.convert_button = tk.Button(self.window, text="Convert", command=self.convert)
        self.convert_button.grid(column=1, row=4, padx=5, pady=5)

        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.window.mainloop()

    def get_currency_options(self):
        data = requests.get(self.url).json()
        return [currency for currency in data["rates"]]

    def convert(self):
        try:
            amount = float(self.amount.get())
        except ValueError:
            self.converted_amount.set("Invalid Amount")
            return

        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()

        data = requests.get(self.url).json()
        try:
            rate = data["rates"][to_currency] / data["rates"][from_currency]
            converted_amount = amount * rate
            self.converted_amount.set(converted_amount)
        except KeyError:
                    self.converted_amount.set("Invalid Currency")
url = "https://api.exchangerate-api.com/v4/latest/USD"
app = App(url)
