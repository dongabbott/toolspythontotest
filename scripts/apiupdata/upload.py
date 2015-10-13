#-*-coding:utf-8 -*-
__author__ = 'DongJie'
import requests
import glob
import os
import time
import random
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#选择测试（从测试图片目录随机选择多张图片）
def chosePic(number):
    pic_list = glob.glob('E:\\testpic\\*.jpg')
    up_pic = random.sample(pic_list, number)
    return up_pic


#上传测试图片（通过接口将图片上传至服务器,得到服务器返回的路径：http图片上传是以二进制附件流上传到服务器的）
def upPic(pic_list):
    up_url = 'http://test.webapi.yilule.com:5580/api/User?sort=tourDating'
    re = []
    for pic in pic_list:
        f = open(u'%s' % pic, 'rb')
        files = {'file':[os.path.split(pic)[-1], f, 'application/octet-stream']}
        req = requests.post(up_url, files=files)
        server_path = req.json()[0]
        re.append(server_path)
    path = ','.join(re)
    return path


#这是一个应该用接口
def sendYue(account, content, startTime, endTime, lat, lng, address, isNearVisible, picList, contactInformation):
    add = "http://test.webapi.yilule.com:5580/api/TourDating/Publish"
    value = {'accountId':account,
             'content':content,
             'startTime':startTime,
             'endTime':endTime,
             'lat':lat,
             'lng':lng,
             'address':address,
             'isNearVisible':isNearVisible,
             'picList':picList,
             'contactInformation':contactInformation}
    #必须用urlencode将参数值编码
    args = urllib.urlencode(value)
    send_url = add + '?' + args
    try:
        req = requests.post(send_url)
        return req.json()
    except Exception, e:
        print e


if __name__ == "__main__":
    #从account取已经从数据库取出来用户ID数据
    account_list = open('account', 'r').readlines()
    #地置数据（位置名称\t经度\t纬度）当然也可以做成你自己文本格式，容易解析最好
    where = open('coordinate', 'r').readlines()
    position = [x.strip().split('\t') for x in where if x!='']
    content_all = open('content', 'r').read()
    for x in range(180):
        account = account_list[x].strip()
        address = position[x][0]
        lng = position[x][1]
        lat = position[x][2]
        #内容也是从一个文本里面随机（10-140个字）这个根据自己的需要
        content = ''.join(random.sample(content_all.decode('utf-8'), random.randint(10, 140)))
        #下面是我随机开始时间和结束时间的方法（从一个时间戳段中取一个值，然后往后推随机天数）
        t = random.randint(1433541966,1451581261)
        startTime = time.strftime('%Y-%m-%d', time.localtime(t))
        endTime = time.strftime('%Y-%m-%d',time.localtime(t+random.randint(1,60)*86400))
        #这个参数也是一个随机数了
        contactInformation = random.randint(111111,19999999999)
        #0和1随机取一个
        isNearVisible = random.randint(0,1)
        #上传图片返回的路径在这里用到
        picList = upPic(chosePic(random.randint(1,3)))
        #发送请求造数据
        sendYue(account, content, startTime, endTime, lat, lng, address, isNearVisible, picList, contactInformation)

