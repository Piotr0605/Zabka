"""
Module for managing product data in the Frog Online Store.
Provides functionalities to add and remove products from the database.
"""

import pandas as pd

def add_product(product_id, product_name, price):
    """
    Adds a new product to the products.xlsx file.

    Args:
        product_id (int): Unique ID for the product.
        product_name (str): Name of the product.
        price (float): Price of the product.

    Raises:
        ValueError: If the product ID already exists.
    """
    try:
        # Load the products file
        products = pd.read_excel("products.xlsx")
        
        # Check for duplicate product ID
        if product_id in products["ID"].values:
            raise ValueError("Product ID already exists.")
        
        # Append new product
        new_product = {"ID": product_id, "Name": product_name, "Price": price}
        products = products.append(new_product, ignore_index=True)
        
        # Save back to the file
        products.to_excel("products.xlsx", index=False)
    except Exception as e:
        print(f"Error adding product: {e}")


def remove_product(identifier, by_name=False):
    """
    Removes a product from the products.xlsx file by ID or name.

    Args:
        identifier (int or str): Product ID or name to remove.
        by_name (bool): If True, removes by name; otherwise, by ID.

    Raises:
        ValueError: If the product is not found.
    """
    try:
        # Load the products file
        products = pd.read_excel("products.xlsx")
        
        if by_name:
            products = products[products["Name"] != identifier]
        else:
            products = products[products["ID"] != identifier]
        
        # Save back to the file
        products.to_excel("products.xlsx", index=False)
    except Exception as e:
        print(f"Error removing product: {e}")