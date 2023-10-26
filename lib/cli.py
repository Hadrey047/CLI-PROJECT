import click
from dofas_kitchen import users

@click.command()
def cli(Base):
    a = click.prompt("Enter an integer", type=click.INT, default=0)
    b = click.prompt("Enter another integer", type=click.INT, default=0)
    click.echo(f"{a} + {b} = {a + b}")


if __name__ == "__main__":
    cli()


