# How to Create a Connection from Python to SQL Server

In this guide, we'll walk you through the steps to connect a Python application to a SQL Server database.

## Prerequisites

Before you start, ensure you have the following:

- Python installed on your system. You can download it from [python.org](https://www.python.org/).
- SQL Server installed and running. You can download it from [microsoft.com](https://www.microsoft.com/en-us/sql-server).
- The `pyodbc` library installed. You can install it using `pip`.

## Step 1: Install Required Libraries

First, you need to install the `pyodbc` library for Python. Open your terminal or command prompt and run:

```sh
pip install pyodbc
```

## Step 2: Write code in python
- Simple code: you can write the credential inside [the python code](https://github.com/erickpaulus/DB/blob/main/sqlserver_reference.py)
- Complex code: For safety reasons, you can separate the credentials from [the code](https://github.com/erickpaulus/DB/blob/main/connect_sqlserver.py) by using a [configuration file](https://github.com/erickpaulus/DB/blob/main/config_sqlserver.ini)
