from flask import Flask
from flask import request
from flask import render_template
import csv
import dao

app = Flask(__name__)
DATA_TEMP = "temp.tsv"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/file_upload', methods=['GET','POST'])
def upload_data():
    if request.method == 'POST':
        file = request.files['tsv_file']
        print("File: ",file.filename)
        file.save(DATA_TEMP)
        print("Saved")
        data = []
        with open('temp.tsv') as file:
            rd = csv.reader(file, delimiter="\t")
            data = list(rd)
            data = list(tuple(item) for item in data[1:])
        conn = dao.get_connection()
        cursor = conn.cursor()
        query = 'INSERT INTO items (Item, ItemDescription, ItemPrice, ItemCount, Vendor, VendorAddress) ' \
                'values (%s,%s,%s,%s,%s,%s)'
        cursor.executemany(query,data)
        conn.commit()
        print("Records Inserted: ",cursor.rowcount)
        cursor.close()
        conn.close()


    return "Success"


@app.route('/upload_page')
def upload_page():
    return render_template('upload.html')


@app.route('/view')
def view():
    conn = dao.get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM items"
    cursor.execute(query)
    res = cursor.fetchall()
    for i in res:
        print(i)
    cursor.close()
    conn.close()
    return render_template('view.html', data=res)

@app.route('/revenue')
def get_revenue():
    conn = dao.get_connection()
    cursor = conn.cursor()
    query = "SELECT ItemPrice, ItemCount from items"
    cursor.execute(query)
    res = cursor.fetchall()
    revenue = 0.0
    for i in res:
        revenue += float(i[0])*float(i[1])
    print(revenue)

    return render_template("revenue.html", revenue=revenue)




if __name__ == '__main__':
    app.run(port=8080)