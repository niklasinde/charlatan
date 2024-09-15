.. _builders:

Builders
========

Builders provide a powerful way to customize getting fixture. You can define
your own builders and provide them as arguments when you instantiate
:py:class:`ciarlare.FixturesManager`.

Example
-------

Here's an example inspired by the schematics library, which expects a dict of
attributes as a single instantiation argument:

.. literalinclude:: ../ciarlare/tests/example/test_custom_builder.py

YAML file:

.. literalinclude:: ../ciarlare/tests/example/data/custom_builder.yaml


API
---

.. automodule:: ciarlare.builder
    :members:
    :undoc-members:
    :special-members: __call__
