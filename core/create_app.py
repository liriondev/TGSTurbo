import requests
from bs4 import BeautifulSoup

class create:
	def __init__(self, number) -> None:
		self.number: str = number
		self.session = requests.Session()
		self.random_hash: str = ''

	def send_code(self) -> None:
		self.random_hash = self.session.post(
					'https://my.telegram.org/auth/send_password',
					data={
							'phone': self.number
						}
				).json()['random_hash']
	
	def login(self, password: str) -> bool:
		
		return self.session.post(
					"https://my.telegram.org/auth/login",
					data={
						"phone": self.number,
						"random_hash": self.random_hash,
						"password": password
					}
				).json()
	
	def get_api(self) -> dict:
		
		data = self.session.get('https://my.telegram.org/apps')
		soup = BeautifulSoup(data.text, features="html.parser")
		
		if "configuration" in soup.title.string:
	
			g_inputs = soup.find_all("span", {"class": "input-xlarge"})
			app_id = g_inputs[0].string
			api_hash = g_inputs[1].string

			return {
				"api_id": app_id,
				"api_hash": api_hash,
				"status": True
				}
		else: 

			hash = soup.find("input", {"name": "hash"}).get("value")
			self.session.post(
				"https://my.telegram.org/apps/create" ,
				data={
					"hash": hash,
					"app_title": "tgsturbo",
					"app_shortname": "tgsturbo",
					"app_url": "",
					"app_platform": "other",
					"app_desc": "The best telegram tools TGSTurbo!"
				}
			)
			
			return {"status": False}

