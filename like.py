from flask import Flask, request, render_template_string, redirect, url_for

def create_app():
    app = Flask(__name__)

    @app.route('/choose_team', methods=['GET', 'POST'])
    def choose_team():
        if request.method == 'POST':
            favorite_team = request.form.get('favorite_team')
            # 여기에서 favorite_team을 저장하거나 사용할 수 있습니다.
            return redirect(url_for('index'))
        return render_template_string(team_template)

    return app

team_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Choose Favorite Team</title>
</head>
<body>
    <div class="content">
        <h1>Choose Your Favorite Team</h1>
        <form method="post">
            <label for="favorite_team">좋아하는 팀을 선택하세요:</label><br>
            <select id="favorite_team" name="favorite_team">
                <option value="Team A">Team A</option>
                <option value="Team B">Team B</option>
                <option value="Team C">Team C</option>
                <option value="Team D">Team D</option>
            </select><br><br>
            <button type="submit">선택</button>
        </form>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app = create_app()
    app.run(port=5002, debug=True)
