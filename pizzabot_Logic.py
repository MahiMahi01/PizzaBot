# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 17:05:14 2025

@author: mahee
"""

def get_response(user_input):
    user_input = user_input.lower()

    if "menu" in user_input or "pizzas" in user_input:
        return "We serve Margherita, Pepperoni, BBQ Chicken, and Veggie pizzas."

    elif "bbq chicken" in user_input:
        return "Our BBQ Chicken pizza has chicken, BBQ sauce, onion, capsicum, and mozzarella."

    elif "vegetarian" in user_input or "veg" in user_input:
        return "Yes! Our Margherita and Veggie pizzas are 100% vegetarian."

    elif "open" in user_input or "hours" in user_input:
        return "We're open 11 AM to 10 PM daily."

    elif "delivery" in user_input:
        return "Delivery usually takes 30–45 minutes in Muswellbrook."

    elif "call" in user_input or "phone" in user_input:
        return "You can call us at (02) 1234 5678."

    elif "order" in user_input:
        return "You can order online from our website or call us directly."

    elif "where" in user_input or "location" in user_input:
        return "We’re at 123 Main Street, Muswellbrook, next to the pharmacy."

    elif "thanks" in user_input or "thank you" in user_input:
        return "You’re welcome! 😊"

    else:
        return "I’m not sure about that. You can call us at (02) 1234 5678 for more help!"
