import urllib2

proxyaddr = "代理IP地址"    #代理IP地址
proxyport = 57114               #代理IP端口
proxyusernm = "代理帐号"        #代理帐号
proxypasswd = "代理密码"        #代理密码


proxyurl="http://"+proxyusernm+":"+proxypasswd+"@"+proxyaddr+":"+"%d"%proxyport
proxy=urllib2.ProxyHandler({"http":proxyurl,"https":proxyurl})
opener=urllib2.build_opener(proxy)
urllib2.install_opener(opener)

try:
    response = urllib2.urlopen("http://2019.ip138.com/ic.asp")
    print response.read()
except  urllib2.HTTPError, e:
    print e.code
