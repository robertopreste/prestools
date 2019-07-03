#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click
from prestools.commands.bioinf import bioinf
from prestools.commands.clustering import clustering
from prestools.commands.graph import graph
from prestools.commands.misc import misc
from prestools.commands.learn import learn


# Custom group class to better handle all the exceptions raised
class HandleExceptions(click.Group):
    def __call__(self, *args, **kwargs):
        try:
            return self.main(*args, **kwargs)
        except Exception as e:
            click.echo("ERROR!\n{}".format(e))


@click.group(cls=HandleExceptions)
@click.version_option()
def main():
    """
    Main command line entry point for prestools.
    """
    pass


main.add_command(bioinf)
main.add_command(clustering)
main.add_command(graph)
main.add_command(misc)
main.add_command(learn)


if __name__ == "__main__":
    sys.exit(main())
