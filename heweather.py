#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ayayaneru'

import requests
import time

mykey = '&key=cbe7ec6******************01d0d20'
url_api = 'https://devapi.heweather.net/v7/weather/'
url_api_v2 = 'https://geoapi.qweather.com/v2/city/'


# 城市相关 api 调用
def get_location(api_type,city_kw):
    # url_v2 = 'https://geoapi.qweather.com/v2/city/lookup?locati
    #           on=101010100&key=cbe7ec6******************01d0d20'
    url_v2 = url_api_v2 + api_type + '?location=' + city_kw + mykey
    return requests.get(url_v2).json()

# 天气相关 api 调用
def get(api_type):
    # url = 'https://devapi.heweather.net/v7/weather/now?locati
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


# 这是一个简单的示范 , 可以获取输入城市的气温
if __name__ == '__main__':
    print('请输入城市...')
    city_input = input()
    city_idname = lookup_city(city_input)
    city_id = city_idname[0]
    tommorrow = daily()[1]
    print(city_idname[1],'现在的气温是：',now_temp(),'℃')
    print(city_idname[1],'明天的天气是：',tommorrow['textDay'],
             tommorrow['tempMin'],'~',tommorrow['tempMax'],'℃')


# to do list ：   明天下雨 、 明天与今天温差过大
while True:
    print(time.struct_time)
    time.sleep(3600)

