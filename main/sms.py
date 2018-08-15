import requests


def send_message(mobile, message):
    str1 = '您的验证码是：'
    str2 = ',打死都不要告诉别人哦。10分钟内有效。'
    strSign = '【iCan培训】'
    msg = str1 + message + str2 + strSign
    resp = requests.post("http://sms-api.luosimao.com/v1/send.json",
                         auth=('api', '6214cf92973a1eef919fca057c0b15b5'),
                         data={
                             "mobile": mobile,
                             "message": msg,
                         }, timeout=3, verify=False)
    result = eval(bytes.decode(resp.content))
    return result['error'] == 0


def send_password(mobile, message):
    str1 = '您的新密码是：'
    str2 = '，请尽快登录并且修改您的密码。'
    strSign = '【iCan培训】'
    msg = str1 + message + str2 + strSign
    resp = requests.post("http://sms-api.luosimao.com/v1/send.json",
                         auth=('api', '6214cf92973a1eef919fca057c0b15b5'),
                         data={
                             "mobile": mobile,
                             "message": msg,
                         }, timeout=3, verify=False)
    result = eval(bytes.decode(resp.content))
    return result['error'] == 0


if __name__ == "__main__":
    message = '9999'
    if send_message('18621667160', message):
        print('ok')
