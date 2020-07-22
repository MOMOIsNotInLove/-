import re

headers_str = """
referer: https://www.zymk.cn/sort/all.html
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
x-requested-with: XMLHttpRequest
"""
pattern = re.compile("^(.*?): (.*)$")
for line in headers_str.splitlines():
    print(re.sub(pattern, "\"\\1\": \"\\2\",", line))
