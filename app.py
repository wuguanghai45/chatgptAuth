from flask import Flask, request, jsonify
from DrissionPage import ChromiumPage, ChromiumOptions
import time
import json


print("start_server")
app = Flask(__name__)

def get_access_token(username, password):
    co = ChromiumOptions()
    co.auto_port(True)
    co.set_argument('--no-sandbox')

    # 用 d 模式创建页面对象（默认模式）
    page = ChromiumPage(co)

    # 跳转到登录页面
    page.get('https://chat.openai.com/auth/login')
    # page.wait.load_start()
    print("page loaded")

    page.ele('@data-testid=login-button').click()

    while True:
        print(page.ele('#username'))
        if page.ele('#username'):
            break
        time.sleep(0.1)

    page.ele('#username').input(username)
    page.ele('@data-action-button-primary=true').click()

    page.wait.load_start()

    while True:
        print(page.ele('#password'))
        if page.ele('#password'):
            break
        time.sleep(0.1)

    page.ele('#password').input(password)

    print(page.ele('@data-action-button-primary=true'))
    print(page.url)

    print("loaded")
    page.ele('@data-action-button-primary=true').click()

    page.wait.load_start()

    page.listen.start('https://chat.openai.com/api/auth/session')

    print(page.url)

    while True:
        if page.url == 'https://chat.openai.com/':
            break
        if not page.is_loading:
            page.ele('@data-action-button-primary=true').click()
        time.sleep(0.1)

    res = page.listen.wait()
    print(res.response.body)
    access_token = res.response.body["accessToken"]
    page.quit()
    return access_token

@app.route('/get_chatgpt_access_token', methods=['POST'])
def get_chatgpt_access_token():
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        access_token = get_access_token(username, password)
        res_data = {
            'access_token': access_token
        }
        return jsonify(res_data)
    except Exception as e:
        print(e)
        return jsonify({'access_token': None})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3010)