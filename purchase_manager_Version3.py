"""
Module for handling product purchases in the Frog Online Store.
Provides functionality for customers to buy products and log their purchases.
"""

import pandas as pd
import os

def purchase_products(customer_id, product_list):
    """
    Allows a customer to purchase multiple products.

    Args:
        customer_id (str): ID of the customer making the purchase.
        product_list (list of tuples): List of tuples where each tuple contains
                                       (product_id, quantity).

    Raises:
        FileNotFoundError: If the products.xlsx or customer file is missing.
        ValueError: If the product ID is invalid or quantities are not available.
    """
    try:
        # Load products database
        products = pd.read_excel("products.xlsx")
        
        # Verify customer exists
        customer_file = f"DATABASE/{customer_id}.txt"
        if not os.path.exists(customer_file):
            raise FileNotFoundError(f"Customer file for ID {customer_id} not found.")
        
        total_cost = 0
        purchase_details = []

        for product_id, quantity in product_list:
            # Check if product exists
            product_row = products[products["ID"] == product_id]
            if product_row.empty:
                raise ValueError(f"Product ID {product_id} does not exist.")
            
            # Get product details
            product_name = product_row.iloc[0]["Name"]
            product_price = product_row.iloc[0]["Price"]
            total_price = product_price * quantity
            total_cost += total_price

            # Log purchase details
            purchase_details.append(f"{product_name} x{quantity}: {total_price} PLN")
        
        # Save purchase details to customer file
        with open(customer_file, mode="a") as file:
            file.write("\n".join(purchase_details) + f"\nTotal: {total_cost} PLN\n")
    except Exception as e:
        print(f"Error during purchase: {e}")