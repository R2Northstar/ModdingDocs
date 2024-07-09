Northstar Interfaces
====================

Interfaces exposed by ``northstar.dll``

.. cpp:struct:: NSSys

    Northstar system functionality

    .. cpp:function:: void Log(HMODULE pluginHandle, LogLevel level, const char* msg)

      Log a message into it's sink maintained by the launcher

    .. cpp:function:: void Unload(HMODULE handle)

      Unload a plugin by it's handle

    .. cpp:function:: void Reload(HMODULE handle)

      Reload a plugin by it's handle

.. cpp:enum:: LogLevel

    .. cpp:enumerator:: INFO

    .. cpp:enumerator:: WARN

    .. cpp:enumerator:: ERR

