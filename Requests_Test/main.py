import requests
import json
 
token = 'ea2cbb7732ca187c434128cc48e58602'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Ponchik",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"

})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1752,
    "name": "Ponchiklol",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "1752"
})

print(response_post.text)

