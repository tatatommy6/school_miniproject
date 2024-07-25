import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, render_template_string

# .env 파일 로드
load_dotenv()

# 환경 변수에서 OpenAI API 키 가져오기
openai_api_key = os.getenv('OPENAI_API_KEY')

# OpenAI API 키 설정
openai.api_key = openai_api_key

def create_app():
    app = Flask(__name__)

    def analyze_match(match_info):
        # OpenAI API를 사용하여 분석 요청
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert in analyzing soccer matches."},
                {"role": "user", "content": f"Analyze the match: {match_info}"},
            ],
            max_tokens=1000,
            temperature=0.1,
            n=1,
            stop=None,
        )
        # 결과 출력
        analysis = response.choices[0].message['content'].strip()
        return analysis

    @app.route('/analyze', methods=['GET', 'POST'])
    def analyze():
        analysis = ""
        if request.method == 'POST':
            match_info = request.form['match_info']
            analysis = analyze_match(match_info)
        return render_template_string(html_template, analysis=analysis)

    return app

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soccer Match Analyzer</title>
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
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .result {
            margin-top: 30px;
            padding: 20px;
            background-color: #e9ecef;
            border-radius: 8px;
        }
        .result h2 {
            color: #495057;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Soccer Match Analyzer</h1>
        <form method="post">
            <label for="match_info">분석할 경기를 입력해주세요 (예: 몇월 몇일 어떤팀 대 어떤팀 경기):</label><br>
            <input type="text" id="match_info" name="match_info" required><br><br>
            <button type="submit">분석 요청</button>
        </form>
        {% if analysis %}
        <div class="result">
            <h2>분석 결과:</h2>
            <p>{{ analysis }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app = create_app()
    app.run(port=5001, debug=True)
