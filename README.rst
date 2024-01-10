========
Overview
========

An example package. Generated with cookiecutter-pylibrary.

Installation
============

::

    pip install cassandra-sink-connector

Documentation
=============

To use the project:

.. code-block:: python

    import cassandra_sink_connector
    cassandra_sink_connector()

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
