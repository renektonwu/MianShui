
import requests
import time
#
# # url='http://2019.ip138.com/ic.asp'
# # url='http://wuguanyu.v4.dailiyun.com/query.txt?key=NP578F8DF1&word=&count=1&rand=false&detail=false'
# url='http://www.cdfgsanya.com/'
proxyaddr = "175.173.222.96"    #代理IP地址
proxyport = 57114               #代理IP端口
proxyusernm = "wuguanyu"        #代理帐号
proxypasswd = "13337677032a"        #代理密码
# #name = input();
# proxyurl="http://"+proxyusernm+":"+proxypasswd+"@"+proxyaddr+":"+"%d"%proxyport
# http://wuguanyu.v4.dailiyun.com/query.txt?key=NP578F8DF1&word=&count=1&rand=false&detail=false
# print(proxyurl)
#
# t1 = time.time()
# r = requests.get(url,proxies={'http':proxyurl,'https':proxyurl},headers={
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding":"gzip, deflate",
#     "Accept-Language":"zh-CN,zh;q=0.9",
#     "Cache-Control":"max-age=0",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
# r.encoding='gb2312'
# # r.encoding='utf-8'
#
# t2 = time.time()
# a = r.text
# print(r.text)
# print("时间差:" , (t2 - t1));


def judge_ip(ip, port):
    # 判断ip是否可用
    # http_url = "http://www.baidu.com"
    http_url = "http://127.0.0.1:8000/polls/"
    proxy_url = "http://{0}:{1}".format(ip, port)
    try:
        proxy_dict = {
            "http": proxy_url,
        }
        response = requests.get(http_url, proxies=proxy_dict)
        a = response.text
        return a
    except Exception as e:
        print("invalid ip and port")
        # self.delete_ip(ip)
        return False
    else:
        code = response.status_code
        if code >= 200 and code < 300:
            print("effective ip")
            return True
        else:
            print(code, "invalid ip and port")
            # self.delete_ip(ip)
            return False

if __name__ == "__main__":
    # get_ip = GetIP()
    # get_ip.get_random_ip()

    ips = ["187.44.1.167"]


    for ip in ips:
        judge_ip(ip,"8080")



