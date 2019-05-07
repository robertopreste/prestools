#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import prestools.graph as pg


@click.group()
def graph():
    """
    Plotting utilities
    """
    pass


@graph.command()
@click.option("--save", "-s", default=False,
              help="""If a path/filename is provided, the image
    will be saved to the given destination; otherwise, a random name will
    be created, taking care that no other files with the same name are
    present (default: False)""")
def random_image(save):
    """Retrieve a random image from the web.

    Retrieve and save a random image from the web, using the service
    provided by Picsum. The downloaded image can be opened using
    IPython.display.Image().
    """
    pg.random_image(save)
    click.echo("Done.")
