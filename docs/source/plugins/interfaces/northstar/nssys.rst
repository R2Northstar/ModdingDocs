NSSys
=====

.. cpp:enum:: LogLevel

    .. cpp:enumerator:: INFO

    .. cpp:enumerator:: WARN

    .. cpp:enumerator:: ERR

.. cpp:struct:: NSSys

    Northstar system functionality

    .. cpp:function:: void Log(HMODULE pluginHandle, LogLevel level, const char* msg)

    .. cpp:function:: void Unload(HMODULE handle)

    .. cpp:function:: void Reload(HMODULE handle)
