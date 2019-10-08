#%%
import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
html = urlopen(
    "http://localhost:8888/tree"
    ).read().decode("utf-8")
print(html)

#%%
title = re.findall(r"<head>(.*?)</head>", html, flags=re.DOTALL)
print(title)

#%%
ref = re.findall(r'href="(.*?)"', html)
print(ref)

#%%
