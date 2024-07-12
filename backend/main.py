from flask import Flask, render_template, request, jsonify
from colleges import get_college_info
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# # Create variables that hold columns and rows from the table
# cols = [col for col in college_info_db]
# rows = []
# for index, row in college_info_db.iterrows():
#     rows.append(row)
#     # note, you can access a value from a row using row["column"]

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/display_college_info')
def display():
    return render_template('display_college_info.html', cols=cols, rows=rows)

@app.route('/search_college', methods=['GET','POST'])
def search_college():
    data = request.get_json()
    college_name = data.get('collegeName')
    result = get_college_info(college_name)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
