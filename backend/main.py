from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
import forms# import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from colleges import get_college_info


app = Flask(__name__)
proxied = FlaskBehindProxy(app)  ## add this line
app.config['SECRET_KEY'] = 'dbf9ddcbcbe89c72275f104812b8c15'

COLLEGE_INFO = get_college_info('vassar')


@app.route('/')
def start():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search_college', methods=['GET','POST'])
def search_college():
    global COLLEGE_INFO

    form = forms.RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        #flash(f'seach complete!', 'success')
        COLLEGE_INFO = get_college_info(form.nameSearch.data) #returns a df with college stats
        return redirect(url_for('display_college_info')) # if so - send to info page
    
    return render_template('info.html', title='Register', form=form)

@app.route('/match', methods=['GET', 'POST'])
def match():
    ## FILL IN HERE ##
    return render_template('match.html', title='Register', form=form)
    



@app.route('/display_college_info')
def display_college_info():

    cols = []
    rows = []
    if len(COLLEGE_INFO) > 0:
        # Create variables that hold columns and rows from the table
        cols = [col for col in COLLEGE_INFO]
        rows = []
        for index, row in COLLEGE_INFO.iterrows():
            # note, you can access a value from a row using row["column"]
            rows.append(row)
    
    return render_template('display_college_info.html', cols=cols, rows=rows)




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)
