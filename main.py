# import openai
# import os
# from dotenv import load_dotenv
# # .env 파일 로드
# load_dotenv()
# # 환경 변수에서 OpenAI API 키 가져오기
# openai_api_key = os.getenv('OPENAI_API_KEY')

# # OpenAI API 키 설정
# openai.api_key = openai_api_key
# def analyze_match():
#     print("분석할 경기를 입력해주세요 예):몇월 몇일 어떤팀 대 어떤팀 경기\n")
    
#     # 분석할 데이터를 입력합니다.

#     # OpenAI API를 사용하여 분석 요청
#     response = openai.Completion.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "축구 경기를 분석하는 역할"},
#             {"role": "user", "content": f"input()"},
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
#         answer = analyze_match()
#         print(f"{answer}")

# if __name__ == "__main__":
#     main()  




import openai
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()
# 환경 변수에서 OpenAI API 키 가져오기
openai_api_key = os.getenv('OPENAI_API_KEY')

# OpenAI API 키 설정
openai.api_key = openai_api_key

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

def main():
    match_info = input("분석할 경기를 입력해주세요 예):몇월 몇일 어떤팀 대 어떤팀 경기\n")
    answer = analyze_match(match_info)
    print(f"{answer}")

if __name__ == "__main__":
    main()
