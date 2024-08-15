from random import randint
from client import PokeAPIClient
import click
from models.generation import Generation
from models.pokemon import Pokemon
from logger import setup_logger


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
        species = pokemon.species.name
        logger.info(f"Random Pokemon id {pokemon_identifier}, Pokemon name: {name}, Base Exp: {base_experience}, Species: {species}")
    else:
        pokemon: Pokemon = pokeclient.get_pokemon(pokemon_identifier)
        name = pokemon.name
        base_experience = pokemon.base_experience
        species = pokemon.species.name
        logger.info(f"Pokemon name: {name}, Base Exp: {base_experience}, Species: {species}")
    
    if generation_identifier == "":
        # get random generation 
        generation_identifier = randint(1, 9)
        generation: Generation = pokeclient.get_generation(generation_identifier)
        name = generation.name
        main_region = generation.main_region.name
        species = generation.pokemon_species
        logger.info(f"Random generation id {generation_identifier}, name: {name}, Main Region: {main_region}")
    else:
        generation: Generation = pokeclient.get_generation(generation_identifier)
        name = generation.name
        main_region = generation.main_region.name
        species = generation.pokemon_species
        logger.info(f"Generation name: {name}, Main Region: {main_region}")


if __name__ == "__main__":
    logger = setup_logger()
    main()
