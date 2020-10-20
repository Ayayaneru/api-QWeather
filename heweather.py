#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ayayaneru'

import requests
import time

mykey = '&key=cbe7ec6******************01d0d20'
url_api = 'https://devapi.qweather.com/v7/weather/'
url_api_v2 = 'https://geoapi.qweather.com/v2/city/'


# 城市相关 api 调用 , 默认关键词为北京
def get_location(api_type,city_kw='beijing'):
    # url_v2 = 'https://geoapi.qweather.com/v2/city/lookup?locati
    #           on=101010100&key=cbe7ec6******************01d0d20'
    if api_type == 'top':
        url_v2 = url_api_v2 + api_type + '?range=cn' + mykey
        return requests.get(url_v2).json()
    url_v2 = url_api_v2 + api_type + '?location=' + city_kw + mykey
    return requests.get(url_v2).json()

# 天气相关 api 调用
def get(api_type):
    # url = 'https://devapi.qweather.com/v7/weather/now?locati
    #        on=101240101&key=cbe7ec6******************01d0d20'
    url = url_api + api_type + '?location=' + city_id + mykey
    return requests.get(url).json()


# 传入城市关键字 ， 返回城市代码 , 只返回相关性最强的城市代码
# 例： lookup_city('北京') == '101010100'
# 例： lookup_city('nanchang') == '101240101'
def lookup_city(city_kw):
    city = get_location('lookup',city_kw)['location'][0]
    city_id = city['id']
    city_name = city['name']
    return city_id,city_name

# 热门城市查询
def top_city(range='cn'):
    return get_location('top')['topCityList'][0]['name']

# 得到当前天气各项参数
def now():
    return get('now')['now']
# 得到当前空气温度
def now_temp():
    return get('now')['now']['temp']
# 得到当前体感温度
def now_feelsLike():
    return get('now')['now']['feelsLike']
# 得到当前天气
def now_text():
    return get('now')['now']['text']

# 得到三天的天气
def daily():
    return get('3d')['daily']
    # return get('7d')   可以得到七天的天气

# 得到未来 24 小时天气 ， 开发版 api 貌似此无权限
def hourly():
    return get('24h')

# 这是一个简单的示范 , 可以获取输入城市的气温
if __name__ == '__main__':
    print('请输入城市...')
    city_input = input()
    city_idname = lookup_city(city_input)
    city_id = city_idname[0]
    tommorrow = daily()[1]
    today = daily()[0]
    print(city_idname[1],'现在的气温是：',now_temp(),'℃')
    print(city_idname[1],'明天的天气是：',tommorrow['textDay'],
             tommorrow['tempMin'],'~',tommorrow['tempMax'],'℃')


# 可以在服务器上运行的一点小设想
while True:
    if time.asctime()[11:13] == '22':
        
        # 明天如果有雨晚上十点告诉我
        for rain in tommorrow['textDay']:
            if rain == '雨':
                print('明天有雨，通过邮件或啥的告诉我')
                break # 防止明天是 '暴雨到大暴雨' 两个雨字的天气
            else: # else 其实没啥意义 ， 而且会执行多次 
                print('什么也不干，继续循环')
        
        # 明天与今天温差过大提醒
        if int(tommorrow['tempMax'])-int(today['tempMax'])>5:
            print('明天很热，通过邮件或啥的告诉我')
        if int(today['tempMin'])-int(tommorrow['tempMin'])>5:
            print('明天很冷，通过邮件或啥的告诉我')
    
    time.sleep(3600)

