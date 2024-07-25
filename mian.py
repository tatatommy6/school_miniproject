from flask import Flask, redirect, url_for, render_template_string, request
import a
import like

app = Flask(__name__)
a_app = a.create_app()
like_app = like.create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'analyze' in request.form:
            return redirect(url_for('analyze'))
        elif 'choose_team' in request.form:
            return redirect(url_for('choose_team'))
    return render_template_string(html_template)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    with a_app.test_request_context('/analyze', method=request.method, data=request.form):
        response = a_app.full_dispatch_request()
        return response

@app.route('/choose_team', methods=['GET', 'POST'])
def choose_team():
    with like_app.test_request_context('/choose_team', method=request.method, data=request.form):
        response = like_app.full_dispatch_request()
        return response

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soccer Match Analyzer - Main</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            border-radius: 8px;
            margin-top: 50px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        button {
            padding: 10px 20px;
            margin: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Soccer Match Analyzer - Main Page</h1>
        <form method="post">
            <button type="submit" name="analyze">분석</button>
            <button type="submit" name="choose_team">좋아하는 팀 선택</button>
        </form>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(port=5000, debug=True)
