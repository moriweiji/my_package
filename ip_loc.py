#/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import json



def get_state(ip,w_ch,w_us):
    if ':' in ip:
        ip_source = ip.split(':')[0]
        url = 'http://freegeoip.net/json/%s' % ip_source
    else:
        url = 'http://freegeoip.net/json/%s' % ip
    content = requests.get(url).text
    ip_status = json.loads(content)
    print ip,ip_status.get('country_name')
    if ip_status.get('country_name') == 'China':
        w_ch.write('%s\n' % ip)
    else:
        w_us.write('%s\n' % ip)


def ip_list_open(file):
    with open(file,'r') as f:
        return [i.strip() for i in f.readlines()]



if __name__ == '__main__':
    for ip in ip_list_open('ip.txt'):
        with open('.\\result\\us_ip.txt', 'w') as w_us:
            with open(r'.\\result\\ch_ip.txt', 'w') as w_ch:
                get_state(ip,w_ch,w_us)