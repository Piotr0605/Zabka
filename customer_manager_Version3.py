"""
Module for managing customer data in the Frog Online Store.
Provides functionalities to register, remove, and log customer purchases.
"""

import csv
import os
import random

def register_customer(first_name, last_name):
    """
    Registers a new customer and assigns a unique 4-digit ID.

    Args:
        first_name (str): First name of the customer.
        last_name (str): Last name of the customer.

    Returns:
        str: Customer ID.

    Raises:
        IOError: If the customers.csv file cannot be accessed.
    """
    try:
        customer_id = str(random.randint(1000, 9999))

        # Save to customers.csv
        with open("customers.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([customer_id, first_name, last_name])
        
        # Create customer-specific file in DATABASE folder
        os.makedirs("DATABASE", exist_ok=True)
        with open(f"DATABASE/{customer_id}.txt", mode="w") as customer_file:
            customer_file.write("Purchase History:\n")
        
        return customer_id
    except Exception as e:
        print(f"Error registering customer: {e}")


def remove_customer(identifier, by_name=False):
    """
    Removes a customer from the customers.csv file by ID or name.

    Args:
        identifier (str): Customer ID or name to remove.
        by_name (bool): If True, removes by name; otherwise, by ID.

    Raises:
        ValueError: If the customer is not found.
    """
    try:
        # Load the customers file
        with open("customers.csv", mode="r") as file:
            rows = list(csv.reader(file))
        
        if by_name:
            rows = [row for row in rows if row[1] != identifier and row[2] != identifier]
        else:
            rows = [row for row in rows if row[0] != identifier]
        
        # Save back to the file
        with open("customers.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        # Remove customer-specific file if exists
        customer_file_path = f"DATABASE/{identifier}.txt"
        if os.path.exists(customer_file_path):
            os.remove(customer_file_path)
    except Exception as e:
        print(f"Error removing customer: {e}")