# How to Create a Connection from Python to MySQL

In this guide, we'll walk you through the steps to connect a Python application to a MySQL database.

## Prerequisites

Before you start, ensure you have the following:

- Python installed on your system. You can download it from [python.org](https://www.python.org/).
- MySQL server installed and running. You can download it from [mysql.com](https://www.mysql.com/).
- The `mysql-connector-python` library installed. You can install it using `pip`.

## Step 1: Install MySQL Connector

First, you need to install the MySQL Connector library for Python. Open your terminal or command prompt and run:

```sh
pip install mysql-connector-python  
```

## Step 2: Write code in python
- Simple code: you can write the credential inside the python code (https://github.com/erickpaulus/DB/blob/main/mysql_reference.py)
- Complex code: For safety reasons, you can separate the credentials from [the code](https://github.com/erickpaulus/DB/blob/main/connect_mysql.py) by using a [configuration file](https://github.com/erickpaulus/DB/blob/main/config.ini)
