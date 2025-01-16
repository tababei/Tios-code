#from code1 import Stiffener
from urllib.request import urlopen

page = urlopen("https://www.scrapethissite.com")
https = page.read.decode("utf-8")

print(https)

#s1 = Stiffener(50, 5, 2000, 780)

