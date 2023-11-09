import urllib

import openai
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
import re


openai.api_key = "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"

# Create your views here.
@csrf_exempt
def Chat_gpt(request):

    if request.method == 'POST':
        print("리퀘스트 로그" + str(request.body))
        data = JSONParser().parse(request)
        prompt = data['prompt']
        str_prompt = str(prompt)

        # 모델 - GPT 3.5 Turbo 선택
        model = "gpt-3.5-turboa"

        # 메시지 설정하기
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": str_prompt}
        ]

        # ChatGPT API 호출하기
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        answer = str(response['choices'][0]['message']['content'])


        if answer:
            print("응답 성공")
            print(answer)
            return JsonResponse({'code': '0000', 'msg': answer}, status=200)
        else:
            print("실패")
            return JsonResponse({'code': '1001', 'msg': '응답실패'}, status=200)

@csrf_exempt
def papago(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        trans_text = data['text']

        client_id = "ebIYl6a2X8eQiRLd3WHa"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "BHMLx01Wnm"  # 개발자센터에서 발급받은 Client Secret 값

        encText = urllib.parse.quote(trans_text)
        data = "source=ko&target=en&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read().decode()
            response_json = json.loads(response_body)
            return JsonResponse(response_json['message']['result']['translatedText'], safe=False)
        else:
            print("Error Code:" + rescode)

@csrf_exempt
def recommend_next(request):

    if request.method == 'POST':
        print("리퀘스트 로그" + str(request.body))
        data = JSONParser().parse(request)
        prompt = data['previous']

        str_prompt = str(prompt) + ". Make the next fairy tale sentence to match the previous sentence. You must print only one sentence. Please print it out in Korean."
        #. Make the next fairy tale sentence to match the previous sentence. You must print only one sentence. Please print it out in Korean.
        #. 앞 문장과 어울리게 다음 동화문장을 만들어줘. 반드시 한 문장만 출력해야 돼. 꼭 한글로 출력해줘

        # 모델 - GPT 3.5 Turbo 선택
        model = "gpt-3.5-turbo"

        # 메시지 설정하기
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": str_prompt}
        ]

        # ChatGPT API 호출하기
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        answer = str(response['choices'][0]['message']['content'])


        if answer:
            print("응답 성공")
            print(answer)
            return JsonResponse({'code': '0000', 'msg': answer}, status=200)
        else:
            print("실패")
            return JsonResponse({'code': '1001', 'msg': '응답실패'}, status=200)

@csrf_exempt
def compatibility(request):

    if request.method == 'POST':
        print("리퀘스트 로그" + str(request.body))
        data = JSONParser().parse(request)
        prompt = data['check']
        str_prompt = str(prompt) + " 위 동화내용이 아이들에게 적합할까? 예,아니오 둘중하나로 대답해줘"

        # 모델 - GPT 3.5 Turbo 선택##
        model = "gpt-3.5-turbo"

        # 메시지 설정하기
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": str_prompt}
        ]

        # ChatGPT API 호출하기
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        answer = str(response['choices'][0]['message']['content'])
        answer_slice = answer[0:2]

        if "예" in answer_slice or "네" in answer_slice or "적합합니다" in answer_slice:
            print("아이들에게 적합함")
            print(answer)
            return JsonResponse({'code': '0000', 'msg': answer}, status=200)
        else:
            print("아이들에게 부적합")
            return JsonResponse({'code': '1001', 'msg': '부적합한내용'}, status=200)

@csrf_exempt
def pick_word(request):

    if request.method == 'POST':
        #단어 봅는 부분
        print("리퀘스트 로그" + str(request.body))
        data = JSONParser().parse(request)
        prompt = data['check']
        print(prompt)
        str_prompt = str(prompt) + "- In the previous fairy tale sentence, be sure to print out only two easy English words that can be recommended to children, separated by commas. Print only example English words without any other explanation. Do not provide any additional explanation. Be sure to print only two words, and always in English. Print it out, never use Korean."
        # - In the previous fairy tale sentence, be sure to print out only two easy English words that can be recommended to children, separated by commas. Print only example English words without any other explanation. Do not provide any additional explanation. Be sure to print only two words, and always in English. Print it out, never use Korean.
        # - 앞의 동화 문장에서 어린이에게 추천해줄만한 쉬운 영어단어 2개만 반드시 쉼표로 구분해서 출력해줘, 다른 설명없이 예시 영어단어만 출력해줘, 어떤 부가설명도 하지마, 반드시 2개 만 출력해줘, 반드시 영어로 출력해, 한글은 절대 쓰지마
        print(str_prompt)

        # 모델 - GPT 3.5 Turbo 선택
        model = "gpt-3.5-turbo"

        # 메시지 설정하기
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": str_prompt}
        ]

        # ChatGPT API 호출하기
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        answer = str(response['choices'][0]['message']['content'])
        print(answer)
        eng_split = answer.split(", ")

        # 번역 부분 1
        client_id = "ebIYl6a2X8eQiRLd3WHa"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "BHMLx01Wnm"  # 개발자센터에서 발급받은 Client Secret 값

        encText = urllib.parse.quote(eng_split[0])
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read().decode()
            response_json = json.loads(response_body)
            kor1 = response_json['message']['result']['translatedText']
            kor1 = kor1.replace(".", "")
            print(kor1)
        else:
            print("Error Code:" + rescode)

        # 번역 부분 2
        client_id = "ebIYl6a2X8eQiRLd3WHa"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "BHMLx01Wnm"  # 개발자센터에서 발급받은 Client Secret 값

        encText = urllib.parse.quote(eng_split[1])
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read().decode()
            response_json = json.loads(response_body)
            kor2 = response_json['message']['result']['translatedText']
            kor2 = kor2.replace(".","")
            print(kor2)
        else:
            print("Error Code:" + rescode)

        return JsonResponse({'eng1': eng_split[0], 'eng2': eng_split[1],
                            'kor1': kor1, 'kor2': kor2}, status=200)


@csrf_exempt
def first_recommend_next(request):

    if request.method == 'POST':
        print("리퀘스트 로그" + str(request.body))
        data = JSONParser().parse(request)
        prompt = data['previous']
        str_prompt = str(prompt) + " - From now on, you will take on the role of a children's story writer. We need to create stories that are creative and fit the emotions of children. Make the first sentence of the introduction to a children's book that uses the preceding word as the main character's name. You must print only one sentence in Korean. The beginning of the sentence starts like an old fairy tale, and the ending of the sentence ends with a '.'. Don't write more than two sentences, just one sentence."
        # 너는 지금부터 어린이 동화작가라는 역할을 맡을거야. 창의적이고 아이들의 정서에 맞는 이야기를 만들어야돼. 앞에 나온 단어를 주인공 이름으로 하는 동화책 도입부의 첫 문장을 만들어줘. 반드시 한글로 한 문장만 출력해야 돼. 문장 앞쪽은 옛날동화처럼 시작하고, 문장 어미는 습니다체로 끝내줘. 두 문장이상 쓰지말고 한문장만 써.
        # 모델 - GPT 3.5 Turbo 선택
        model = "gpt-3.5-turbo"

        # 메시지 설정하기
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": str_prompt}
        ]

        # ChatGPT API 호출하기
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        answer = str(response['choices'][0]['message']['content'])


        if answer:
            print("응답 성공")
            print(answer)
            return JsonResponse({'code': '0000', 'msg': answer}, status=200)
        else:
            print("실패")
            return JsonResponse({'code': '1001', 'msg': '응답실패'}, status=200)