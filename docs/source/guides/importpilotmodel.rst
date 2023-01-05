Pilot Model Importing
=====================

Tools Needed
-------------
- `Blender <https://www.blender.org/download/>`_
- `Blender Source Tools <http://steamreview.org/BlenderSourceTools/>`_
- `Titanfall VPK Tool <https://github.com/Wanty5883/Titanfall2/blob/master/tools/Titanfall_VPKTool3.4_Portable.zip>`_
- `Crowbar <https://github.com/ZeqMacaw/Crowbar/releases>`_
- `LegionPlus <https://github.com/r-ex/LegionPlus/releases>`_
- `RePak <https://github.com/r-ex/RePak/releases>`_
- `MDLShit <https://github.com/headassbtw/mdlshit-binaries/releases>`_

Any text editor `Visual Studio Code (optional but recommended) <https://code.visualstudio.com/>`_

Exporting the pilot model from the VPK
--------------------------------------

* Locate your ``Titanfall 2`` game folder:

  * For Origin (Default): ``OriginGames/Titanfall2``
 
  * For Steam: ``Steam/steamapps/common/Titanfall2``

* Open ``Titanfall VPK Tool`` and press the open button at the top left.


* Step by step first expand the ``models`` > ``humans`` > click on the ``pilots`` folder.

* The files have different names that correspond to their pilot classes;
  
  * pilot_light_jester = Stim
  
  * pilot_light_ged = Phase Shift
  
  * pilot_medium_stalker = Holo
  
  * pilot_medium_reaper = Pulse Blade
  
  * pilot_medium_geist = Grapple
  
  * pilot_heavy_roog = A-Wall
  
  * pilot_heavy_drex = Cloak
  
* Export the pilot model to any location you desire.

Exporting the POV model (Optional)
----------------------------------

Do the following if you want your model to be visible from the perspective of anyone using the modified model:

* Expand the ``models folder`` > ``weapons folder`` > ``arms folder.``

* Repeat the same process used for exporting the ``pilot model`` to export the POV file.


Decompiling the pilot model
---------------------------

* Open `Crowbar`_

* Select ``Decompile`` at the top.

* Click on the browse button next to ``MDL input`` then locate and select your exported pilot model.

* Click on the browse button next to ``Output to`` then choose any location you want the decompiled model to go to.

Modifying the model with `Blender`_
------------------------------------

* Open `Blender`_

* Select ``Edit`` then ``Preferences``

* Press ``Install`` at the top right.

* Locate the Blender Source Tools zip file and select it (Make sure to enable it).

* Select ``File`` at the top left > ``Import`` > ``Source Engine``

* Locate and select the ``decompiled pilot model`` and make any changes you want.

* The head of your model should be separate from the rest of the body. You can use the ``bisect tool`` in edit mode to separate the head if it isn’t already.

  * `Separating the head <https://drive.google.com/file/d/1l_FXbB0H6ptSjR44CXC1OflIcytmB5XA>`_  
* Make sure the body and head of your model match the names of the pilot model.

* Drag your model’s head and body into the correct collection.

* Delete the ``pilot models head and body`` after doing so.

  * `Renaming and putting your model in the correct collection <https://drive.google.com/file/d/12uy3Zje7q8OSShrTNSU8JMrvbFxGaaL0/view>`_

* Rig the model to match the bones of the armature that came with the pilot model.

* Create an armature modifier for your model’s body and head.

* `Attach the model’s body and head to the armature <https://drive.google.com/file/d/1VOt8ntuxCZJ4sHmMw_WKhu367nT5DmGL/view>`_

  * The video does not have the model properly aligned with the armature. Please make sure your model is aligned with the armature before attaching the model to it.

  * A properly rigged model should look like this.
  

|image1|


* If you have multiple textures on your model then you would create several materials that match the name of the textures for the pilot you are modifying.

* If you only have one texture for your model just create one material for your entire model.

  * Use `LegionPlus`_ to view paths for materials.

|image2|

* Once you have made all the changes you wanted to, select ``Scene Properties`` > ``Source Engine Export`` then set the export format to ``SMD`` and set an export path.

|image3|

* Copy the `QC <https://developer.valvesoftware.com/wiki/QC>`_ file to the same location where you exported the model.

Modifying the POV model (Optional)
----------------------------------

* Select ``file`` in `Blender`_, then select ``Save Copy.``
* Choose any name, save the copy, then open the copy.
* Delete everything except for the body, the body collection, and the skeleton.
* Add ``pov_`` to the beginning of your body model and armature.
* Repeat the process of exporting the model with ``Source Engine Export``

Using `LegionPlus`_ to view paths
----------------------------------

* Open `LegionPlus`_
* Select ``Load File``
* Follow the directory that matches your launcher,
  
  * ``Steam/steamapps/common/Titanfall2/r2/paks/Win64/common.rpak``
  
  * ``Origin Games/Titanfall2/r2/paks/Win64/common.rpak``
  
* Type the file name of the pilot into the search bar to view ``texture`` and ``material paths.``
* View file paths to create paths in ``RePak.``


Recompiling the Model
---------------------

* Open `Crowbar`_
* Select ``Compile``
* Click on the Browse button next to ``QC input`` then locate and select your modified model.
* Click on the Browse button next to ``Output to`` then choose a location to output the model to.

Making a PAK file
------------------

* `Follow this tutorial to create a pak file. <https://r2northstar.readthedocs.io/en/latest/repak/map.html>`_
* It’s recommended to use Visual Studio Code when making RPak maps.


Making changes to the `QC`_ file (Optional)
-------------------------------------------
|image4|

* Open any text editor.
* If you want to prevent camos from being used on your model, delete any textures that have ``skn31`` in the texture group.

Creating a Northstar mod 
-------------------------
Documented in `Getting Started <https://r2northstar.readthedocs.io/en/latest/guides/gettingstarted.html>`_

* Create a folder that matches this file structure,
* Only create the weapons folder and everything else within it IF you made a ``pov model.``
:: 

    AuthorName.Mod
    ├── mod
    |   └── models
    |       └── humans
    |           └── pilots
    |               └── ModifiedCustomModel
    |       └── weapons
    |           └── arms
    |               └── ModifiedPovModel
    ├── paks
    |   ├── rpak.json
    |   ├── YourRpakFile.rpak
    |   └── PreLoadRpak.rpak
    └──mod.json


.. |image1| image:: https://raw.githubusercontent.com/rwynx/northstar-commands-and-audio-overriding/main/Images/imagerst1.png
.. |image2| image:: https://raw.githubusercontent.com/rwynx/northstar-commands-and-audio-overriding/main/Images/imagerst2.png
.. |image3| image:: https://raw.githubusercontent.com/rwynx/northstar-commands-and-audio-overriding/main/Images/imagerst3.png
.. |image4| image:: https://raw.githubusercontent.com/rwynx/northstar-commands-and-audio-overriding/main/Images/imagerst4.png
