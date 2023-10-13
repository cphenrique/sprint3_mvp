from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Make a request to the external API
    api_url = "http://192.168.0.16:5000/processos"  # Replace with the actual API URL
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return render_template('index.html', processos=data)
    else:
        return render_template('index.html') #"Failed to fetch data from the API"

if __name__ == '__main__':
    app.run(debug=True)