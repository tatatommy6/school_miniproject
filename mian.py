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
        return response.get_data(as_text=True)

@app.route('/choose_team', methods=['GET', 'POST'])
def choose_team():
    with like_app.test_request_context('/choose_team', method=request.method, data=request.form):
        response = like_app.full_dispatch_request()
        return response.get_data(as_text=True)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soccer Match Analyzer - Main</title>
</head>
<body>
    <div class="content">
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
