Creating RPak Mods using RePak
==============================

RPak mods can be used for the following:

* Custom UI
* Skins
* World Materials
* Texture replacements

RePak First-Time Setup
^^^^^^^^^^^^^^^^^^^^^^

The lastest RePak release can be downloaded from `here <https://github.com/r-ex/RePak/releases>`_.
Once it has been downloaded, it is recommended to set up your file structure as follows:

.. note::

    Depending on the version of RePak, some of these folders and files might be already there for you

.. code-block::

    RePak
    ├── RePak.exe
    ├── pack_all.bat
    ├── rpaks
    ├── maps
    └── assets

- ``RePak``: the base folder where your RePak/RPak related files go
- ``RePak.exe``: the `unzipped` file you downloaded from GitHub
- ``pack_all.bat``: a .bat file that will pack all of your RPaks when opened (outlined below)
- ``rpaks``: the folder where RePak.exe will put your RPaks when they have been created
- ``maps``: the folder where you will write your "map" files, these define the contents of your RPaks
- ``assets``: the folder where you will put your various different images and folders, used to create your RPaks

Making pack_all.bat
-------------------

``pack_all.bat`` is recommended for using RePak, as it allows for quick and easy packing of all of your RPaks.
Below is the script that should be copied into the file.

.. code-block:: bat

    for %%i in ("%~dp0maps\*") do "%~dp0RePak.exe" "%%i"
    pause

Making RPaks
^^^^^^^^^^^^

This section will walk you through the process of making an RPak that replaces a camo, for information on making other types of RPaks, check the RePak docs THIS IS TODO

Finding the camo
----------------

Before you can make your RPak, you need to know which assets you want to replace.
Camos in Titanfall 2 tend to have their own RPaks, with the naming scheme ``camo_skin<number>_col.rpak``

Firstly, make sure you have LegionPlus downloaded, if you don't, it can be downloaded from `here <https://github.com/r-ex/LegionPlus/releases>`_.

Then use LegionPlus to open one of the ``camo_skin<number>_col.rpak`` RPaks, and extract the 

Making a map file
-----------------



.. |CamoRPak| image:: 