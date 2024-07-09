Required Interfaces
===================

All plugins are required to expose these interfaces, otherwise they will not get loaded.

PluginId
--------

.. note::

   The latest version is ``PluginId001``

.. cpp:struct:: PluginId

    Query static data about a plugin like it's name

    .. cpp:function:: const char* GetString(PluginString prop)

    .. cpp:function:: int64_t GetField(PluginField prop)

.. cpp:enum:: PluginString

   Identifier of the string queried by ``GetString``. Enum members are 32 bit large.

    .. cpp:enumerator:: NAME

      Name of the plugin

    .. cpp:enumerator:: LOG_NAME

      Name of the plugin used for logging

.. cpp:enum:: PluginField

    Identifier of the bitfield queried by ``GetField``. Enum members are 32 bit large.

    .. cpp:enumerator:: CONTEXT

      - ``1`` if the plugin should run on dedicated servers
      - ``2`` if the plugin should run when ``client.dll`` is going to get loaded

PluginCallbacks
---------------

.. note::

   The latest version is ``PluginCallbacks001``

.. cpp:struct:: PluginCallbacks

    Callbacks for the launcher

    .. cpp:function:: void Init(HMODULE nsModule, const PluginNorthstarData* initData, bool reloaded)

      Called after the plugin has been loaded and validated.

    .. cpp:function:: void Finalize()

      Called after all plugins have been loaded.

    .. cpp:function:: bool Unload()

      Called just before the plugin library will get unloaded by the launcher's plugin system.

      If ``false`` is returned, the plugin will not be unloaded.

      At the moment plugins that get unloaded are intended for development purposes. Consider always returning ``false`` in distributed builds of your plugin.

    .. cpp:function:: void OnSqvmCreated(CSquirrelVM* sqvm)

      Notifies the plugin of any squirrel virtual machines that got created

    .. cpp:function:: void OnLibraryLoaded(HMODULE module, const char* libraryName)

      Notifies the plugin of any other library loaded by the launcher or any other library.

    .. cpp:function:: RunFrame()

      .. note::

        Keep this function simple to avoid performance issues

      This function will run every frame of the game.

      If you want to call any squirrel functions, you need to make sure the state of the vm allows it. If you're not in the context of a native closure and want to call a squirrel function, you need to implement a buffer that calls objects in this Callback.


.. cpp:struct:: PluginNorthstarData

    Data passed to plugins on initialization

    .. cpp:var:: HMODULE pluginHandle

    The handle of this plugin used for logging
