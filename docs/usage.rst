=====
Usage
=====

To use prestools in a project::

    import prestools

``prestools`` include several different modules, each one specifically suited for one particular topic or task (bioinformatics, plotting, etc.).
It is recommended that you only import the required module, as follows::

    import prestools.bioinf as pb       # bioinformatics utilities
    import prestools.clustering as pc   # clustering utilities
    import prestools.graph as pg        # plotting utilities
    import prestools.misc as pm         # miscellaneous

Some functions are also available as CLI commands, and can be used as follows::

    prestools bioinf [command] [options]
    prestools clustering [command] [options]
    prestools misc [command] [options]

Please refer to the API_ page for more information.

.. _API: https://prestools.readthedocs.io/en/latest/api.html
