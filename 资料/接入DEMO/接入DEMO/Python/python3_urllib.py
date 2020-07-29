
import urllib.request as urlreq
import time


url='http://2019.ip138.com/ic.asp'
proxyaddr = "代理IP地址"    #代理IP地址
proxyport = 57114               #代理IP端口
proxyusernm = "代理帐号"        #代理帐号
proxypasswd = "代理密码"        #代理密码

proxyurl="http://"+proxyusernm+":"+proxypasswd+"@"+proxyaddr+":"+"%d"%proxyport

ph = urlreq.ProxyHandler({"http": proxyurl, "https": proxyurl})
oper = urlreq.build_opener(ph)

t1 = time.time()

urlreq.install_opener(oper)
res = oper.open(url)

print(res.read().decode("gb2312"))
t2 = time.time()

print("时间差:" , round(t2 - t1, 3));
