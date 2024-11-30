from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    # Add your code to handle the subscription logic here
    return jsonify({'message': 'Subscription successful'})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    conn = create_connection()
    if conn is not None:
        add_subscription(conn, email)
        conn.close()
        return jsonify({'message': 'Subscription successful'})
    else:
        return jsonify({'message': 'Error! cannot create the database connection.'})
