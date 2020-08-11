import requests
from flask import Flask, render_template, request, flash, redirect, url_for
from forms import weather_data, weather_data2, weather_data3

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def main():
    return render_template('main.html')
#VILNIUS----------------------------------------------------------------------------------------

@app.route('/vilnius')
def vilnius():
    return render_template('vilniuslentele.html', weather_data=weather_data)

@app.route('/send', methods=['GET', 'POST'])
def send():
        return redirect(url_for('main'))

#KAUNAS----------------------------------------------------------------------------------------
@app.route('/kaunas')
def kaunas():
    return render_template('kaunaslentele.html', weather_data2=weather_data2)

@app.route('/sendd', methods=['GET', 'POST'])
def sendd():
        number = request.form['age'] #kai paspaudziam ant mygtuko nuveda i pagrindini
        return redirect(url_for('main', number=number))


#MARIJAMPOLE----------------------------------------------------------------------------------------
@app.route('/marijampole')
def marijampole():
    return render_template('marijampolelentele.html', weather_data3=weather_data3)

@app.route('/senddd', methods=['GET', 'POST'])
def senddd():
        number = request.form['age'] #kai paspaudziam ant mygtuko nuveda i pagrindini
        return redirect(url_for('main', number=number))

if __name__ == '__main__':
    app.run(debug=True)