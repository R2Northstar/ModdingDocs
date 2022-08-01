VTF Modding
===========

VTF Overview
------------

VTF, short for "Valve Texture Format", is a texture type used by Valve in the source engine and is occasionally in Titanfall. vtf's are used for fx, animation, and other textures. 


VMT Overview
------------

VMT, short for "Valve Material Type", is a text `material <https://developer.valvesoftware.com/wiki/Material>`__ system that dictates how the game perceives a vtf outside of how it looks. It uses `parameters <https://developer.valvesoftware.com/wiki/Category:List_of_Shader_Parameters>`__ and `proxies <https://developer.valvesoftware.com/wiki/Material_proxies>`__ to dictate how `shaders <https://developer.valvesoftware.com/wiki/Shader>`__ will show the game. We will go into greater detail later.

Editing FX that use VTFs
------------------------

A lot of fx in Titanfall use vtf's as textures. Therefore, if the corresponding vtf can be found, we can do almost anything with the fx's appearence.
Example Mod: `Exrill's Blue L-Star <https://northstar.thunderstore.io/package/EXRILL/Exrills_Blue_Lstar/>`_.
Since the L-Star has a physical bullet that is counted as fx, we can edit how it looks.

VTF Skins
---------

Since vtf modding was majorly for introducing custom weapon skins. Most of the development on VTF modding was designed focused on custom weapon skins. Though understanding how custom VTF skins is specific, it is needed in order to VTF mod other textures. 

Most textures in the game use .dds. We can make them use .vtf. 

What we'll be doing is extracting the model. Replacing the texture path in the mdl to lead to our texture. Then using our texture and allowing for extra properties.

.. _VPK Tool: https://github.com/Wanty5883/Titanfall2/blob/master/tools/Titanfall_VPKTool3.4_Portable.zip

VPK Tool
--------
.. _cra0 VPKTool: https://github.com/Wanty5883/Titanfall2/blob/master/tools/Titanfall_VPKTool3.4_Portable.zip

.. _Harmony VPKTool: https://github.com/harmonytf/HarmonyVPKTool

You have 2 options for a VPK tool. Pick either the older VPK tool: `cra0 VPKTool`_ or the Newer VPK tool: `Harmony VPKTool`_

With your VPK tool opened. 'Open' ``englishclient_mp_common.pak000_dir.vpk`` which is located in ``Titanfall2/vpk``. 

Inside of the VPK. Not all guns are named the same in files as they are in game. Here is `list of weapon names <https://noskill.gitbook.io/titanfall2/documentation/file-location/weapon/weapon-model>`_ to help you out. Navigate to ``models/weapons/car101``. Extract all the viewmodel versions (ptpov) and normal model (w) mdl's.

Hex Editor
----------

To change the path in the .mdl to the custom .vtf texture. We need a hex editor. I will use `HxD`_, but you can also use `ida`_, or anything else; its personal preference. 

.. _HxD: https://mh-nexus.de/en/hxd/
.. _ida: https://hex-rays.com/ida-free/


In your hex editor. Open your .mdl. We need to get closer to the string we need or else you'll be scrolling and searching for hours. Search (ctrl+f) for skin_31. If you don't get any matches, try skn_31, skin31, elite, or prime. T 

The string of text we need should look something like ``models\Weapons_R2\weaponname\weaponname_skin_31``. Near it, there should be the same text, but without the ``_skin_31``. This is the path to the default textures. 

Now, before you edit, you have to realize hex editors are just built different (cant help it). You cannot add or delete text with a hex editor, only replace. Go to the start of the path for the default textures, and change the path to anything else, as long as it starts with ``.models\weapons_r2``. 

We'll change the path from ``.models\Weapons_r2\car101\car_smg`` to ``.models/weapons_r2/car101/car_ctm``.  Note the capitalization. Some vpk repacking tools cannot repack properly if we edit in captials. Now do these changes for ``ptpov_`` and/or ``w_`` model(s). 

 Creating VMT
-------------

In the same folder you extracted your mdl's. Make a ``materials`` folder next to the ``models`` folder. Inside the ``materials`` folder. Recreate the path you hex edited, but the last name is a .vmt file. Not a folder. Our path of folders is ``.models/weapons_r2/car101``, our .vmt file would be named ``car_ctm.vmt``. 

Inside your .vmt paste:
::

	"UnlitTwoTexture"
	{

		"$surfaceprop" "metal"
		"$basetexture" ""
		"$texture2" ""
		"$bumpmap" ""	
		"$allowoverbright" "1"
		"$vertexcolor" 1
		"$vertexalpha" 1	
		"$decal" "1"
		"$model" 1
		"$nocull" "1"
	}

When we use vtf textures, we can only use the albedo and normal `maps <https://titanfall-skin-group.gitbook.io/titanfall-2-skin-creation/ms/genral-information/texture-maps>`_. 

VTFEdit
--------

`VTFEdit`_ is a tool to edit, view, and create .vtf files.

.. _VTFEdit: https://nemstools.github.io/pages/VTFLib-Download.html

Launch `VTFEdit`_. Top left, click `File`, `Import`, find and Import your custom texture. After that, save your new .vtf into the same folder as your custom .vmt. 

Configuring your .vmt
---------------------

In the ``"$basetexture"`` "area". So i would put, `models\weapons_r2\vtfkraber\kraber_col`. Then do the same for your normal map, but when you import it, pick volume texture instead of animated texture. In `"$bumpmap"` put the path to your normal texture. Now create another vtf with literally any image. Put its path in `"$texture2"`. As far as i know, this is neccesary even though the texture isnt used. Your root folder should look somewhat like this::

	root
	├─ materials
	│  └─ models
	│     └─ weapons_r2
	│        └─ vtfkraber
	│           └─ vtfkraber.vmt
	└─ models
	   └─ weapons
	      └─at_rifle (name of kraber)
	        ├─ ptpov_at_rifle.mdl
	        └─ w_at_rifle.mdl

And you're done! You just need to pack it into a vpk with the vpk tool and put it in a mod.

Making your Skin Animated
-------------------------

To make an animated skin, all we need to do is add a proxie and change our albedo vtf. Once you've made the frames of your skin, import them all at once with ctrl+a and save your vtf. Put it as `"$basecolor"`. At the bottom of your vmt but before the }, add this:
::
	"Proxies"
	{
			AnimatedTexture
			{
				animatedTextureVar $basetexture
				animatedTextureFrameNumVar $frame
				animatedTextureFrameRate 
			}
	}

Put the fps you want your skin to play at in afet animatedTextureFrameRate, and you're done!
