#coding=utf-8

import sys

import requests
import csv

reload(sys)
sys.setdefaultencoding('utf-8')


# You need to register your App first, andenter you API key/secret.
# 您需要先注册一个App，并将得到的API key和API secret写在这里。
API_KEY ='gwFiGs7g2vbYQ1qLcwcdvieaEprbGbCXe'
API_SECRET ='qVGtFiWR2iQG5Wmy9uRrdZgm6PWEijEVU'

import time
from pprint import pformat

import json


#imgurl = 'http://ol6pdll7a.bkt.clouddn.com/x_23.jpg'

def getInfo(imageUrl):

    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'

    data ={
        'api_key':API_KEY,
        'api_secret':API_SECRET,
        'image_url': imageUrl,
        'return_landmark':0,
        'return_attributes':'gender,age'
    }

    content = requests.post(url,data=data).text

    return content


def parae_json(js):
    data = json.loads(js)
    collect = data['faces']

    gender = ''
    age =''

    if collect:
        gender= collect[0]['attributes']['gender']['value']
        age =  collect[0]['attributes']['age']['value']

        print gender
        #save_csv(gender,age)

        # if len(collect)>1:
        #     gender = collect[1]['attributes']['gender']['value']
        #     age = collect[1]['attributes']['age']['value']
        #
        #     print gender
        #     save_csv(gender,age)


    else:
        gender ='no'
        age = 'no'

        print gender

    save_csv(gender,age)


## 这一段需要重写一下，考虑写的效率
def save_csv(gender,age):
    csvfile = file('/Users/apple/Desktop/toimg/a.csv', 'ab+')
    writer = csv.writer(csvfile)
    data = []
    data.append((gender, age))
    writer.writerows(data)
    csvfile.close()



for i in range(1396,1547):`

    image_url = 'http://ol6pdll7a.bkt.clouddn.com/x_%s.jpg'%i

    parae_json(getInfo(image_url))


#'http://ol6pdll7a.bkt.clouddn.com/x_1505.jpg'

#parae_json(getInfo('http://ol6pdll7a.bkt.clouddn.com/x_1505.jpg'))


