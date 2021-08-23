import urllib.request
try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except:
    print("\033[1;31m🤔🤔🤔Site não Acessivél🤔🤔🤔\033[m")
else:
    print("\033[1;32m🤔🤔🤔Site Acessivél🤔🤔🤔\033[m")
