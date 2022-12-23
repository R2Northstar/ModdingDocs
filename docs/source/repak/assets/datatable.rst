Datatables - TODO
^^^^^^^^^^^^^^^^^

Examples:
=========

Asset Structure:
================

``$type``
---------

For an asset to be a datatable asset, the ``$type`` field must be ``"dtbl"``.

``path``
--------

The ``path`` field of a datatable asset is used to determine the location in the RPak's ``assetsDir`` that the ``.csv`` file is in.

.. warning::
    If the .csv file has no columns, RePak will output the following warning to the console, before skipping the asset.
    ``Attempted to add dtbl asset with no columns. Skipping asset...``

.. warning::
    If the .csv file has fewer than 2 rows, RePak will output the following warning to the console, before skipping the asset.
    ``Attempted to add dtbl asset with invalid row count. Skipping asset...
    DTBL    - CSV must have a row of column types at the end of the table``