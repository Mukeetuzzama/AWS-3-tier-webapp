from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(**name**)

@app.route('/api/data',  methods=\['GET'])
def get\_data():
try:
connection = mysql.connector.connect(
host='aws3tierdb.cbw6ieuasxyz.eu-north-1.rds.amazonaws.com',
user='root',
password='amazzuteekum&100',
database='webapp'
)
if connection.is\_connected():
cursor = connection.cursor()
cursor.execute("SELECT message FROM messages LIMIT 1;")
result = cursor.fetchone()
return jsonify({'message': result\[0]})
except Error as e:
return jsonify({'error': str(e)})
finally:
if connection.is\_connected():
cursor.close()
connection.close()

if **name** == '**main**':
app.run(host='0.0.0.0', port=5000, debug=True)
