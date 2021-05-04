from bs4 import BeautifulSoup
from urllib.request import urlopen

soup = BeautifulSoup("<HTML><HEAD><header></HEAD><body></HTML>")

soup2 = BeautifulSoup(urlopen("http://www.networksciencelab.com/"))
