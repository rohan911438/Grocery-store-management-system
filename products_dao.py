from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    cursor.close()  # Added missing cursor.close()
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()
    
    product_id = cursor.lastrowid
    cursor.close()  # Added missing cursor.close()
    return product_id

def delete_product(connection, product_id):
    cursor = connection.cursor()
    # Fixed SQL injection vulnerability
    query = ("DELETE FROM products where product_id=%s")
    cursor.execute(query, (product_id,))
    connection.commit()

    deleted_id = cursor.lastrowid
    cursor.close()  # Added missing cursor.close()
    return deleted_id

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': '10'
    }))