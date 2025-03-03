import tkinter as tk
from tkinter import messagebox


class CoffeeMachine:
    def __init__(self):
        # Initial resources for the coffee machine
        self.water = 1000  # milliliters
        self.coffee_beans = 500  # grams
        self.milk = 500  # milliliters
        self.sugar = 200  # grams
        self.maintenance_count = 0  # Counter for maintenance
        self.balance = 0.0  # virtual payment balance (in euros)

        # Menu for different drinks with their ingredients and price
        self.menu = {
            "Espresso": {"water": 50, "coffee_beans": 18, "milk": 0, "price": 1.5, "color": "brown"},
            "Ristretto": {"water": 30, "coffee_beans": 18, "milk": 0, "price": 1.7, "color": "darkred"},
            "Double espresso": {"water": 100, "coffee_beans": 36, "milk": 0, "price": 2.0, "color": "darkbrown"},
            "Café": {"water": 150, "coffee_beans": 20, "milk": 0, "price": 2.0, "color": "beige"},
            "Americano": {"water": 200, "coffee_beans": 15, "milk": 0, "price": 2.2, "color": "lightbrown"},
            "Cappuccino": {"water": 150, "coffee_beans": 24, "milk": 100, "price": 2.5, "color": "tan"},
            "Latte Macchiato": {"water": 200, "coffee_beans": 20, "milk": 150, "price": 3.0, "color": "lightyellow"},
            "Café au lait": {"water": 150, "coffee_beans": 18, "milk": 150, "price": 2.5, "color": "lightpink"},
            "Lait chaud": {"water": 0, "coffee_beans": 0, "milk": 200, "price": 2.0, "color": "lightblue"},
            "Thé": {"water": 200, "coffee_beans": 0, "milk": 0, "price": 1.5, "color": "green"},
        }