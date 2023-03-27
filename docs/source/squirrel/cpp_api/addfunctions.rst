Squirrel Functions API
======================

Adding Squirrel Functions
-------------------------

You can use the ``ADD_SQFUNC`` macro defined in ``squirrelautobind.h`` to easily add new Squirrel functions for specific contexts.

Inside the macro you have access to the Squirrel Manager of the context the function has been called from and the SQVM.

.. cpp:function:: macro ADD_SQFUNC(return_type, funcName, argTypes, helpText, runOnContext)

    :param return_type: The squirrel return type the compiler expects from this function
    :param funcName: The squirrel function name
    :param argTypes: The args with types the compiler expects
    :param helpText: A help text describing the function
    :param runOnContext: The contexts that have access to this function

Examples
~~~~~~~~

Return a string from a native registered function:

.. code-block:: cpp

    ADD_SQFUNC("string", CPlugTest, "", "returns \"native gaming\"", ScriptContext::CLIENT | ScriptContext::SERVER)
    {
        g_pSquirrel<context>->pushstring(sqvm, "native gaming"); // push a string to the stack
        
        return SQRESULT_NOTNULL; // Signal that the topmost item on the stack is returned by this function
    }

.. code-block:: cpp

    ADD_SQFUNC("array ornull", CPlugComplex, "int n", "returns null", ScriptContext::CLIENT | ScriptContext::SERVER | ScriptContext::UI)
    {
        SQInteger n = g_pSquirrel<context>->getinteger(sqvm, 1);

        if (n == 0)
            return SQRESULT_NULL;

        g_pSquirrel<context>->newarray(sqvm, 0);
        g_pSquirrel<context>->pushinteger(sqvm, n);
        g_pSquirrel<context>->arrayappend(sqvm, 2);
        g_pSquirrel<context>->pushinteger(sqvm, n * 2);
        g_pSquirrel<context>->arrayappend(sqvm, 2);

        return SQRESULT_NOTNULL; // return the array [ n, n * 2 ]
    }

Return a complex ``ornull`` type:

.. code-block:: cpp

    ADD_SQFUNC("ornull int", CPlugComplex, "int n", "returns null", ScriptContext::CLIENT | ScriptContext::SERVER | ScriptContext::UI)
    {
        SQInteger n = g_pSquirrel<context>->getinteger(sqvm, 1);
        
        if (n == 0)
            return SQRESULT_NULL;

        g_pSquirrel<context>->newarray(sqvm);
        g_pSquirrel<context>->pushinteger(sqvm, n);
        g_pSquirrel<context>->arrayappend(sqvm, 2);
        g_pSquirrel<context>->pushinteger(sqvm, n * 2);
        g_pSquirrel<context>->arrayappend(sqvm, 2);

        return SQRESULT_NOTNULL; // return the array [ n, n * 2 ]
    }

Replacing Squirrel Functions
----------------------------

You can use the ``REPLACE_SQFUNC`` macro to replace an existing sq function.

.. cpp:function:: macro REPLACE_SQFUNC(funcName, runOnContext)

    :param funcName: The name of the function to replace
    :param runOnContext: The contexts that have access to this function

It's also possible to add an override directly with the ``AddFuncOverride`` funciton of the ``SquirrelManager`` class.

.. cpp_function:: void AddFuncOverride(std::string name, SQFunction func)

    :param std::string name: The name of the function to override
    :param SQFunc func: A function object that replaces the logic

.. code-block:: cpp

    // Replaces dangerous vanilla functions to only log their call with no further logic.
	g_pSquirrel<context>->AddFuncOverride("DevTextBufferWrite", SQ_StubbedFunc<context, "DevTextBufferWrite">);
	g_pSquirrel<context>->AddFuncOverride("DevTextBufferClear", SQ_StubbedFunc<context, "DevTextBufferClear">);
	g_pSquirrel<context>->AddFuncOverride("DevTextBufferDumpToFile", SQ_StubbedFunc<context, "DevTextBufferDumpToFile">);

Script Contexts
---------------

Scriptcontexts are used to define the VMs that have access to a native function. Available Contexts are

- ``ScriptContext::SERVER`` - The SERVER sqvm
- ``ScriptContext::CLIENT`` - The CLIENT sqvm
- ``ScriptContext::UI`` - The UI vm

Script Returns
--------------

Squirrel functions need to return a ``SQRESULT``. Valid results are

- ``SQRESULT_NULL`` - This function returns ``null``. Nothing is left over on the stack.
- ``SQRESULT_NOTNULL`` - This functions returns the last item on the stack.
- ``SQRESULT_ERROR`` - This function has thrown an error.
