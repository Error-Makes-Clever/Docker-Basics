from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <h1>Multiplication Table Generator</h1>
    <form method="POST">
        <label>Enter a number:</label>
        <input type="number" name="number" required>
        <button type="submit">Generate Table</button>
    </form>
    {% if table %}
    <h2>Table of {{ num }}</h2>
    <ul>
        {% for line in table %}
        <li>{{ line }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    table = None
    num = None
    
    if request.method == 'POST':
        num  = int(request.form['number'])
        table = [f"{num} x {i} = {num * i}" for i in range(1, 11)]
    
    return render_template_string(HTML_TEMPLATE, table=table, num=num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)