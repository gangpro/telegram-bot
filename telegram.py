import requests
from decouple import config



def send_message(text):
    token = config('TOKEN')
    api_url = f'https://api.telegram.org/bot{token}'


    # [1]
    # getMe를 통해 접속 체크
    # response = requests.get(api_url + '/getMe').json()
    # print(response)
    # {'ok': True, 'result': {'id': 713810722, 'is_bot': True, 'first_name': 'kangpro', 'username': 'kangpro_bot'}}


    # [2]
    # getUpdates  # chat_id에게 메시지를 보낼 준비하기
    response = requests.get(api_url + '/getUpdates').json()
    chat_id = response['result'][0]['message']['from']['id']
    # print(chat_id)  # 728488945


    # [3]
    # text = '안녕하세요. 또 메시지를 보냅니다 :)'  -> app.py - send_message('곧 점심이네요.')  # 매개 변수매개변수 설정했으므로 주석처리
    # requests.get(api_url + f'/sendMessage?chat_id={chat_id}&text={text}')
    requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')

