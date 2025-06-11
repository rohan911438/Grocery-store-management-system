# 🛒 Grocery Store Management System

This is a complete Grocery Store Management System built using **Python**, **Flask**, and **MySQL**. It helps small stores manage inventory, customer orders, and product listings through a RESTful API backend.

---

## 🚀 Features

- 🧾 Order Management (create and view orders)
- 📦 Product Management (add, view, delete products)
- ⚖️ Unit of Measure (manage kg, liter, piece, etc.)
- 🗃️ MySQL database for persistent storage
- 🌐 REST API via Flask
- 🧩 Modular Python files for scalability

---

## 🛠️ Technologies Used

- Python 3.x
- Flask (backend framework)
- MySQL (relational database)
- flask-cors (for API access)
- mysql-connector-python

---

## 📂 Project Structure

## 📁 Project Structure

- `server.py` – Flask app with all API routes
- `sql_connection.py` – MySQL connection configuration
- `schema.sql` – SQL file for database setup
- `requirements.txt` – Python dependencies
- `orders_dao.py` – Order-related logic
- `products_dao.py` – Product-related logic
- `uom_dao.py` – Unit of Measure handling
- `README.md` – Project documentation


---

## 🧰 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/rohan911438/Grocery-store-management-system.git
cd Grocery-store-management-system
```




### 2. 🛠️ Set Up the MySQL Database

1. Ensure MySQL is installed and running.
2. Log in to MySQL from your terminal:
```bash
CREATE DATABASE gs;
USE gs;
SOURCE schema.sql;
INSERT INTO uom (uom_name) VALUES ('kg'), ('litre'), ('piece');
```



### 3.🛠️ Configure Database Access
In sql_connection.py, update:
```bash
__cnx = mysql.connector.connect(
    host='127.0.0.1',
    database='gs',
    user='root',
    password=''  # Change this to your MySQL root password
)
```

### 4. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Flask Server
```bash
python server.py

```

## 🔌 API Endpoints

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| GET    | /getUOM        | Get all units of measure |
| GET    | /getProducts   | Get list of products     |
| POST   | /insertProduct | Add a new product        |
| POST   | /deleteProduct | Delete a product by ID   |
| GET    | /getAllOrders  | View all customer orders |
| POST   | /insertOrder   | Create a new order       |




### 📦 Example JSON (Insert Product)
```bash
{
  "product_name": "Milk",
  "uom_id": 2,
  "price_per_unit": 25.5
}

```

###  🧾 Example JSON (Insert Order)
```bash
{
  "customer_name": "Ramesh",
  "grand_total": 81.0,
  "order_details": [
    { "product_id": 1, "quantity": 2, "total_price": 50 },
    { "product_id": 2, "quantity": 1, "total_price": 31 }
  ]
}


```
### 🎓 What You’ll Learn from This Project
How to build REST APIs using Flask

How to integrate a MySQL database with Python

Best practices for modular code architecture

How to handle real-world data like products and orders

Using tools like Postman for testing and debugging APIs

### 🤝 Contributing
Have ideas to improve this project?
Feel free to fork it, create a new branch, and submit a pull request.
All contributions and feedback are welcome!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software with proper attribution.

### 📬 Contact
Created with ❤️ by Rohan
📧 Reach out via GitHub: rohan911438

If you find this project useful, consider giving it a ⭐ on GitHub!

