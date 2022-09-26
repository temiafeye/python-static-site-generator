import typer
from ssg import site


def main(source="content", dest="dist"):

    config = {
        "source":source, 
        "dest":dest
    }

    site = site.Site(**config)
    site.build()

if __name__ == "__main__":
    typer.run(main)




