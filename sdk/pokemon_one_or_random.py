from random import randint
from client import PokeAPIClient
import click
from models.generation import Generation
from models.pokemon import Pokemon


@click.command()
@click.option("--pokemon_identifier", default="", prompt="Enter a Pokemon identifier (name or id) or press Enter to get a random Pokemon")
@click.option("--generation_identifier", default="", prompt="Enter a generation id, or press Enter to get a random generation")
def main(pokemon_identifier, generation_identifier):
    pokeclient = PokeAPIClient()

    if pokemon_identifier == "":
        # get random pokemon
        pokemon_identifier = randint(1, 151)
        pokemon: Pokemon = pokeclient.get_pokemon(pokemon_identifier)
        name = pokemon.name
        base_experience = pokemon.base_experience
        species = pokemon.species.get('name')
        print(f"Random Pokemon id {pokemon_identifier}, Pokemon_name: {name}, base_experience: {base_experience}, species: {species}")
    else:
        pokemon: Pokemon = pokeclient.get_pokemon(pokemon_identifier)
        name = pokemon.name
        base_experience = pokemon.base_experience
        species = pokemon.species.get('name')
        print(f"Pokemon name: {name}, base_experience: {base_experience}, species: {species}")
    
    if generation_identifier == "":
        # get random generation 
        generation_identifier = randint(1, 9)
        generation: Generation = pokeclient.get_generation(generation_identifier)
        name = generation.name
        species = generation.pokemon_species
        print(f"Random generation id {generation_identifier}, name: {name}, species: {species}")
    else:
        generation: Generation = pokeclient.get_generation(generation_identifier)
        name = generation.name
        species = generation.pokemon_species
        print(f"Generation name: {name}, pokemon species: {species}")


if __name__ == "__main__":
    main()
