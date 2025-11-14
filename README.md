Cursor E-Commerce Data Pipeline (Hands-On Project)

This project was completed as part of a **Cursor A-SDLC hands-on hiring task**, where the objective was to use **Cursor IDE + AI prompts** to build a mini end-to-end data pipeline.

The solution includes:

- Generating synthetic e-commerce datasets using Python  
- Loading the data into a SQLite database  
- Running a SQL query that joins 5 tables  
- Executing everything using Cursor prompts  
- Uploading the complete project to GitHub  

---

## 🧠 Objective

1. Generate 5 synthetic e-commerce data files  
2. Load the data into a database  
3. Perform SQL joins  
4. Do everything using Cursor IDE  
5. Push the project to GitHub  

This repo fulfills all of the above steps.

---

## 📂 Project Structure
cursor-ecom-hands-on/

│

├── generate_data.py

├── load_to_sqlite.py

├── query_join.py

│

├── customers.csv

├── products.csv

├── orders.csv

├── order_items.csv

├── payments.csv

│

├── ecom.db

│

└── README.md

---

## 🔧 Technologies Used

- Python  
- Cursor IDE (A-SDLC)  
- SQLite (sqlite3)  
- CSV  
- Git & GitHub  

---

## ✨ Features

- Automated synthetic data generation  
- Five relational tables  
- CSV → SQLite import pipeline  
- Full join query for analytics  
- Prompt-driven AI development  

---

## ▶️ How to Run

### 1️⃣ Generate data

python generate_data.py


### 2️⃣ Load into SQLite

python load_to_sqlite.py


### 3️⃣ Run SQL join

python query_join.py


---

## 📊 Final Output

<img width="216" height="419" alt="Screenshot 2025-11-14 021640" src="https://github.com/user-attachments/assets/6a64d33a-748f-4127-8e88-761835427ae0" />
<img width="1039" height="776" alt="Screenshot 2025-11-14 021744" src="https://github.com/user-attachments/assets/9f0acf6e-113d-4735-9f69-08bcc242e986" />
<img width="1093" height="264" alt="Screenshot 2025-11-14 021816" src="https://github.com/user-attachments/assets/7a0557e5-dbfb-4544-bb7c-8e8ec5da1f15" />


---

## 🤖 Cursor Prompts Used

**Prompt 1:** Generate 5 synthetic e-commerce CSV files with around 20 rows each:

- customers.csv → customer_id, name, email, city
- products.csv → product_id, product_name, category, price
- orders.csv → order_id, customer_id, order_date
- order_items.csv → order_item_id, order_id, product_id, quantity
- payments.csv → payment_id, order_id, amount, payment_method

Create Python code in a new file called generate_data.py that generates all these CSV files and saves them in the project folder. Use realistic but synthetic values (random names, categories, prices, dates within the past 90 days, and reasonable quantities). Ensure headers are included and generate ~20 rows per file.
After generating the code, save the file automatically in the project.
  
**Prompt 2:** Create a new Python file load_to_sqlite.py that:

- Creates a SQLite database named ecom.db
- Creates tables for customers, products, orders, order_items, payments matching the CSV schemas
- Reads each CSV file in the project folder
- Inserts all rows into the respective tables using Python's standard libraries only (csv, sqlite3)
- Commits changes and closes the DB connection

Use safe handling for CSV reading (skip headers) and make sure numeric columns use appropriate types. After generating, save the file automatically.
  
**Prompt 3:** Create a new Python file query_join.py that connects to ecom.db and executes an SQL query joining all 5 tables (customers, orders, order_items, products, payments).

The output printed to console should include columns:
- customer_name
- product_name
- category
- quantity
- price
- total_amount (price × quantity)
- payment_method
- order_date

Order the results by order_date. The file should run the query, fetch all rows, and print a readable header followed by each row (one per line). After generating, save the file automatically.
 
**Prompt 4:** Generate a step-by-step list of terminal commands to push this entire project to GitHub, including:

1. Initializing git in the project
2. Adding all files
3. Committing with a message
4. Creating (or switching to) the main branch
5. Adding a remote origin (provide placeholder for the repo URL)
6. Pushing to the remote

Format the response as a plain sequence of commands and short notes on where to replace values (e.g., replace <your-username> and <repo-name> in the remote URL). Keep commands cross-platform friendly for Windows PowerShell.

---

## Why This Project Stands Out

- Fully AI-generated workflow  
- Unique random dataset  
- Correct SQL joins  
- Clean repo  
- Professional README  

---

## 📬 Contact

**Name:** Tausif Ansari  
**Email:** tausifansari2907@gmail.com  
**GitHub:** https://github.com/tausif2907

