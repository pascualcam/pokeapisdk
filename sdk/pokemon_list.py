from typing import List
from client import PokeAPIClient
import click
from models.generation import Generation
from models.pokemon import Pokemon
from logger import setup_logger


@click.command()
@click.option("--all_pokemons/--no_pokemons", default=False, prompt="See all pokemons?")
@click.option("--all_gen/--no_gen", default=False, prompt="See all generations?")
def main(all_pokemons: bool, all_gen: bool):
    pokeclient = PokeAPIClient()
    
    try:
        if all_pokemons:
            limit = click.prompt("Select how many Pokemons to display from the top", default=10, type=int)
            logger.info("This may take a while...")
            pokemons: List[Pokemon] = pokeclient.get_pokemons_list()
            logger.info(f"Total number of pokemons: {len(pokemons)}")
            logger.info("List of Pokemons:")
            for pokemon in pokemons[:limit]:
                logger.info(f"  {pokemon.name} (id: {pokemon.id})")

        if all_gen:
            generations: List[Generation] = pokeclient.get_generations_list()
            logger.info(f"Total number of Pokemon generations: {len(generations)}")
            logger.info("List of Pokemon generations:")
            for g in generations:
                logger.info(f"{g.name} (id: {g.id})")
                logger.info(f"  Pokemon species in this generation: {len(g.pokemon_species)}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    logger = setup_logger()
    main()
