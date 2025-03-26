#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install mysql-connector-python')


# In[4]:


import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aneesh25",  # Change this
        database="MessMenuDB",
        use_pure=True 
    )
    print("Connected Successfully!")
    

except mysql.connector.Error as err:
    print(f"Error: {err}")


# In[3]:


import os
os.system(r'"C:\Program Files\MySQL\MySQL Server 9.2\bin\mysqld.exe" --port=3306')


# In[2]:


import sys
get_ipython().system('{sys.executable} -m pip install --upgrade mysql-connector-python')


# In[5]:


import mysql.connector

def setup_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aneesh25",
        use_pure=True
    )
    cursor = conn.cursor()

    # Step 1: Drop the existing database and create a new one
    cursor.execute("DROP DATABASE IF EXISTS MessMenuDB")
    cursor.execute("CREATE DATABASE MessMenuDB")
    cursor.execute("USE MessMenuDB")

    # Step 2: Create tables
    cursor.execute("""
        CREATE TABLE Students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            reg_no VARCHAR(20) UNIQUE NOT NULL,
            name VARCHAR(100),
            block VARCHAR(10),
            room_number VARCHAR(10)
        )
    """)

    cursor.execute("""
        CREATE TABLE MessDetails (
            id INT AUTO_INCREMENT PRIMARY KEY,
            reg_no VARCHAR(20),
            mess_name VARCHAR(50),
            mess_type VARCHAR(20),
            food_suggestion VARCHAR(100),
            meal_type VARCHAR(50),
            feasibility VARCHAR(10),
            FOREIGN KEY (reg_no) REFERENCES Students(reg_no) ON DELETE CASCADE
        )
    """)

    print("Database and Tables Created Successfully!")

    

if __name__ == "__main__":
    setup_database()


# In[ ]:




