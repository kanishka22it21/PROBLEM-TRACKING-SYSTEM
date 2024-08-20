from flask import Flask, request, send_from_directory, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = {
        'Username': request.form.get('Username'),
        'Location': request.form.get('Location'),
        'Room No': request.form.get('Room No'),
        'Floor': request.form.get('Floor'),
        'Field Domain': request.form.get('Field Domain'),
        'Defect Appliances': request.form.get('Defect')
    }

   
    print(form_data, flush=True)

   
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Form Data in Sheets</title>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body>
        <h1>Form Submitted Successfully!</h1>
        <h2>Submitted Details:</h2>
        <ul>
            {% for key, value in form_data.items() %}
                <li><strong>{{ key }}:</strong> {{ value }}</li>
            {% endfor %}
        </ul>
        <a href="/">Back to Form</a>
    </body>
    </html>
    ''', form_data=form_data)

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('', filename)

if __name__ == '__main__':
    app.run(debug=True)
