from flask import Flask, request, render_template_string, redirect, url_for
import requests
import json

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
            return json.dumps(data, indent=4)
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
        <div class="content">
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
        <div class="content">
            <h1>Team Data</h1>
            <pre>{{ team_data }}</pre>
            <a href="{{ url_for('choose_team') }}">Go Back</a>
        </div>
    </body>
    </html>
    """

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5002, debug=True)
