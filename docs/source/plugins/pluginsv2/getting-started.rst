Getting Started
===============

for plugins you can use any language that be compiled into a dll.
But its better to use either ``rust`` or ``c++``.

plugins with c++
^^^^^^^^^^^^^^^^^^^^^^
c++ is used in northstar and titanfall so it makes it easy to work with titanfall's engine.

A template for c++ plugins would be the unfinished `discord rpc v2 <https://github.com/R2Northstar/NorthstarDiscordRPC/tree/rewrite>`__.
it is some parts of northstar commbied with custom stuff.

plugins with rust
^^^^^^^^^^^^^^^^^^^^^^
altought rust isn't used by northstar or titanfall, 
it is arguably the best language for plugins because of `rrplug <https://github.com/catornot/rrplug>`__

a good example of a rust plugin with rrplug is `furnace <https://github.com/catornot/furnace>`_

..
    this wasn't biased at all. trust me

what a plugin dll needs?
^^^^^^^^^^^^^^^^^^^^^^^^

the plugin system looks for a manfest in the dll inserted with windres.

the other things are function exports for each callback.

exports
-------

.. cpp:function:: void PLUGIN_INIT(PluginInitFuncs* funcs, PluginNorthstarData* data)

    called on northstar init with init data

.. cpp:function:: void PLUGIN_INIT_SQVM_CLIENT(SquirrelFunctions* funcs)

    called when sqvm client funcs loaded

.. cpp:function:: void PLUGIN_INIT_SQVM_SERVER(SquirrelFunctions* funcs)

    called when sqvm server funcs loaded

.. cpp:function:: void PLUGIN_INFORM_SQVM_CREATED(ScriptContext context, CSquirrelVM* sqvm)

    called when a sqvm is created and passes that sqvm

.. cpp:function:: void PLUGIN_INFORM_SQVM_DESTROYED(ScriptContext context)

    called when a sqvm is destroyed

.. cpp:function:: void PLUGIN_INFORM_DLL_LOAD(PluginLoadDLL dll, void* data)

    called on engine load with engine funcs and vtables



