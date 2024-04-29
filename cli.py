import click
from img import process_images

@click.command()
@click.option('--input', '-i')
@click.option('--output', '-o')
@click.option('--style', '-s')
@click.option('--author', '-a')
@click.option('--quality', '-q')
def main(input, output, style, author, quality):
    process_images(input, output, style, author, quality)


if __name__ == "__main__":
    main()