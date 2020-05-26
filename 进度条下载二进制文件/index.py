# -*- coding:utf-8 -*-
import requests
import sys


url ="https://vdept.bdstatic.com/6b4976384e4e6d5163693837704b3859/52324b7279764e67/2405e65fad99a55c7d8cc807c90db8c881b8b30c7e6d2576924bd9d1298e0327440bf7e1e0abcf3f29bd95ae83c027d2.mp4?auth_key=1589968650-0-0-48d66b8acf9b451911f7b042d976f59a"
rsp = requests.head(url)
# 获取返回文件的大小
size = rsp.headers['Content-Length']
# 将字节Byte转换为MB
print("文件大小: %.2f MB" % (int(size)/1024/1024))
p = 0
rp = requests.get(url, stream=True)
with open('video.mp4', 'wb') as f:
    # 开始下载每次请求1024字节
    for i in rp.iter_content(chunk_size=1024):
        p += len(i)
        f.write(i)
        done = 50 * p / int(size)
        sys.stdout.write("\r[%s%s] %.2f%%" % ('█' * int(done), '' * int(50 - done), done+done))
    sys.stdout.flush()
print("\nOK")

