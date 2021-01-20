from decouple import config

# <setWebhook 정의 from https://core.telegram.org/bots/api>
# Use this method to specify a url and receive incoming updates via an outgoing webhook.
# Whenever there is an update for the bot,
# we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update.
# In case of an unsuccessful request, we will give up after a reasonable amount of attempts.
# Returns True on success.

# If you'd like to make sure that the Webhook request comes from Telegram,
# we recommend using a secret path in the URL,
# e.g. https://www.example.com/<token>.
# Since nobody else knows your bot‘s token, you can be pretty sure it’s us.


# <ngrok 사용법>
# ngrok 파일을 Telegram 폴더에 놓는다.
# app.py 서버 실행 중에 터미널 세션 추가 실행
# 터미널에서(ngrok) ngrok http 5000 콘솔 실행
# http://66b14c17.ngrok.io 새롭게 생성 (주의할점 : 8시간 뒤 변경 되니 체크하고 사용해야한다.)


token = config('TOKEN')
api_url = f'https://api.telegram.org/bot{token}'
webhook_url = input()

print(f'{api_url}/setWebhook?url={webhook_url}')


# 터미널 세션(Local(2)) 추가
# 터미널에서 python set_webhook.py 실행하면 아무것도 안뜸 그런 상태에서 아래 url  입력
# ngrok 서버 IP+토큰정보를 터미널에 입력 -> http://66b14c17.ngrok.io/토큰값
# 새롭게 생성된걸 인터넷 창에서 열어보기  https://api.telegram.org/bot토큰값/setWebhook?url=https://66b14c17.ngrok.io/토큰값
# JSON 파일을 확인 할 수 있을 거임(세팅 됨)
