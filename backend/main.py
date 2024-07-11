from flask import Flask, render_template, url_for
from colleges import college_info_db

app = Flask(__name__)

# Create variables that hold columns and rows from the table
cols = [col for col in college_info_db]
rows = []
for index, row in college_info_db.iterrows():
    rows.append(row)
    # note, you can access a value from a row using row["column"]

@app.route('/')
def home():
    return "<p>Hello, World!</p>" 

@app.route('/display_college_info')
def display():
    return render_template('display_college_info.html', cols=cols, rows=rows)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")