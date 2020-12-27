"""
# This is a simple news app based on web scrapping
# Enter the following keywords as a input to get the letest news of the given keyword.
# The default value of input is Top Stories
# For Example Input : lifestyle


# Key words

1) top-stories
2) People
3) Offbeat
4) Health
5) South
6) Cities
7) India
8) Latest
9) Food
"""

a = """
####################################################
#                                                  #
#           Author : Awaneesh Srivastava          #
#         Creation date : 26th dec, 2020           #
#                                                  #
####################################################

"""
print(a,"\n\n")

import subprocess,sys
def install(package):
    subprocess.call([sys.executable, "-m","pip","--disable-pip-version-chec","-q", "install", package])

install("bs4")
install("requests")

import requests
from bs4 import BeautifulSoup

inp = input("") or "top-stories"
print(((52-len(inp))//2)*" "+(len(inp)+2)*"—")
print(((52-len(inp))//2)*" "+"",inp.upper())
print(((52-len(inp))//2)*" "+(len(inp)+2)*"—")
print("\n\n\n")
print('—'*52+'\n')
link = "https://www.ndtv.com/" + inp
raw = requests.get(link)
bs = BeautifulSoup(raw.text,'html.parser')
a = bs.find_all("div",class_="new_storylising_contentwrap")
count = 1
for i in list(a):
    print(str(count)+")",i.find('h2').find('a').contents[0].strip())
    print('–'*52)
    print(i.find('div',class_='nstory_intro').contents[0])
    print('—'*52+'\n')
    count +=1
    #.find("a").contents[0].strip())
