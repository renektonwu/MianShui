import requests
import sys
reload(sys)
sys.setdefaultencoding("gb2312")


url='http://2019.ip138.com/ic.asp'
proxyaddr = "代理IP地址"    #代理IP地址
proxyport = 57114               #代理IP端口
proxyusernm = "代理帐号"        #代理帐号
proxypasswd = "代理密码"        #代理密码

proxyurl="http://"+proxyusernm+":"+proxypasswd+"@"+proxyaddr+":"+"%d"%proxyport

try:
    r = requests.get(url,proxies={'http':proxyurl,'https':proxyurl},headers={
        "User-Agent":"curl/0.7.6"})
    r.encoding='gb2312'
    print(r.text)

except IOError, e:
    print ''

