from random import randint
from client import PokeAPIClient

def main():
    client = PokeAPIClient()
    
    pokemon_identifier = input("Enter a Pokemon identifier (name or id): ")
    pokemon_data = client.get_pokemon(pokemon_identifier)
    pokemon_name = pokemon_data.name
    pokemon_base_experience = pokemon_data.base_experience
    print(f"Pokemon id {pokemon_identifier}:", f"pokemon_name: {pokemon_name}, base_experience: {pokemon_base_experience}")

    # get random generation 
    random_id = randint(1, 9)
    generation_id = random_id
    generation_data = client.get_generation(generation_id)
    generation_name = generation_data.name
    print("Random generation name:", generation_name)


if __name__ == "__main__":
    main()
