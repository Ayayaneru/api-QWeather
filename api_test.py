import requests

mykey = '&key=***'
url_api = 'https://devapi.heweather.net/v7/weather/'
api_type = 'now?'
city = 'location=101240101'
# 南昌市


url = url_api + api_type + city + mykey

weather = requests.get(url).json()

now_temp = weather["now"]["temp"]


print(now_temp)
'''
# api_type = 'now?' 时 ， api 返回格式参考如下
{
     'code': '200',
     'updateTime': '2020-10-18T21:00+08:00',
     'fxLink': 'http://hfx.link/36z1',
     'now': 
        {
         'obsTime': '2020-10-18T20:30+08:00', 
         'temp': '15', 
         'feelsLike': '14',
         'icon': '305', 
         'text': '小雨', 
         'wind360': '6', 
         'windDir': '北风', 
         'windScale': '2', 
         'windSpeed': '11', 
         'humidity': '95', 
         'precip': '0.1', 
         'pressure': '1018', 
         'vis': '6',
         'cloud': '100',
         'dew': '14'
        }, 
     'refer': 
        {
         'sources': ['Weather China'],
         'license': ['no commercial use']
        }
}

'''


# to do list ： 得到城市参数 、 明天下雨 、 明天与今天温差过大