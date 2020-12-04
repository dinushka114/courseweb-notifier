from bs4 import BeautifulSoup as bs #import bs4
import requests # import requests
import os

URL = 'https://courseweb.sliit.lk/' # main url
LOGIN_ROUTE = 'login/' # login route
secret = open("do_not_touch.xyz" , "a+")
user_data = open("data.dat" , "w")

print(

    """
            


                                                                                        
             ██████   █████           █████     ███     ██████   ███                    
            ░░██████ ░░███           ░░███     ░░░     ███░░███ ░░░                     
             ░███░███ ░███   ██████  ███████   ████   ░███ ░░░  ████   ██████  ████████ 
             ░███░░███░███  ███░░███░░░███░   ░░███  ███████   ░░███  ███░░███░░███░░███
             ░███ ░░██████ ░███ ░███  ░███     ░███ ░░░███░     ░███ ░███████  ░███ ░░░ 
             ░███  ░░█████ ░███ ░███  ░███ ███ ░███   ░███      ░███ ░███░░░   ░███     
             █████  ░░█████░░██████   ░░█████  █████  █████     █████░░██████  █████    
            ░░░░░    ░░░░░  ░░░░░░     ░░░░░  ░░░░░  ░░░░░     ░░░░░  ░░░░░░  ░░░░░     
                                                                            
                                                                            
                                                                            
    """

    )

username = input("Enter username for log courseweb: ")
password = input("Enter password for log couresweb: ")

user_data.write(str(username)+"\n")
user_data.write(str(password))


#HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.67', 'origin': URL, 'referer': URL + LOGIN_ROUTE}

s = requests.session()


login_payload = {
        'username': username.rstrip(" ").lstrip(" "),
        'password': password.rstrip(" ").lstrip(" "), 
        }

login_req = s.post(URL + LOGIN_ROUTE, data=login_payload)

cookies = login_req.cookies

def findUpdatedOnMainPage():
    updates = []
    
    soup = bs(s.get(URL + 'my').text, 'html.parser')

    main_div = soup.find('div', {"id":"inst76599"})
    for tag in main_div:
        div_tags = tag.find_all("div" , {'class':"info"})
        for a in div_tags:
            a_tag = a.find('a')
            updates.append(a_tag)   
            secret.write(str(a_tag)+"\n")

findUpdatedOnMainPage()
