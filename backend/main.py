from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
import forms# import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from colleges import get_college_info
import requests


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

@app.route('/match', methods=['GET', 'POST'])
def match():
    if request.method == 'POST':
        population = request.form.get('population')
        department = request.form.get('department')
        environment = request.form.get('environment')

        api_key = '9cx6Llu0TXhNipn0XjML7TTictmFY8eKAJtmn2aQ'
        url = 'https://api.data.gov/ed/collegescorecard/v1/schools'
        
        # Mapping user input to API filters
        population_size_map = {
            'small': '0..2000',
            'medium': '2001..15000',
            'large': '15001..'
        }
        
        environment_map = {
            'city': '11,12,13',  # Locale codes for city
            'rural': '41,42,43', # Locale codes for rural
            'suburban': '21,22,23' # Locale codes for suburban
        }
    

        params = {
            'api_key': api_key,
            'fields': 'school.name,school.city,latest.student.size,latest.academics.program_percentage,latest.cost.attendance.academic_year',
            'latest.student.size__range': population_size_map.get(population),
            'school.locale': environment_map.get(environment),
        }

        response = requests.get(url, params=params)
        colleges = response.json()
        print(colleges)

        return render_template('results.html', colleges=colleges)
    return render_template('match.html')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)
