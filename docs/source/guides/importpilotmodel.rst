.. _importpilotmodel:

Pilot Model Importing
=====

Tools:
^^^^^

.. _Blender: https://www.blender.org/
`Blender`_ 

.. _Blender Source Tools: http://steamreview.org/BlenderSourceTools/
`Blender Source Tools`_

.. _Titanfall VPK Tools: https://retryy.gitbook.io/tf2/Wiki/Tools/vpk-tools
`Titanfall VPK Tools`_

.. _Crowbar: https://steamcommunity.com/groups/CrowbarTool
`Crowbar`_

.. _Legion+: https://github.com/r-ex/LegionPlus
`Legion+`_

.. _RePak: https://github.com/r-ex/RePak
`RePak`_

.. _mdlshit: https://github.com/headassbtw/mdlshit-binaries
`mdlshit`_

.. _Text Editors: https://retryy.gitbook.io/tf2/Wiki/Tools/general-pc-tools#text-editing
`Text Editors`_

Exporting the pilot model from the vpk
^^^^^

Locate your Titanfall 2 game folder
-----

For Origin you should find it in this directory ``Origin Games\Titanfall2``
For Steam you should find it in this directory ``Steam\steamapps\common\Titanfall2``

Open Titanfall VPK Tool
-----

At the top left press the ``Open`` button.
Open the vpk folder then open ``englishclient_mp_common.bsp.pak000_dir.vpk``,
Expand the ``models`` folder, then the ``humans`` folder, then click on the ``pilots`` folder.

The files have different names that correspond to their pilot classes

====================    ===== 
VPK .mdl name           Name
====================    =====
pilot_light_jester      Stim
pilot_light_ged         Phase Shift
pilot_medium_stalker    Holo Pilot
pilot_medium_reaper     Pulse Blade
pilot_medium_geist      Grapple
pilot_heavy_roog        A-Wall
pilot_heavy_drex        Cloak
====================    =====
Export the pilot model to any location you desire.

Exporting the POV model (Optional)
^^^^^

Do the following if you want your model to be visible from the perspective of anyone using the modified model
Expand the models folder, then the weapons folder, then click on the arms folder
Repeat the same process used for exporting the pilot model to export the POV file


Decompiling the pilot model
^^^^^

Open Crowbar
-----

Select ``Decompile`` at the top
Click on the browse button next to “MDL input” then locate and select your exported pilot model.
Click on the browse button next to “Output to” then choose any location you want the decompiled model to go to.

Modifying the model with Blender
^^^^^

Open Blender
-----

Select ``Edit`` then ``Preferences``
Press ``Install`` at the top right
Locate the Blender Source Tools zip file and select it (Make sure to enable it)
Select ``File`` at the top left, import, then Source Engine
Locate and select the decompiled pilot model
Make any changes you want
The head of your model should be separate from the rest of the body. You can use the bisect tool in edit mode to separate the head if it isn’t already.
Separating the head	
Make sure the body and head of your model match the names of the pilot model
Drag your model’s head and body into the correct collection
Delete the pilot models head and body after doing so
Renaming and putting your model in the correct collection
Rig the model to match the bones of the armature that came with the pilot model
Create an armature modifier for your model’s body and head

.. image:: /_static/importpilotmodel/ss0-pilotBlenderArmature.png
   :align: center
   :class: screenshot


Attach the model’s body and head to the armature
The video does not have the model properly aligned with the armature. Please make sure your model is aligned with the armature before attaching the model to it
A properly rigged model should look like this

.. image:: /_static/importpilotmodel/ss1-pilotBlender.png
   :align: center
   :class: screenshot

If you have multiple textures on your model then you would create several materials that match the name of the textures for the pilot you are modifying
If you only have one texture for your model just create one material for your entire model
Use LegionPlus to view paths for materials

.. image:: /_static/importpilotmodel/ss2-pilotBlenderMatl.png
   :align: center
   :class: screenshot

Once you have made all the changes you wanted to, select Scene Properties, Source Engine Export, then set the export format to SMD and set an export path.

.. image:: /_static/importpilotmodel/ss3-BlenderQcModifier.png
   :align: center
   :class: screenshot

Copy the qc file to the same location where you exported the model

Modifying the POV model (Optional)
^^^^^

Select ``File`` in Blender, then select ``Save Copy``
Choose any name, save the copy, then open the copy
Delete everything except for the body, the body collection, and the skeleton
Add “pov_” to the beginning of your body model and armature
Repeat the process of exporting the model with Source Engine Export

Using Legion+ to view paths
^^^^^

Open `Legion+`_
-----

Select Load File
Follow the directory that matches your launcher
“Steam\steamapps\common\Titanfall2\r2\paks\Win64\common.rpak”
“Origin Games\Titanfall2\r2\paks\Win64\common.rpak”
Type the file name of the pilot into the search bar to view texture and material paths
View file paths to create paths in RePak

Recompiling the model
^^^^^

Open `Crowbar`_
-----

Select ``Compile``
Click on the Browse button next to ``QC input`` then locate and select your modified model
Click on the Browse button next to ``Output to`` then choose a location to output the model to

Making a Pak file
^^^^^

Follow this `tutorial <https://r2northstar.readthedocs.io/en/latest/guides/rpakmodding.html>`_ to create a pak file

Making changes to the qc file (Optional)
^^^^^

Open any text editor 
If you want to prevent camos from being used on your model, delete any textures that have skn31 in the texture group

.. figure:: /_static/importpilotmodel/ss4-qcFileChanges.png
   :align: center

.. figure:: /_static/importpilotmodel/ss5-qcFileChanges2.png
    :align: center

Creating a Northstar mod
^^^^^

Follow this guide to create a Northstar mod
Create a folder that matches this file structure
Only create the weapons folder and everything else within it if you made a pov model

.. Directory Structure for Northstar Mod
:: 

    AuthorName.Mod
    ├──mod
    |   └──models
    |       └──humans
    |           └──pilots
    |               └──customModel
    ├──paks
    |   ├──rpak.json
    |   ├──example.rpak
    |   └──preloadexample.rpak
    └──mod.json