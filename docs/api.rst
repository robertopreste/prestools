===
API
===

All functionalities of prestools can be accessed after having imported the desired module into Python, as in ``import prestools.bioinf as pb`` and similars. In addition, some functions are also available as Command-Line Interface commands, but this should not be relied on.

Python module functions
=======================

prestools.bioinf
----------------

.. automodule:: prestools.bioinf
    :members:

prestools.clustering
--------------------

.. automodule:: prestools.clustering
    :members:

prestools.graph
---------------

.. automodule:: prestools.graph
    :members:

prestools.misc
--------------

.. automodule:: prestools.misc
    :members:

----

Command Line Interface
======================

prestools bioinf
----------------

.. click:: prestools.commands.bioinf:bioinf
    :prog: bioinf
    :show-nested:

prestools clustering
--------------------

.. click:: prestools.commands.clustering:clustering
    :prog: clustering
    :show-nested:

prestools misc
--------------

.. click:: prestools.commands.misc:misc
    :prog: misc
    :show-nested:
