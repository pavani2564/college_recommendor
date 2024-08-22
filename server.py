<<<<<<< HEAD
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, template_folder="templates")

data = pd.read_excel('data.xlsx')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index_page')
def index_page():
    return render_template('index.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    rank = int(request.form.get('rank'))
    caste = request.form.get('caste')
    location = request.form.get('location')
    branch = request.form.get('branch')
    if caste.endswith("BOYS"):
        gender = "BOYS"
    else:
        gender =  "GIRLS"

    gender_column = f"{caste}_{gender}"

    filtered_data = data[
        (data[gender_column] > rank) &
        (data['DIST'] == location) &
        (data['branch_code'] == branch)
    ]
    recommended_colleges = filtered_data[['inst_name', 'DIST', 'PLACE', 'branch_code']].to_dict(orient='records')

    if len(recommended_colleges) == 0:
        message = 'Sorry, there are no colleges of your choice available.'
        return render_template('recommendations.html', colleges=None, message=message)
    else:
        return render_template('recommendations.html', colleges=recommended_colleges, message=None)

if __name__ == '__main__':
    app.run(debug=False)
=======
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, template_folder="templates")

data = pd.read_excel('data.xlsx')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index_page')
def index_page():
    return render_template('index.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    rank = int(request.form.get('rank'))
    caste = request.form.get('caste')
    location = request.form.get('location')
    branch = request.form.get('branch')
    if caste.endswith("BOYS"):
        gender = "BOYS"
    else:
        gender =  "GIRLS"

    gender_column = f"{caste}_{gender}"

    filtered_data = data[
        (data[gender_column] > rank) &
        (data['DIST'] == location) &
        (data['branch_code'] == branch)
    ]
    recommended_colleges = filtered_data[['inst_name', 'DIST', 'PLACE', 'branch_code']].to_dict(orient='records')

    if len(recommended_colleges) == 0:
        message = 'Sorry, there are no colleges of your choice available.'
        return render_template('recommendations.html', colleges=None, message=message)
    else:
        return render_template('recommendations.html', colleges=recommended_colleges, message=None)

if __name__ == '__main__':
    app.run(debug=False)
>>>>>>> 4215f6abc834729663cf0f0d50ec700df52adace
