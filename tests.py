import requests
 
def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        return joke['value']
    else:
        return "Não foi possível obter uma piada. Por favor, tente novamente mais tarde."
 
if __name__ == "__main__":
    joke = get_random_joke()
    print(joke)