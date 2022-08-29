Publishing your mod
===================

Best practices
--------------

Make sure to name your mod in the form ``<your name>.<mod name>``, similar to the existing default mods, like ``Northstar.Client``, ``Northstar.CusomServer``,
Note that the Northstar name (``Northstar.Xyz``) is reserved for mods that come with the Northstar install and should therefore **not** be used.

It is recommended to upload the source code of your mod to a public repository like `Github <https://github.com/>`_ to give your users a place to suggest changes and leave feedback in an organised manner.

If the changes your mod makes can be represented in screenshots, gameplay recordings, or GIFs, consider adding those to your README. This way anyone coming across your mod can tell which aspects of the game it changes even before installing it.

To do so, simply upload the image or gif to a host of your choice (Imgur, GitHub, and even Discord all work). To display the image directly on your page in Thunderstore, add the following line to your README:

.. code:: markdown

    ![alt text, this text shows up when image cannot be loaded](https://example.com/image/to/link/to.gif)


Thunderstore
------------

The best place to publish your mod is `Thunderstore <https://northstar.thunderstore.io/>`_. To do so, you need to package your mod as a zip with a specific folder structure. You can either set the structure up manually or use `this GitHub template <https://github.com/laundmo/northstar-mod-template>`_

Package structure
^^^^^^^^^^^^^^^^^

The Thunderstore package zip structure is as follows:

.. code-block::

    mods/<your name>.<mod name>/
    icon.png
    manifest.json
    README.md


- ``icon.png``: 256x256px icon for your mod.
- ``README.md``: the description page for your mod
- ``manifest.json`` outlined `here <https://northstar.thunderstore.io/package/create/docs/>`_

You can put multiple mods in the ``mods/`` folder, but only do this if neccessary.

``manifest.json`` checker: `https://northstar.thunderstore.io/tools/manifest-v1-validator/ <https://northstar.thunderstore.io/tools/manifest-v1-validator/>`_

Uploading
^^^^^^^^^

After you have set up the folder structure, head to `https://northstar.thunderstore.io <https://northstar.thunderstore.io>`_ and log in with either Discord or Github. Then you can use the `Upload` button at the top of the page to upload your zip.

When uploading, it will verify your package structure and you can publish after it's successfully checked.

To update a mod, change the version in ``mod.json`` and ``manifest.json``, and upload again. If the mod name is the same, it will update the previous version.


Verified mods
-------------

If you server requires client-side mods, when people connect to it, they will see this kind of message:

.. image:: ../img/missing_mod_screenshot.png
  :width: 1000
  :alt: Game client displays a "required mod" message.

This requires players to manually download required mods, which prevents them from playing straight away, and thus breaks user experience.

Fortunately, to counter that, Northstar integrates a *verified mod* feature: if a mod is missing and it has been verified by the Northstar team, game clients will automatically download it.

For your mod to be verified, you need to follow the following rules:

1. Source code is publicly available
2. Mod is automatically uploaded to Thunderstore via continuous deployment (check "Recommanded mod template" section below!)
3. Mod follows semantic versioning

Once your mod is ready, for it to be verified, you can open a pull request on this repository to add your mod: TODO

You will need to do this each time you release a new version of your mod.

Recommanded mod template
^^^^^^^^^^^^^^^^^^^^^^^^

We recommand you to use the `AnActualEmerald mod template <https://github.com/GreenTF/NSModTemplate>`_, which integrates 
a continuous integration job, which will automatically build your mod and upload it to Thunderstore each time you 
create a GitHub release.

If you want to tune CI more precisely, you'll find its `documentation here <https://github.com/GreenTF/upload-thunderstore-package>`_.