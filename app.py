import requests

def pobierz_kod():
	return requests.get("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json").json()

def pobierz_dane():
	if pobierz_kod() == 200:
		return requests.get("https://mdn.github.io/learnin-area/javascript/oojs/json/superheroes.json").json()
	else:
		return None

if __name__ == "__main__":
	print(pobierz_dane())
