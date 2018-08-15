from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, CreateNewUserForm, SignUpForm
from django.core.exceptions import ObjectDoesNotExist
from .sms import send_message, send_password
from django.utils import timezone
from datetime import timedelta
from datetime import date as mydate
import datetime as dt
import random
import uuid
import pickle
from .alipay import create_direct_pay_by_user, notify_verify, get_old_password_md5_style
from .myDes import encode_des_base64, decode_base64_des
import json


def log(str):
    # trace = trace_code()
    # trace.trace = str
    # trace.when = dt.datetime.now()
    # trace.save()
    pass


# Create your views here.
def index_page(request):
    setattr(request, 'view', 'index_page')
    log("index html")
    return render(request, 'index.html')


def software_page(request):
    setattr(request, 'view', 'software_page')
    css_files = ('lib/css/jquery.fullPage.css', 'lib/css/examples.css',)
    js_files = ('lib/js/jquery.fullpage.js',)
    return render(request, 'software.html', {'css_files': css_files, 'js_files': js_files, })


def login_page(request):
    next = request.GET.get('next', '')
    frm_login = LoginForm()
    frm_create_new_user = CreateNewUserForm()
    return render(request, 'register.html',
                  {'frmLogin': frm_login, 'frmCreate': frm_create_new_user, 'type': 'login', 'next': next})


def create_new_user_page(request):
    frm_login = LoginForm()
    # frm_create_new_user = CreateNewUserForm()
    # frm_create_new_user = SignUpForm()
    # frm_create_new_user = SignUpForm()
    js_files = ('js/script_account.js',)
    return render(request, 'register.html', {'frmLogin': frm_login, 'type': 'create', 'js_files': js_files, })
    # return render(request, 'register.html', {'frmLogin': frm_login, 'frmCreate': frm_create_new_user, 'type': 'create'})


def forget_password_page(request):
    # return HttpResponse("建设中...........")
    js_files = ('js/script_forget.js',)
    return render(request, 'forget.html', {'js_files': js_files, })


def creating_new_user(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password_1']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/main/')
    frm_login = LoginForm()
    js_files = ('js/script_account.js',)
    return render(request, 'register.html', {'frmLogin': frm_login, 'type': 'create', 'js_files': js_files, })


@login_required
def changing_password(request):
    user = request.user
    newpwd = request.POST['password_1']
    user.set_password(newpwd)
    user.save()
    logout(request)
    newuser = authenticate(username=user.username, password=newpwd)
    login(request, newuser)
    return HttpResponseRedirect('/main/')


def reset_password(request):
    mobile = request.POST['mobile']
    try:
        user = User.objects.get(username=mobile)
    except ObjectDoesNotExist:
        return HttpResponse("1")

    message = request.POST["message"]
    sms_All = Sms.objects.filter(mobile=mobile)
    if sms_All.count() <= 0:
        return HttpResponse("2")
    else:
        sms = sms_All[0]
        bDelay = timezone.now() - timedelta(minutes=10) <= sms.sendTime
        if (sms.message == message) and bDelay:

            letters = '0123456789'
            newpwd = ''.join(random.sample(letters, 6))
            user.set_password(newpwd)
            user.save()
            send_password(mobile, newpwd)
            return HttpResponse("0")
        else:
            return HttpResponse("2")


def logining(request):
    url_next = request.GET.get('next', '')
    if request.method == 'POST':
        frm_login = LoginForm(request.POST)
        if frm_login.is_valid():
            register_info = frm_login.cleaned_data
            user_name = register_info['user_name']
            user_pwd = register_info['password']
            user = authenticate(username=user_name, password=user_pwd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if url_next != '':
                        return HttpResponseRedirect(url_next)
                    else:
                        return HttpResponseRedirect('/main/')
                        # return render(request, 'index.html', {})
                        # redirect to main page(not written so far)
    else:
        frm_login = CreateNewUserForm()
    frm_create_new_user = CreateNewUserForm()
    return render(request, 'register.html', {'frmLogin': frm_login, 'frmCreate': frm_create_new_user, 'type': 'login'})


def loging_out(request):
    logout(request)
    return index_page(request)


def tutorial_page(request, tutorialid):
    js_head_files = ('lib/flowplayer/flowplayer.min.js',)
    js_files = ('js/script.js',)
    tutorial = Tutorial.objects.get(id=tutorialid)
    return render(request, 'tutorial.html', {'tutorial': tutorial, 'js_heads': js_head_files, 'js_files': js_files, })


def read_p(request):
    return HttpResponse('read function')


def ccc(request):
    return HttpResponse("建设中...........")


def blog_detail(request, blog_id):
    return HttpResponse("建设中...........")


def blog_list(request, page_num):
    return HttpResponse("建设中...........")


def test_ajax(request):
    return HttpResponse("建设中...........")


def test_param(request, param):
    return HttpResponse("建设中...........")


def can_watch_video(video, user):
    return True


def get_video_url(request):
    v_id = request.POST["VV"]
    try:
        video = Video.objects.get(id=v_id)
        v_url = video.file

    except ObjectDoesNotExist:
        v_url = 'error'
    return HttpResponse(v_url)


def check_sms(request):
    mobile = request.POST["mobile"]
    message = request.POST["message"]
    sms_All = Sms.objects.filter(mobile=mobile)
    if sms_All.count() <= 0:
        return HttpResponse(False)
    else:
        sms = sms_All[0]
        bDelay = timezone.now() - timedelta(minutes=10) <= sms.sendTime
        if (sms.message == message) and bDelay:
            return HttpResponse(True)
        else:
            return HttpResponse(False)


def check_mobile_exists(request):
    mobile = request.POST["mobile"]
    users_count = User.objects.filter(username=mobile).count()
    return HttpResponse(users_count <= 0)


def send_sms(request):
    mobile = request.POST['mobile']
    letters = '0123456789'
    msg = ''.join(random.sample(letters, 4))
    if send_message(mobile, msg):
        sms = Sms(mobile=mobile, message=msg, sendTime=timezone.now())
        sms.save()
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def tutorial_list_page(request, category_id):
    setattr(request, 'view', 'tutorial_list_page')
    js_files = ('js/script_classesList.js',)
    cates = TutorialCategory.objects.all()
    if int(category_id) <= 0:
        tutorials = Tutorial.objects.all()
        setattr(request, 'cate', -1)
    else:
        category = TutorialCategory.objects.get(id=int(category_id))
        tutorials = Tutorial.objects.filter(category=category)
        setattr(request, 'cate', category_id)

    if int(category_id) <= 0:
        return render(request, 'tutorialList.html', {'cates': cates,
                                                     'tutorials': tutorials, })
    else:
        return render(request, 'tutorialList.html',
                      {'cates': cates, 'tutorials': tutorials, 'js_files': js_files,
                       'id_ins': int(category_id), })


def classes_list(request, ins_id, page_num):
    return HttpResponse("建设中...........")


def classes_filter(request, ins_id, cat_id, page_num):
    return HttpResponse("建设中...........")


def shop(request):
    return render(request, 'shop.html')


def shop_s(request):  # 显示商品页面
    return HttpResponse("建设中...........")


@login_required
def profile(request):
    js_files = ('js/script_profile.js',)
    user = request.user
    buys = User_buy.objects.filter(user=user)
    is_buy = len(buys) > 0
    if is_buy:
        buy = buys[0]
    if is_buy:
        return render(request, 'profile.html',
                      {'js_files': js_files, 'register_date': user.date_joined, 'is_buy': is_buy, 'buy': buy, })
    else:
        return render(request, 'profile.html',
                      {'js_files': js_files, 'register_date': user.date_joined, 'is_buy': is_buy, })


@login_required
def buy(request, c_id):
    # user = request.user
    order_id = (str(uuid.uuid1())).replace('-', '')
    id_c = int(c_id)  # 得到商品id
    try:
        commodity = Commodity.objects.get(pk=id_c)
    except ObjectDoesNotExist:
        pass
    if commodity.price <= 0:
        setattr(request, 'view', 'index_page')
        return render(request, 'index.html')

    start = mydate.today()
    user_buy = User_buy()
    user_buy.commodity = commodity
    user_buy.start = start
    user_buy.expire = start + timedelta(days=commodity.days)
    user_buy.user = request.user
    user_buy.price = commodity.price
    user_buy.order_id = order_id
    user_buy.save()
    url = create_direct_pay_by_user(order_id, commodity.title, commodity.description, '', '1.00')
    # url = create_direct_pay_by_user(order_id, commodity.title, commodity.description, '', commodity.price)
    return HttpResponseRedirect(url)


def downloads(request):
    return HttpResponse("建设中...........")


# 确认支付
def pay(request, c_id):
    return HttpResponse("建设中...........")


# alipay异步通知

@csrf_exempt
def alipay_notify_url(request):
    log("alipay notify")
    if request.method == 'POST':
        if notify_verify(request.POST):
            # 商户网站订单号
            tn = request.POST.get('out_trade_no')
            # 支付宝单号
            trade_no = request.POST.get('trade_no')
            # 返回支付状态
            trade_status = request.POST.get('trade_status')

            this_order_list = User_buy.objects.filter(order_id=tn)
            if this_order_list.count() == 1:
                this_order = this_order_list[0]
                this_order.alipay_id = trade_no
                if trade_status == 'TRADE_SUCCESS':
                    this_order.payed = True
                    this_order.save()
                    return HttpResponse("success")
                else:
                    # 写入日志
                    this_order.save()
                    return HttpResponse("success")
            else:
                return HttpResponse("success")
        else:
            # 黑客攻击
            pass
    return HttpResponse("fail")


# 同步通知

def alipay_return_url(request):
    if notify_verify(request.GET):
        tn = request.GET.get('out_trade_no')
        trade_no = request.GET.get('trade_no')
        trade_status = request.GET.get('trade_status')
        this_order_list = User_buy.objects.filter(order_id=tn)
        if this_order_list.count() == 1:
            this_order = this_order_list[0]
            this_order.alipay_id = trade_no
            if trade_status == 'TRADE_SUCCESS':
                this_order.payed = True
            this_order.save()
        return HttpResponseRedirect('/main/')
    else:
        pass
        # 错误或者黑客攻击

        # return HttpResponseRedirect("/")


        # 外部跳转回来的链接session可能丢失，无法再进入系统。


# 客户可能通过xxx.com操作，但是支付宝只能返回www.xxx.com，域名不同，session丢失。
def verify(request, cbid):
    return HttpResponse("建设中...........")


def kota(request):
    p1 = request.GET.get('p1')  # p1是用户名密码
    p2 = request.GET.get('p2')
    key = 'go4succ!'
    temp_str = decode_base64_des(key, p1)
    dic_param = json.loads(temp_str)
    return_param = {}
    letters = [chr(i) for i in range(97, 123)]  # letters =['a','b','c','d',......'z']
    return_param['seed'] = "".join(random.sample(letters, 7))
    return_param['expire'] = '2000-01-01'

    user_name = dic_param['user_name']
    user_pwd = dic_param['password']
    back_key = dic_param['key']
    time_spam = dt.datetime.strptime(dic_param['now'], '%Y%m%d%H%M%S')
    my_now = dt.datetime.now()
    if (my_now - time_spam).days > 5:
        return_param['status'] = 'timeout'
        return_str = encode_des_base64(back_key, json.dumps(return_param))
        return HttpResponse(return_str)
    user = authenticate(username=user_name, password=user_pwd)
    if user is not None:
        if user.is_active:
            return_param['status'] = 'succ'
            this_user = User.objects.get(username=user_name)
            user_buys = User_buy.objects.filter(user=this_user).filter(payed=True).order_by('-expire')
            if user_buys.exists():
                user_buy = user_buys[0]
                return_param['expire'] = user_buy.expire.strftime('%Y-%m-%d')
            else:
                user_buy = User_buy()
                commodity = Commodity.objects.filter(price__lte=0)[0]
                order_id = (str(uuid.uuid1())).replace('-', '')
                start = mydate.today()
                user_buy.commodity = commodity
                user_buy.start = start
                user_buy.expire = start + timedelta(days=commodity.days)
                user_buy.user = user
                user_buy.price = commodity.price
                user_buy.order_id = order_id
                user_buy.save()
                return_param['expire'] = user_buy.expire.strftime('%Y-%m-%d')
        else:
            return_param['status'] = 'fail'
    else:
        return_param['status'] = 'fail'
    return_str = encode_des_base64(back_key, json.dumps(return_param))
    return HttpResponse(return_str)


def get_now(request):
    return HttpResponse(dt.datetime.now().strftime('%Y%m%d%H%M%S'))


def delete_user(request, uname):
    user = User.objects.get(username=uname)
    user.delete()
    return HttpResponse('删除成功')
