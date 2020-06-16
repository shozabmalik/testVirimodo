from flask import Flask, render_template, request
import pymysql.cursors
import os

app = Flask(__name__)
IMAGES_DIR = os.path.join(os.getcwd(), "images")

conn = pymysql.connect(host='localhost',
                       port=8888,
                       user='root',
                       password='',
                       db='LandingPage',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if (request.form):
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone number']

        cursor = conn.cursor()
        query = 'SELECT * FROM testDB WHERE email = %s'
        cursor.execute(query, email)
        data = cursor.fetchone()
        cursor.close()
        if (data):
            error = "A person with this email already exists in the database"
            return render_template('register.html', error=error)
        else:
            ins = "INSERT INTO LandingPage (name, email, phone number) VALUES (%s, %s, %s)"
            cursor.execute(ins, (name, email, phone_number))
            conn.commit()
            cursor.close()
            return render_template('index.html')


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
