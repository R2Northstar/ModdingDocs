mod.json architecture
================================

Located at your mod's root folder, the `mod.json` file is the entrypoint of your mod; 
it contains human-readable information about it, which scripts to load, and a bunch
of interesting stuff.

This section will dig into each of the possible `mod.json` fields. Please note that 
`mod.json` keys must start with an uppercase letter.

Name and description
------------------------

Those ones are pretty self-explanatory. Both fields are used by Northstar itself 
to display in-game information about your mod in the main screen `Mods` menu.

Best pratice for your mod's name is to use the ``Author.ModName`` convention.

Version
------------------------

This field specifies version of your mod using ``X.Y.Z`` scheme; this field must be
updated each time you release a new version of your mod.

Common use is to increase *Z* when you publish a fix (*e.g.* ``1.5.0`` to ``1.5.1``), and 
increase *Y* when you release new features (*e.g.* ``1.5.1`` to ``1.6.0``).

Best practise is to follow semantic versioning (https://semver.org/).

LoadPriority
------------------------

This field defines the order in which all mods will be loaded by Northstar. For example,
a mod with `"LoadPriority": 1` will be loaded after a mod with `"LoadPriority": 0`.

If your mod uses code from another mod, make sure to set a greater LoadPriority than the 
mod you're using code from.

ConVars
------------------------

This field lists configuration variables, that can be set by servers owners to modify 
behaviour of your mod.

Each configuration variable must have a ``"Name"`` and a ``"DefaultValue"``.

You can access configuration variables from squirrel code using ``GetConVarInt``, 
``GetConVarFloat``, ``GetConVarBool`` or ``GetConVarString`` calls.

.. warning::

   No matter the type of your variables, they have to be JSON strings, otherwise game won't start!

Example
^^^^^^^^^^^^^^^^^^^^^^^^ 

If I don't want to wait 15 seconds for matchs to start on my server, ``Northstar.CustomServers`` 
mod exposes a ConVar named `ns_private_match_countdown_length` in its ``mod.json`` manifesto:

.. code-block:: json

    "ConVars": [
        {
            "Name": "ns_private_match_countdown_length",
            "DefaultValue": "15"
        },

        ...
    ]

I can setup the ``ns_private_match_countdown_length`` variable in my 
``R2Northstar/mods/Northstar.CustomServers/mod/cfg/autoexec_ns_server.cfg`` configuration file.

When starting a match, ``Northstar.CustomServers`` mod will retrieve the configuration variable
value, or its default value if it hasn't been specified in configuration file:

.. code-block:: javascript

    // start countdown
    SetUIVar( level, "gameStartTime", Time() + GetConVarFloat( "ns_private_match_countdown_length" ) ) 

.. note::

   All ``Northstar.CustomServers`` ConVars are listed here: https://r2northstar.gitbook.io/r2northstar-wiki/hosting-a-server-with-northstar/basic-listen-server

Scripts
------------------------

Strip off "gettingstarted" section?

* array of scripts
* path + runOn fields
  * client VM vs server VM
  * RunOn syntax
* client and server callbacks  

Localisation
------------------------

This field is an array listing localisation files relative paths.

For more info about localisation works on Northstar, read the :doc:`localisation` section.