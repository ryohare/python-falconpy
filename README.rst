========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |
        | |codecov|
    * - package
      - | |commits-since|

.. |codecov| image:: https://codecov.io/gh/ryohare/python-falconpy/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ryohare/python-falconpy

.. |commits-since| image:: https://img.shields.io/github/commits-since/ryohare/python-falconpy/v1.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ryohare/python-falconpy/compare/v0.0.0...master



.. end-badges

Crowdstrike Falcon API

* Free software: BSD 2-Clause License

Installation
============

::

    pip install falconpy

You can also install the in-development version with::

    pip install https://github.com/ryohare/python-falconpy/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import falconpy
    falconpy.longest()


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
