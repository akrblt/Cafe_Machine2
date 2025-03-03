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

        def check_resources(self, drink, size):
            # Check if there are enough resources to prepare the selected drink
            drink_data = self.menu[drink]
            water_required = drink_data["water"] * size
            coffee_beans_required = drink_data["coffee_beans"] * size
            milk_required = drink_data["milk"] * size

            # Check for sufficient water, coffee beans, and milk
            if self.water < water_required:
                return False, "water"
            if self.coffee_beans < coffee_beans_required:
                return False, "coffee_beans"
            if self.milk < milk_required:
                return False, "milk"
            return True, None

        def prepare_drink(self, drink, size):
            # Prepare the selected drink if there are enough resources
            drink_data = self.menu[drink]
            water_required = drink_data["water"] * size
            coffee_beans_required = drink_data["coffee_beans"] * size
            milk_required = drink_data["milk"] * size

            check, resource = self.check_resources(drink, size)
            if not check:
                return f"Insufficient resource: {resource}."

            # Deduct resources after preparation
            self.water -= water_required
            self.coffee_beans -= coffee_beans_required
            self.milk -= milk_required
            self.balance += drink_data["price"]
            self.maintenance_count += 1

            # Check if the machine needs cleaning
            if self.maintenance_count >= 5:
                return "Machine requires cleaning."

            return f"{drink} ({size} dl) prepared successfully!"

        def add_resources(self, water, coffee_beans, milk, sugar):
            # Add resources to the machine
            self.water += water
            self.coffee_beans += coffee_beans
            self.milk += milk
            self.sugar += sugar

        def clean_machine(self):
            # Clean the machine by resetting the maintenance counter
            self.maintenance_count = 0



