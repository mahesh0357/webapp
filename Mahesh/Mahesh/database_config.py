#Sets up table in database
#To Be Executed only once

import dao

def configure():
    drop = 'DROP TABLE IF EXISTS items'
    table = 'CREATE TABLE items (ItemId int NOT NULL PRIMARY KEY AUTO_INCREMENT,' \
            'Item varchar(255),' \
            'ItemDescription varchar(255),' \
            'ItemPrice Float,' \
            'ItemCount int,' \
            'Vendor varchar(255),' \
            'VendorAddress varchar(255));'
    conn = dao.get_connection()
    cursor = conn.cursor()
    cursor.execute(drop)
    cursor.execute(table)
    query = "SHOW TABLES"
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)


if __name__ == '__main__':
    configure()