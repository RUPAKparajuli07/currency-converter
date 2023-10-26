# Currency Converter Documentation

This documentation explains the functionality and usage of the provided Python code that implements a simple currency converter using the Tkinter library and a currency exchange rate API. The program allows users to input an amount in one currency and convert it to another currency.

## Table of Contents
1. [Introduction](#1-introduction)
2. [Prerequisites](#2-prerequisites)
3. [Code Explanation](#3-code-explanation)
4. [How to Use](#4-how-to-use)

## 1. Introduction

The code defines a `CurrencyConverter` class that creates a graphical user interface (GUI) for a currency conversion application. It uses the Tkinter library for the GUI elements and makes API requests to obtain exchange rate data from a currency exchange rate API.

## 2. Prerequisites

Before using the code, make sure you have the following prerequisites:

- Python 3.x installed.
- The `tkinter` library is included with Python's standard library.
- An internet connection to access the currency exchange rate API.

## 3. Code Explanation

### 3.1. Class `CurrencyConverter`

The `CurrencyConverter` class is the heart of the application and performs the following key functions:

- Initialize the GUI elements, including labels, input fields, and buttons.
- Fetch the currency exchange rate data from a specified API.
- Handle currency conversion based on user input.

### 3.2. Initialization

- The class constructor `__init__` initializes the GUI and sets up the Tkinter window. It also initializes several variables and widgets:

    - `self.window`: The main Tkinter window.
    - `self.from_currency`, `self.to_currency`, `self.amount`, and `self.converted_amount`: Tkinter StringVar objects to store user input and conversion results.
    - `self.url`: The URL of the currency exchange rate API.

### 3.3. GUI Setup

The GUI is set up with labels, dropdown menus, input fields, and a conversion button.

- `self.from_currency_label` and `self.to_currency_label`: Label widgets to display "From Currency" and "To Currency" labels.
- `self.from_currency_dropdown` and `self.to_currency_dropdown`: OptionMenu widgets to select the source and target currencies.
- `self.amount_label` and `self.amount_entry`: Label and Entry widgets for inputting the amount to be converted.
- `self.converted_amount_label` and `self.converted_amount_entry`: Label and Entry widgets to display the converted amount.
- `self.convert_button`: Button widget to trigger the conversion process.

### 3.4. GUI Positioning

- The code positions the widgets on the window and centers it on the screen.
- The `convert` method is bound to the "Convert" button, and it handles the conversion process.

### 3.5. API Requests

- The `get_currency_options` method sends a GET request to the specified currency exchange rate API URL and retrieves the available currency options.

### 3.6. Currency Conversion

- The `convert` method calculates the converted amount based on user input. It first validates the user's input and then uses the exchange rate data obtained from the API to perform the conversion.

## 4. How to Use

To use the currency converter:

1. Ensure you have the prerequisites mentioned earlier.
2. Provide the URL of a currency exchange rate API in the `url` variable.
3. Create an instance of the `CurrencyConverter` class with the URL as a parameter.
4. Run the Python script to open the GUI.
5. Select the source and target currencies from the dropdown menus, enter an amount to convert, and click the "Convert" button.
6. The converted amount will be displayed in the "Converted Amount" field.

Remember to have an active internet connection when running the code to fetch the exchange rate data from the API.

That's it! You now have a basic currency converter application. Feel free to customize it and add more features as needed.
