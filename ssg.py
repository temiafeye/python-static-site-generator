import typer
from ssg import Site


def main(source="content", dest="dist"):

    config = {
        "source":source, 
        "dest":dest
    }

    Site(**config).build()

if __name__ == "__main__":
    typer.run(main)




