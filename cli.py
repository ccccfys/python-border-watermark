import click
from img import process_images

@click.command()
@click.option('--input', '-i')
@click.option('--output', '-o')
@click.option('--style', '-s')
def main(input, output, style):
    process_images(input, output, style)


if __name__ == "__main__":
    main()