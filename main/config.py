__author__ = 'yinmingke'


class settings:
    # 安全检验码，以数字和字母组成的32位字符
    ALIPAY_KEY = 'mbgxj6dtpdk54iv03gxuv21w13lm60ji'

    ALIPAY_INPUT_CHARSET = 'utf-8'

    # 合作身份者ID，以2088开头的16位纯数字
    ALIPAY_PARTNER = '2088521051396655'

    # 签约支付宝账号或卖家支付宝帐户
    ALIPAY_SELLER_EMAIL = '528084147@qq.com'

    ALIPAY_SIGN_TYPE = 'MD5'

    # 付完款后跳转的页面（同步通知） 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
    ALIPAY_RETURN_URL = 'http://www.taobaoican.com/main/payreturn/'

    # 交易过程中服务器异步通知的页面 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
    ALIPAY_NOTIFY_URL = 'http://www.taobaoican.com/main/paynotify/'
    # 收银台页面上，商品展示的超链接。
    ALIPAY_SHOW_URL = ''
