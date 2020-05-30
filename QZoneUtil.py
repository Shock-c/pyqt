import hashlib
import json
import traceback
import urllib
from http.cookiejar import CookieJar
from random import random

import cv2
import requests
import re
import base64
import os
import time

from urllib3 import encode_multipart_formdata

HOST = 'https://jiazhang.qq.com/'

def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

def getGTK(skey):
    hash = 5381
    for i in range(0,len(skey)):
        hash += (hash << 5) + utf8_unicode(skey[i])
    return hash & 0x7fffffff

def utf8_unicode(c):
    if len(c)==1:
        return ord(c)
    elif len(c)==2:
        n = (ord(c[0]) & 0x3f) << 6
        n += ord(c[1]) & 0x3f
        return n
    elif len(c)==3:
        n = (ord(c[0]) & 0x1f) << 12
        n += (ord(c[1]) & 0x3f) << 6
        n += ord(c[2]) & 0x3f
        return n
    else:
        n = (ord(c[0]) & 0x0f) << 18
        n += (ord(c[1]) & 0x3f) << 12
        n += (ord(c[2]) & 0x3f) << 6
        n += ord(c[3]) & 0x3f
        return n

class QZoneUtil:
    # __qzone_token = ''
    # __uin = ''
    #
    # __gtk = ''

    def __init__(self, uin, text, proxy=''):
        self.__session = requests.session()
        headers = {
            'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
            'Referer': 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=523005419&style=42&s_url=http://wtlogin.qq.com/&daid=120&pt_no_auth=1'
        }
        self.__session.headers = headers
        self.forward_text = text
        if proxy != '':
            self.__session.proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }

        self.__uin = uin

    def login_with_cookie(self, cookie):
        for k in cookie:
            self.__session.cookies[k] = cookie[k]
        try:
            self.__session.cookies.clear('.qzone.qq.com')
        except:
            pass
        else:
            pass
        skey = self.__session.cookies['p_skey']
        self.__gtk = getGTK(skey)
        try:
            home_page = self.__session.get("https://h5.qzone.qq.com/mqzone/index")
            self.__qzone_token = re.search(r'window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)',
                                       home_page.text)
        except:
            print("代理失败")
            return False
        # print(self.__qzone_token)
        if not self.__qzone_token:
            return False
        self.__qzone_token = self.__qzone_token.group(1)
        self.__qzone_token = self.__qzone_token.strip('"')
        # print(self.__qzone_token)

        skey = self.__session.cookies['p_skey']
        self.__gtk = getGTK(skey)


    def check_user_need_vcode(self, aid, daid):
        qzone_url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?target=self&appid=' + aid + '&daid=' + daid +'&s_url=https://mail.qq.com/cgi-bin/readtemplate?check=false%26t=loginpage_new_jump%26vt=passport%26vm=wpt%26ft=loginpage%26target=&style=25&low_login=1&proxy_url=https://mail.qq.com/proxy.html&need_qr=0&hide_border=1&border_radius=0&self_regurl=http://zc.qq.com/chs/index.html?type=1&app_id=11005?t=regist&pt_feedback_link=http://support.qq.com/discuss/350_1.shtml&css=https://res.mail.qq.com/zh_CN/htmledition/style/ptlogin_input24e6b9.css'
        print (qzone_url)
        resp = self.__session.get(qzone_url)

        self.__session.get("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?target=self&appid=" + aid + "&daid=" + daid + "&s_url=https://mail.qq.com/cgi-bin/readtemplate?check=false%26t=loginpage_new_jump%26vt=passport%26vm=wpt%26ft=loginpage%26target=&style=25&low_login=1&proxy_url=https://mail.qq.com/proxy.html&need_qr=0&hide_border=1&border_radius=0&self_regurl=http://zc.qq.com/chs/index.html?type=1&app_id=11005?t=regist&pt_feedback_link=http://support.qq.com/discuss/350_1.shtml&css=https://res.mail.qq.com/zh_CN/htmledition/style/ptlogin_input24e6b9.css")

        text = resp.text
        js_ver = getmidstring(text, 'ptui_version:encodeURIComponent("', '"')
        print(self.__session.cookies)
        login_sig = self.__session.cookies['pt_login_sig']
        check_param = {
            "regmaster": "",
            "pt_tea": "2",
            'pt_vcode': '1',
            'uin': self.__uin,
            'appid': aid,
            'js_ver': js_ver,
            'js_type': '1',
            'login_sig': login_sig,
            'u1': HOST,
            'r': '0.27872559952975506',
            'pt_uistyle': '25'
        }

        cookie = {}
        for k in self.__session.cookies:
            cookie[k.name] = k.value

        cp = urllib.parse.urlencode(check_param)
        cp = urllib.parse.unquote(cp)
        print(cp)
        resp = self.__session.get('https://ssl.ptlogin2.qq.com/check?' + cp, cookies=cookie)
        print(resp.text)
        cap = re.findall("'(.*?)'", resp.text, re.M)
        print(cap[5])
        return cap[1], cap[5]

    def deal_slider_vcode(self, aid, tk):
        vcode_info = json.dumps({
            'appid': int(aid),
            'capcd': tk,
            'qq': self.__uin
        }, separators=(',', ':'))

        print(vcode_info)
        data = {
            'id': '9878',
            'dev_id': '',
            'token': '5058621957c8a804056f2d43455b7859',
            'type': 'tx_qq',
            'data': vcode_info
        }

        deal_data = urllib.parse.urlencode(data)
        deal_data = urllib.parse.unquote(deal_data)

        print(deal_data)

        str = requests.post('http://www.qieocr.com/qieocr', data=data)
        print(str.text)
        ret_id = json.loads(str.text)
        task_id = ret_id['data']['id']
        print(task_id)
        time.sleep(3)
        data = {
            'uid': '9878',
            'token': '5058621957c8a804056f2d43455b7859',
            'tid': task_id
        }

        resp = requests.post('http://www.qieocr.com/getdata', data=data)
        print(resp.text)
        return json.loads(resp.text)

    def login(self, aid, daid , p, vcode, tick, tk):
        login_sig = self.__session.cookies['pt_login_sig']

        #https://ssl.ptlogin2.qq.com/login?
        # u=66456804
        # &verifycode=@09C
        # &pt_vcode_v1=1
        # &pt_verifysession_v1=t02_mMV10uX-jgCeH8fkHtZBCRclCtmHjRPkmpP234xgVHaO3gDpOFJ3tRrxGhTnoD5qYKZtunWiE9sfGyh4ZJ-m1sWDKvV8b59iLtteKNDqdF774VrVe-Y2g**
        # &p=kToWdZkQZ1Oc2U9Us9TlsRtG*dLe2rUW5*wJe1fLafiOJqB57CDrtEzSnNPj3a7BfNCFo5bcBkfsWrspvO1qPWP3CFMAoEDFvZifNmfdPtMGqqnMcBnEOkePvtTZDxnQCxlF3dSbhD7xORW*P2k7A*z3PubyFu-UhmzSZaWUmIY46jOFZ4StS8rRQFzqj64uv3NGdnorbxvAizaHIRskW380Em2h0nOfIgUq1XrVbymm7M6v6Y3kXZh8omy*pSMpLEAUO6kJ01K3GGwOa90887B6GVHWhaKet7T5LNQbd6cnbsSJe5OQb-sffOcVSsovTx25LJOFWkb6KDjWKbX2Cg__
        # &pt_randsalt=2
        # &u1=https://qzone.qq.com
        # &ptredirect=0
        # &h=1
        # &t=1
        # &g=1
        # &from_ui=1
        # &ptlang=2052
        # &action=8-4-1564394896571
        # &js_ver=19062020
        # &js_type=1
        # &login_sig=8InXwbqkCL3uLAZfManxwh-1MWr4TGgCV758A-puzUUj8v4dayXzcsXVjvyz4H2g
        # &pt_uistyle=25
        # &aid=549000912
        # &daid=5
        # &ptdrvs=uVNsQcZ6mHTjMQb6IPmien3j1P6tYWZ5xZYrbvDP9rDV80b-C17kDkv1hot5-QrYmMe6F0SrTws_&

        login_param = {
            'u': self.__uin,
            "verifycode": vcode,
            'pt_vcode_v1': 1,
            'pt_verifysession_v1': tick,
            'p': p,
            'pt_randsalt': 2,
            'u1': HOST,
            'ptredirect': '0',
            'from_ui': '1',
            'h': '1',
            't': '1',
            'g': '1',
            'ptlang': '2052',
            'action': '8-4-1564394896571',
            'js_ver': '19062020',
            'js_type': '1',
            'login_sig': login_sig,
            'pt_uistyle': 25,
            'aid': aid,
            'daid': daid,
            'ptdrvs': tk
        }


        lp = urllib.parse.urlencode(login_param)
        lp = urllib.parse.unquote(lp)
        url = 'https://ssl.ptlogin2.qq.com/login?' + lp + '&'
        print(url)
        resp = self.__session.get(url)
        print(resp.text)
        cap = re.findall("'(.*?)'", resp.text, re.M)
        url = cap[2]
        print(url)
        pt_sigx = getmidstring(url, 'ptsigx=', '&')

        url = 'https://ptlogin2.qzone.qq.com/check_sig?pttype=1&uin=' + str(self.__uin) + \
              '&service=login&nodirect=0&ptsigx=' + pt_sigx + "&s_url=" + "https://qzs.qq.com" + "&f_url=&ptlang=2052&ptredirect=100" \
              "&aid=" + '549000912' + "&daid=" + '5' + "&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=1&pt_aid=0&pt_" \
                                                "aaid=0&pt_light=0&pt_3rd_aid=0"
        resp = self.__session.get(url, allow_redirects=False)
        print(resp.text)
        print(self.__session.cookies)
        resp = self.__session.get('https://h5.qzone.qq.com/mqzone/index')
        print(self.__session.cookies)
        print(resp.text)
        return


    def login_with_clientkey(self, client_key):
        self.__session.get(
            "https://ui.ptlogin2.qq.com/cgi-bin/login?pt_hide_ad=1&style=9&appid=549000929&pt_no_auth=1&pt_wxtest=1&daid=5&s_url=https%3A%2F%2Fh5.qzone.qq.com%2Fmqzone%2Findex")
        self.__session.cookies["pgv_pvi"] = "4891808758"
        self.__session.cookies["pgv_si"] = "s3110396918"
        login_url = "https://ssl.ptlogin2.qq.com/jump?u1=https%3A%2F%2Fh5.qzone.qq.com%2Fmqzone%2Findex&pt_report=1&daid=5&style=9&pt_ua=30F0FD03C9EEBCDCF868871DF5F9648D&pt_browser=MQQBrowser&keyindex=19&clientuin=" + self.__uin + "&clientkey=" + client_key
        login_result = self.__session.get(login_url)
        home_page = self.__session.get("https://h5.qzone.qq.com/mqzone/index")
        self.__qzone_token = re.search(r'window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)',
                                       home_page.text)
        if not self.__qzone_token:
            return False
        self.__qzone_token = self.__qzone_token.group(1)
        self.__qzone_token = self.__qzone_token.strip('"')

        skey = self.__session.cookies['p_skey']
        self.__gtk = getGTK(skey)
        return True

    def post_shuoshuo(self, con, pic_list):
        reqURL = 'https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6??g_tk={0}&qzonetoken={1}'.format(
            self.__gtk, self.__qzone_token)

        richval = ''

        for i in pic_list:
            richval = richval + i + ' '


        data = (
            ('syn_tweet_verson', '1'),
            ('paramstr', '1'),
            ('pic_template', ''),
            ('richtype', '1' if len(pic_list) > 0 else ''),
            ('richval', pic_list[0]),
            ('special_url', ''),
            ('subrichtype', ''),
            ('who', '1'),
            ('con', con),
            ('ver', '1'),
            ('ugc_right', '1'),
            ('to_sign', '1'),
            ('hostuin', self.__uin),
            ('code_version', '1'),
            ('format', 'fs'),
            ('qzreferrer', 'https://user.qzone.qq.com/' + self.__uin),
        )

        rsp = self.__session.post(reqURL, data=data)
        print(rsp)

    def upload_image(self, path):
        file = open(path, 'rb')
        file_content = file.read()
        file.close()
        base64_pic = base64.urlsafe_b64encode(file_content)

        reqURL = 'https://up.qzone.qq.com/cgi-bin/upload/cgi_upload_image?g_tk={0}&qzonetoken={1}&g_tk={2}'.format(
            self.__gtk, self.__qzone_token, self.__gtk)
        data = (
            ('filename', 'filename'),
            ('uin', self.__uin),
            ('skey', self.__session.cookies.get('skey', domain='/')),
            ('zzpaneluin', self.__uin),
            ('zzpanelkey', ''),
            ('p_uin', self.__uin),
            ('p_skey', self.__session.cookies.get('p_skey')),
            ('qzonetoken', self.__qzone_token),
            ('uploadtype', '1'),
            ('albumtype', '7'),
            ('exttype', '0'),
            ('refer', 'shuoshuo'),
            ('output_type', 'json'),
            ('charset', 'utf-8'),
            ('output_charset', 'utf-8'),
            ('upload_hd', '1'),
            ('hd_width', '2048'),
            ('hd_height', '10000'),
            ('hd_quality', '96'),
            ('backUrls', 'http://upbak.photo.qzone.qq.com/cgi-bin/upload/cgi_upload_image,http://119.147.64.75/cgi-bin/upload/cgi_upload_image'),
            ('url', 'https://up.qzone.qq.com/cgi-bin/upload/cgi_upload_image?g_tk=' + str(self.__gtk)),
            ('base64', '1'),
            ('jsonhtml_callback', 'callback'),
            ('picfile', base64_pic),
            ('qzreferrer', 'https://user.qzone.qq.com/' + self.__uin),
        )

        rsp = self.__session.post(reqURL, data=data)

        if rsp.content == '':
            return ''

        result = rsp.content[10: -3]
        result = json.loads(result)

        if result['ret'] != 0:
            return ''

        img = ',' + result['data']['albumid'] + ',' + result['data']['lloc'] + ',' + result['data']['lloc'] + ',' + str(result['data']['type'])
        img = img + ',' + str(result['data']['height']) + ',' + str(result['data']['width'])
        img = img + ',,' + str(result['data']['height']) + ',' + str(result['data']['width'])

        return img

    def create_album(self, path):
        file = open(path, 'rb')
        file_content = file.read()
        file.close()
        base64_pic = base64.urlsafe_b64encode(file_content)

        reqURL = 'https://up.qzone.qq.com/cgi-bin/upload/cgi_upload_image?g_tk={0}&qzonetoken={1}&g_tk={2}'.format(
            self.__gtk, self.__qzone_token, self.__gtk)
        data = (
            ('inCharset', 'utf-8'),
            ('outCharset', 'utf-8'),
            ('hostUin', self.__uin),
            ('notice', '1'),
            ('callbackFun', '_Callback'),
            ('format', 'fs'),
            ('plat', 'qzone'),
            ('source', 'qzone'),
            ('appid', '4'),
            ('uin', self.__uin),
            ('album_type', ''),
            ('birth_time', ''),
            ('degree_type', ''),
            ('enroll_time', ''),
            ('albumname', 'TEST'),
            ('albumdesc', 'TEST1'),
            ('albumclass', '100'),
            ('priv', '1'),
            ('question', 'question'),
            ('answer', ''),
            ('whiteList', ''),
            ('bitmap', '10000000'),
            ('picfile', base64_pic),
            ('qzreferrer', 'https://user.qzone.qq.com/' + self.__uin),
        )

        rsp = self.__session.post(reqURL, data=data)

        if rsp.content == '':
            return ''

        result = rsp.content[10: -3]
        result = json.loads(result)

        if result['ret'] != 0:
            return ''

        img = ',' + result['data']['albumid'] + ',' + result['data']['lloc'] + ',' + result['data']['lloc'] + ',' + str(result['data']['type'])
        img = img + ',' + str(result['data']['height']) + ',' + str(result['data']['width'])
        img = img + ',,' + str(result['data']['height']) + ',' + str(result['data']['width'])

        return img

    def creat_img(self):
        self.__AlbumName = "travel" + str(int(random()*1000))
        creat_url = "https://user.qzone.qq.com/proxy/domain/photo.qzone.qq.com/cgi-bin/common/cgi_add_album_v2?qzonetoken={0}&g_tk={1}".format(self.__qzone_token, self.__gtk)
        referer = "https%3A%2F%2Fuser.qzone.qq.com%2F{0}%2Fmain".format(self.__uin)
        data = "inCharset=utf-8&outCharset=utf-8&hostUin={0}&notice=0&callbackFun=_Callback&format=fs&plat=qzone&source=qzone&appid=4&uin={0}&album_type=travel&birth_time=&degree_type=0&enroll_time=&albumname={1}&albumdesc=&albumclass=100&priv=3&question=&answer=&whiteList=&bitmap=10000010&qzreferrer={2}".format(self.__uin, self.__AlbumName, referer)
        #       inCharset=utf-8&outCharset=utf-8&hostUin=508868052&notice=0&callbackFun=_Callback&format=fs&plat=qzone&source=qzone&appid=4&uin=508868052&album_type=travel&birth_time=&degree_type=0&enroll_time=&albumname=ds&albumdesc=&albumclass=100&priv=3&question=&answer=&whiteList=&bitmap=10000010&qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2F508868052%2F4
        self.__session.headers["Referer"] = referer
        self.__session.headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"

        # print("cookie", self.__session.cookies)
        # print("url", creat_url)
        # print("data", data)

        i = 0
        response = None
        while i <= 3:
            try:
                response = self.__session.post(creat_url, data=data)
                # print(response)
                if response.status_code != 200:
                    print("response.status_code != 200", response.text)
                    return False
                break
            except Exception as e:
                # print('代理访问频繁')
                i += 1
                time.sleep(10)
            # print(traceback.print_exc())

        # print(response.text)
        msgParam = r'\"message\":\"(.+?)\"'
        msg = re.search(msgParam, response.text)
        # print(msg)
        if msg != None:
            print(msg.group(1) + " -- "+str(self.__uin))
            return False
        param = r'\"id\" : \"(.+?)\"'
        id = re.search(param, response.text)
        # print(id)
        if id != None :
            id = id.groups(1)
            self.__albumId = id[0]
            return True

        return False

    def set_img_pri(self):
        set_img_url = "https://user.qzone.qq.com/proxy/domain/photo.qzone.qq.com/cgi-bin/common/cgi_modify_album_v2?g_tk={0}".format(self.__gtk)
        referer = "https://user.qzone.qq.com/proxy/domain/qzs.qq.com/qzone/photo/v7/page/photo.html"
        data = "uin={0}&albumId={1}&nvip=1&type=4&priv=1&pypriv=undefined&question=&answer=&bitmap=10000000&whiteList=&appid=4&notice=0&hostUin={0}&plat=qzone&source=qzone&inCharset=utf-8&outCharset=utf-8&qzreferrer={2}".format(self.__uin, self.__albumId, referer)
        self.__session.headers["Referer"] = referer
        self.__session.headers["Content-Type"] = "application/json"
        time.sleep(5)
        i = 0
        while i <= 3:
            try:
                rsp = self.__session.post(set_img_url, data=data)
                break
            except Exception as e:
                # print("代理频繁")
                time.sleep(10)
                i += 1
        # print(rsp.text)


    def upload_img(self):

        pic = open("vc1.png", "rb").read()
        pic_len = len(pic)
        pic_num = pic_len / 16384
        offset = 0
        seq = 0
        end = 16384
        file_path = 'vc1.png'
        pic_md5 = self.get_md5(file_path)

        time_str = time.strftime("%Y/%m/%d 上午%H:%M:%S", time.localtime())
        log_data = "[{\"time\":\"" + time_str + "\",\"log\":\"upload\"},{\"time\":\"" + time_str + "\",\"log\":\"encrypt\"},{\"time\":\"" + time_str + "\",\"log\":\"[encrypt] cal hash by webworker, file size " + str(pic_len) + "\"},{\"time\":\"" + time_str + "\",\"log\":\"encrypt hash " + pic_md5 + "\"},{\"time\":\"" + time_str + "\",\"log\":\"controlPacker request\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"[encrypt] cal hash cost 18, file size " + str(pic_len) + "\"},{\"time\":\"" + time_str + "\",\"log\":\"controlPacker done\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData\"},{\"time\":\"" + time_str + "\",\"log\":\"websocket send start\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData done ret: 0\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData done ret: 0\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData done ret: 0\"},{\"time\":\"" + time_str + "\",\"log\":\"upload fragment uploadData done ret: 0\"}]"
        log_url = "https://h5.qzone.qq.com/log/post/uploaderWebApp"
        self.__session.headers["Content-Type"] = "application/json"
        self.__session.headers[
            "Referer"] = "https://user.qzone.qq.com/proxy/domain/qzs.qq.com/qzone/photo/v7/page/upload.html"
        try:
            log_rsp = self.__session.post(log_url, data=log_data)
            print(log_rsp.text)
            time.sleep(1)
        except:
            pass


        iBatchID = int(time.time() * 1000000)
        img = cv2.imread('vc1.png')
        sp = img.shape
        width = sp[1]
        high = sp[0]
        data = json.dumps({"control_req": [
            {"uin": str(self.__uin), "token": {"type": 4, "data": self.__session.cookies["p_skey"], "appid": 5},
             "appid": "pic_qzone", "checksum": pic_md5, "check_type": 0, "file_len": pic_len,
             "env": {"refer": "qzone", "deviceInfo": "h5"}, "model": 0,
             "biz_req": {"sPicTitle": "1000369", "sPicDesc": "", "sAlbumName": self.__AlbumName, "sAlbumID": self.__albumId,
                         "iAlbumTypeID": 0, "iBitmap": 0, "iUploadType": 0, "iUpPicType": 0, "iBatchID": iBatchID,
                         "sPicPath": "", "iPicWidth": width, "iPicHight": high, "iWaterType": 0, "iDistinctUse": 0,
                         "iNeedFeeds": 1, "iUploadTime": int(time.time()), "mapExt": "null", "sExif_CameraMaker": "",
                         "sExif_CameraModel": "", "sExif_Time": "", "sExif_LatitudeRef": "", "sExif_Latitude": "",
                         "sExif_LongitudeRef": "", "sExif_Longitude": ""}, "session": "", "asy_upload": 0,
             "cmd": "FileUpload"}]})
        session_url = "https://h5.qzone.qq.com/webapp/json/sliceUpload/FileBatchControl/{0}?g_tk={1}".format(pic_md5, self.__gtk)
        self.__session.headers["Content-Type"] = "application/json"
        self.__session.headers["Referer"] = "https://user.qzone.qq.com/proxy/domain/qzs.qq.com/qzone/photo/v7/page/upload.html"
        ret = self.__session.post(session_url, data=data)
        # print("rsp status", ret.status_code)
        try:
            session_json = json.loads(ret.text)
        except:
            return False
        # print(type(session_json))
        session = session_json["data"]["session"]
        self.__session.headers[
            "Content-Type"] = "multipart/form-data; " "boundary=----WebKitFormBoundarya2hxB7cvYGQA5ov1"
        pic_json = ""

        while pic_num > 0 :
            pic_num -= 1
            slice_file = pic[offset:end]
            data = {
                "uin": self.__uin,
                "appid": "pic_qzone",
                "session": session,
                "offset": offset,
                "data": ("blob", slice_file, "application/octet-stream"),
                "checksum": "",
                "check_type": "0",
                "retry": "0",
                "seq": seq,
                "end": end,
                "cmd": "FileUpload",
                "slice_size": "16384",
                "biz_req.iUploadType": "0"
            }

            upload_url = "https://h5.qzone.qq.com/webapp/json/sliceUpload/FileUpload?seq={0}&retry=0&offset={1}&end={2}&total={3}&g_tk={4}".format(seq, offset, end, pic_len, self.__gtk)

            m = encode_multipart_formdata(data, boundary="----WebKitFormBoundarya2hxB7cvYGQA5ov1")
            try:
                response = self.__session.post(upload_url, data=m[0])
            except:
                print('代理异常')
                return False
            # print(response.text)
            try:
                pic_json = json.loads(response.text)
            except:
                return False
            seq += 1
            offset += 16384
            end += 16384


        if pic_json == "" or pic_json == None:
            return False
        sAlbumID = pic_json["data"]["biz"]["sAlbumID"]
        sPhotoID = pic_json["data"]["biz"]["sPhotoID"]
        desc_forward = "https://user.qzone.qq.com/{0}/infocenter".format(self.__uin)
        desc_url = "https://user.qzone.qq.com/proxy/domain/photo.qzone.qq.com/cgi-bin/common/cgi_modify_multipic_v2?qzonetoken={0}&g_tk={1}".format(self.__qzone_token, self.__gtk)
        desc_data = "inCharset=utf-8&outCharset=utf-8&hostUin={0}&notice=0&callbackFun=_Callback&format=fs&plat=qzone&source=qzone&appid=4&uin={0}&albumId={1}&nvip=1&pub=0&albumTitle=ds&albumDesc=&picCount=1&priv=3&afterUpload=1&total=1&modifyType=1&type=010&name=&desc={2}&tag=&codeList={3}&qzreferrer={4}".format(
            self.__uin, sAlbumID, self.forward_text, sPhotoID+"?010??"+self.forward_text+"??", desc_forward).encode('utf-8')
        self.__session.headers["Referer"] = desc_forward
        self.__session.headers[
            "Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        time.sleep(2)
        try:
            desc_rsp = self.__session.post(desc_url, data=desc_data)
        except:
            pass

        self.set_img_pri()
        forward_url = "https://user.qzone.qq.com/p/h5/pc/api/sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_save?qzonetoken={0}&g_tk={1}".format(self.__qzone_token, self.__gtk)
        forward_referer = "https://user.qzone.qq.com/{0}/infocenter?via=toolbar".format(self.__uin)
        self.__session.headers["Referer"] = forward_referer
        self.__session.headers[
            "Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"

        forward_data = "notice=1&fupdate=1&platform=qzone&token={0}&auto=0&type=picture&description={1}&share2weibo=0&onekey=0&comment=0&format=fs&spaceuin={2}&id={3}&reshare=0&batchid=&sendparam=&entryuin={2}&qzreferrer={4}".format(
            self.__gtk, self.forward_text, self.__uin, sAlbumID+":"+sPhotoID, forward_referer).encode('utf-8')
        time.sleep(4)
        forward_rsp = self.__session.post(forward_url, data=forward_data)
        # print(forward_rsp.text)

        return True



    def get_md5(self, file_path):
        md5 = None
        if os.path.isfile(file_path):
            f = open(file_path, 'rb')
            md5_obj = hashlib.md5()
            md5_obj.update(f.read())
            hash_code = md5_obj.hexdigest()
            f.close()
            md5 = str(hash_code).lower()
        return md5

    def inquire_img(self):

        try:
            url = "https://user.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/fcg_list_album_v3?g_tk={0}&callback=shine0_Callback&t=517880052&hostUin={1}&uin={1}&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&format=jsonp&notice=0&filter=1&handset=4&pageNumModeSort=40&pageNumModeClass=15&needUserInfo=1&idcNum=4&callbackFun=shine0&_={2}".format(
                self.__gtk, self.__uin, int(time.time()))
            self.__session.headers["Referer"] = "https://user.qzone.qq.com/proxy/domain/qzs.qq.com/qzone/photo/v7/page/photo.html?init=photo.v7/module/albumList/index&navBar=1&g_iframeUser=1&g_iframedescend=1"
            response = self.__session.get(url)
            # print("查询：",response.status_code, response.text)
            msgParam = r'\"message\":\"(.+?)\"'
            msg = re.search(msgParam, response.text)
            # print(msg)
            if msg != None:
                print(msg.group(1) + " -- "+str(self.__uin))
                return False
            id_param = r'\"id\" : \"(.+?)\"'
            id = re.search(id_param, response.text)
            name_param = r'\"name\" : \"(.+?)\"'
            name = re.search(name_param, response.text)
            # print("查询：", id, name)
            if id != None and name != None:
                id = id.groups(1)
                name = name.groups(1)
                self.__albumId = id[0]
                self.__AlbumName = name[0]
                return True
            return False
        except:
            return False
