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

LoadPriority
------------------------

This field defines the order in which all mods will be loaded by Northstar. For example,
a mod with `"LoadPriority": 1` will be loaded after a mod with `"LoadPriority": 0`.

If your mod uses code from another mod, make sure to set a greater LoadPriority than the 
mod you're using code from.

## scripts and RunOn

RunOn syntax

## Keyvalues

## Localisation