=======
History
=======

0.1.0 (2019-03-07)
==================

* First development release.

0.1.1 (2019-03-14)
------------------

* Add functions for clustering data.

0.1.2 (2019-03-15)
------------------

* Add ``hamming_distance()`` and ``mutate_sequence()`` functions in ``prestools.bioinf`` and related tests;
* Clean code style.

0.1.3 (2019-03-19)
------------------

* Add command line interface commands and related tests for ``bioinf`` and ``misc`` modules;
* Add ``filter_type()`` function in ``prestools.misc`` and related tests;
* Clean code style.

0.1.4 (2019-03-23)
------------------

* Add ``wordcount()`` function in ``prestools.misc`` and related tests.

0.1.5 (2019-04-05)
------------------

* Add ``equal_files()`` function in ``prestools.misc`` and related tests;
* Update docstrings.

0.1.6 (2019-04-11)
------------------

* Add ``random_image()`` function and CLI in ``prestools.plotting``.

0.1.7 (2019-04-20)
------------------

* Add ``benchmark()`` function in ``prestools.misc`` and related tests.

0.1.8 (2019-04-26)
------------------

* Change ``pm.benchmark()`` function to a decorator;
* Add several distance calculation functions to ``prestools.bioinf`` and related tests;
* Reformat code in ``prestools.bioinf``.

0.1.9 (2019-04-27)
------------------

* Add distance functions to ``bioinf`` CLI command and related tests.

0.1.10 (2019-05-06)
-------------------

* Change ``plotting`` library name to ``graph`` (to avoid alias conflict with pandas_profiling).

0.1.11 (2019-05-07)
-------------------

* Fix docstrings and type hints;
* Update documentation.

0.1.12 (2019-05-08)
-------------------

* Add ``apply_parallel`` function to ``prestools.misc``.

0.1.13 (2019-06-22)
-------------------

* Add short version arguments to ``reverse_complement`` bioinf function.

0.1.14 (2019-07-03)
-------------------

* Add ``learn`` module and related tests;
* Remove ``random_image`` from ``graph`` module;
* Clean code.

0.2.0 (2019-08-14)
==================

* Add ``rpkm`` and ``quantile_norm`` functions to ``prestools.bioinf``;
* Add ``reduce_xaxis_ticks`` and ``reduce_yaxis_ticks`` functions to ``prestools.graph``;
* Move ``flatten_image`` to ``prestools.graph``;
* Remove ``prestools.learn``;
* Update related tests;
* Fix documentation and API.

0.2.1 (2019-09-07)
------------------

* Add ``plot_confusion_matrix`` to ``prestools.graph``;
* Add related tests;
* Drop support for Python < 3.6;
* Update requirements;
* Update documentation.
