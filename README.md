# Grocery Store Management System

A professional, full-stack Python project for managing a grocery store's products, orders, and inventory using Flask and MySQL.

## Features
- Product management (add, view, delete)
- Order management (create, view)
- Unit of Measure (UOM) management
- RESTful API with Flask
- MySQL database integration

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd Grocery-Store-Management-System-using-Python
```

### 2. Set Up the Database
- Make sure MySQL is installed and running.
- Create a database named `gs`:
  ```sql
  CREATE DATABASE gs;
  ```
- Run the provided schema:
  ```sql
  USE gs;
  SOURCE schema.sql;
  ```
- (Optional) Insert some initial UOMs:
  ```sql
  INSERT INTO uom (uom_name) VALUES ('kg'), ('litre'), ('piece');
  ```

### 3. Configure Database Credentials
- Edit `sql_connection.py` and set your MySQL username and password.

### 4. Install Python Dependencies
```
pip install -r requirements.txt
```

### 5. Run the Server
```
python server.py
```
- The API will be available at `http://localhost:5000/`

## API Endpoints
- `GET /getUOM` - List all units of measure
- `GET /getProducts` - List all products
- `POST /insertProduct` - Add a new product
- `POST /deleteProduct` - Delete a product
- `GET /getAllOrders` - List all orders
- `POST /insertOrder` - Create a new order

## Professional Tips for LinkedIn Posting
- Share a brief project summary and your motivation.
- Highlight the tech stack: Python, Flask, MySQL.
- Mention features and what you learned.
- Add screenshots or a demo video.
- Link to your GitHub repo.

---

**Feel free to reach out if you have questions or want to collaborate!** 