# import openai
# import os
# from dotenv import load_dotenv

# # .env 파일 로드
# load_dotenv()
# # 환경 변수에서 OpenAI API 키 가져오기
# openai_api_key = os.getenv('OPENAI_API_KEY')

# # OpenAI API 키 설정
# openai.api_key = openai_api_key

# def analyze_match(match_info):
#     # OpenAI API를 사용하여 분석 요청
#     response = openai.ChatCompletion.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are an expert in analyzing soccer matches."},
#             {"role": "user", "content": f"Analyze the match: {match_info}"},
#         ],
#         max_tokens=1000,
#         temperature=0.1,
#         n=1,
#         stop=None,
#     )
#     # 결과 출력
#     analysis = response.choices[0].message['content'].strip()
#     return analysis

# def main():
#     match_info = input("분석할 경기를 입력해주세요 예):몇월 몇일 어떤팀 대 어떤팀 경기\n")
#     answer = analyze_match(match_info)
#     print(f"{answer}")

# if __name__ == "__main__":
#     main()



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

app = Flask(__name__)

def analyze_match(match_info):
    # OpenAI API를 사용하여 분석 요청
    response = openai.ChatCompletion.create(
        model="gpt-4",
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

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis = ""
    if request.method == 'POST':
        match_info = request.form['match_info']
        analysis = analyze_match(match_info)
    return render_template_string(html_template, analysis=analysis)


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soccer Match Analyzer</title>
</head>
<body>
    <div class="content">
        <h1>Soccer Match Analyzer</h1>
        <form method="post">
            <label for="match_info">분석할 경기를 입력해주세요 (예: 몇월 몇일 어떤팀 대 어떤팀 경기):</label><br>
            <input type="text" id="match_info" name="match_info" required><br><br>
            <button type="submit">분석 요청</button>
        </form>
        {% if analysis %}
        <h2>분석 결과:</h2>
        <p>{{ analysis }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)