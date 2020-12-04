from bs4 import BeautifulSoup as bs #import bs4
import requests # import requests
import os
from win10toast import ToastNotifier

URL = 'https://courseweb.sliit.lk/' # main url
LOGIN_ROUTE = 'login/' # login route
user_data = open("data.dat" , "r")
uname = user_data.readline()
upass = user_data.readline()


#HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.67', 'origin': URL, 'referer': URL + LOGIN_ROUTE}

s = requests.session()


login_payload = {
        'username': uname.rstrip(" ").lstrip(" "),
        'password': upass.rstrip(" ").lstrip(" "), 
        }

login_req = s.post(URL + LOGIN_ROUTE, data=login_payload)

cookies = login_req.cookies

#find all a tags in https://courseweb.sliit.lk/my/
def findUpdatedOnMainPage():
    updates = []
    
    soup = bs(s.get(URL + 'my').text, 'html.parser')

    # spotlite_div = soup.find('div',{"class":"spotlight spotlight-v3"})
    #print(spotlite_div)

    main_div = soup.find('div', {"id":"inst76599"})
    for tag in main_div:
        div_tags = tag.find_all("div" , {'class':"info"})
        for a in div_tags:
            a_tag = a.find('a')
            updates.append(str(a_tag))   
            # secret.write(str(a_tag)+",")

    # stored_data = []
    
    # updates[4] = "asddasdasd asd asd"
    no_updates = True
    secret_read= open("do_not_touch.xyz" , "r")
    stored_data = secret_read.readlines()
    data = []
    for i in stored_data:
        data.append(i.replace("\n" , ""))

    if(data==updates):
        no_updates=True
    else:
        no_updates = False
        secret_write= open("do_not_touch.xyz" , "w")
        for i in updates:
            secret_write.write(str(i)+"\n")
        

    if(no_updates==True):
        toaster = ToastNotifier()
        toaster.show_toast("Course web Updates",
                "There are no latest notices available",
                icon_path=None,
                duration=20,
                threaded=True)
    else:
        toaster = ToastNotifier()
        toaster.show_toast("Course web Updates",
                "There are some latest notices available",
                icon_path=None,
                duration=20,
                threaded=True)


findUpdatedOnMainPage()
