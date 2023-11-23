# Inventory Management System

This Inventory Management System is a Python-based application designed to facilitate efficient management of inventory-related tasks including product handling, order processing, sales tracking, user administration, and database management.

## Features

- **Product Management:** Add, update, delete, and list products with detailed information such as name, price, quantity, and category.
- **Order Management:** Add and list orders with supplier details, date, and product specifics.
- **Sales Management:** Track sales, calculate totals, and maintain sales records.
- **User Administration:** Create and manage user accounts with appropriate permissions.
- **Database Management:** Create, list, and recreate the database to suit business needs.
- **Menu Interface:** Intuitive menu-driven interface for easy navigation through functionalities.

## Requirements

- Python 3.x
- MySQL Database

## Installation and Setup

1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Install necessary dependencies: `pip install mysql-connector-python`
3. Ensure MySQL is installed and running.
4. Configure the database connection parameters in the code.

## Usage

1. Run the program: `python inventory_management.py`
2. Follow the on-screen menu to access various functionalities.
3. Use appropriate options to manage products, orders, sales, users, and the database.

## Security Note

- Avoid exposing sensitive database credentials in the code.
- Sanitize user inputs to prevent SQL injection attacks.
