from flask import Flask, request, render_template_string, redirect, url_for
import requests
import json

def get_team_data(team):
    # API 키
    API_KEY = '1a9f31ef03684b888fea9637c51bbd6f'

    # API 엔드포인트 URL
    url = f'http://api.football-data.org/v2/competitions/{team}/teams'

    # 요청 헤더 설정
    headers = {
        'X-Auth-Token': API_KEY
    }

    # API 요청 보내기
    response = requests.get(url, headers=headers)

    # 응답 데이터 확인
    if response.status_code == 200:
        data = response.json()
        # 특정 필드 수정
        formatted_teams = []
        for team in data['teams']:
            formatted_team = f"""
            <div class="team">
                <h2>{team['name']} ({team['shortName']})</h2>
                <img src="{team['crestUrl']}" alt="Team Crest" width="100"><br>
                <strong>Address:</strong> {team['address']}<br>
                <strong>Phone:</strong> {team['phone']}<br>
                <strong>Website:</strong> <a href="{team['website']}">{team['website']}</a><br>
                <strong>Email:</strong> {team['email']}<br>
                <strong>Founded:</strong> {team['founded']}<br>
                <strong>Club Colors:</strong> {team['clubColors']}<br>
                <strong>Venue:</strong> {team['venue']}<br>
            </div>
            <hr>
            """
            formatted_teams.append(formatted_team)
        return "\n".join(formatted_teams)
    else:
        return f"Error: {response.status_code}"

team_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Choose Favorite Team</title>
</head>
<body>
    <div class="container">
        <h1>Choose Your Favorite Team</h1>
        <form method="post">
            <label for="favorite_team">좋아하는 팀을 선택하세요:</label><br>
            <select id="favorite_team" name="favorite_team">
                <option value="PL">PL</option>
                <option value="BL1">Bundesliga</option>
                <option value="SA">Serie A</option>
                <option value="PD">La Liga</option>
            </select><br><br>
            <button type="submit">선택</button>
        </form>
    </div>
</body>
</html>

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
    label {
        margin: 10px 0 5px;
        font-weight: bold;
    }
    select, button {
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid #ddd;
        border-radius: 4px;
        width: 100%;
        max-width: 300px;
    }
    button {
        background-color: #007bff;
        color: white;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
</style>
"""

result_template = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team Data</title>
</head>
<body>
    <div class="container">
        <h1>Team Data</h1>
        {{ team_data|safe }}
        <a href="{{ url_for('choose_team') }}">Go Back</a>
    </div>
</body>
</html>

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
    .team {
        margin-bottom: 20px;
    }
    .team h2 {
        margin: 0;
        color: #007bff;
    }
    .team img {
        margin: 10px 0;
    }
    hr {
        border: 0;
        border-top: 1px solid #ddd;
        margin: 20px 0;
    }
    a {
        color: #007bff;
    }
    a:hover {
        text-decoration: none;
    }
</style>
"""

def create_app():
    app = Flask(__name__)

    @app.route('/choose_team', methods=['GET', 'POST'])
    def choose_team():
        if request.method == 'POST':
            favorite_team = request.form.get('favorite_team')
            print(f"Favorite team selected: {favorite_team}")  # 선택된 팀 출력
            # 선택된 팀을 사용하여 API 요청을 보냅니다.
            team_data = get_team_data(favorite_team)
            print(f"Team data: {team_data}")  # API 응답 데이터 출력
            return render_template_string(result_template, team_data=team_data)
        return render_template_string(team_template)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5002, debug=True)
