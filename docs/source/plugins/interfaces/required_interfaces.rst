Required Interfaces
===================

All plugins are required to expose these interfaces, otherwise they will not get loaded.

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

