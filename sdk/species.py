import click
from client import PokeAPIClient
import logger


@click.command()
@click.option("--generation_id", prompt="Enter a generation name or id", required=True, type=int)
def main(generation_id):
    pokeclient = PokeAPIClient()
    generation_id = pokeclient.get_generation(generation_id).name
    species_names = pokeclient.get_species_by_generation(generation_id)
    
    logger.info(f"New species introduced in {generation_id}: {len(species_names)}")
    for name in species_names:    
        logger.info(f"  {name}")


if __name__ == "__main__":
    logger = logger.setup_logger()
    main()
