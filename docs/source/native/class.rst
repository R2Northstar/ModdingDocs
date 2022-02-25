Classes
=======

.. note::

   This is by no means complete. Please add anything you know.

Declaring Classes
-----------------

To declare a class, first add the ``untyped`` keyword and the class as a global variable at file level.

.. code-block:: javascript

    untyped
    global var ExampleClass

The ``untyped`` declaration is required because instances have an unknown type and it's not possible to use classes as types.

``global var [classname]`` represents the class. After declaring the class inside of a function you can use it anywhere. It's not possible to declare classes on local variables.

You can then add the declaration inside of a function.

Most classes use a constructor. A constructor is a function of the instance that gets executed on object creation.

.. code-block:: javascript

    void function initClient() {
        class ExampleClass {
            constructor(){print("Instance of ExampleClass created");}
        }
    }

You can require parameters in the constructor. Keep in mind that you have to pass those when creating an object.

The types of the parameters have to be ``var``, but you can ``expect`` types in the constructor as usual.

.. code-block:: javascript

    class ExampleClass {
            propertyString // Actual type is var
            propertyInt // Actual type is var
            constructor( var pString, var pInt ) {
                this.propertyString = expect string(pString);
                this.propertyInt = expect int(pInt); 
            }
    }

    // See section "Declaring Objects" for more information on object creation
    var obj = ExampleClass( "foo", 1 );
    printt(obj.propertyString, obj.propertyString ) // foo, 1
    var lObj = ExampleClass(); tObj = ExampleClass( "" , 0 , 0); // Both throw an error compile time because parameters don't match with the constructor

Usually objects have properties. To define them, just add their identifier into the class without type declaration. The properties will be of type ``var``. However, you are required to set a default value of a property. This may be ``null``.

Every object has a reference to itself called ``this``. You can change parameters of an object by reference.

.. code-block:: javascript

    void function initClient() {
        class ExampleClass {
            property = null
            constructor( var parameter ) {
                this.property = expect int(parameter);
            }
        }
    }

You can't use the class name as a type. Instead use ``var`` instead. You can't ``expect`` them either.

Declaring Objects
-----------------

To declare an object, do:

.. code-block:: javascript

    class ExampleClass {
        property = null
        constructor( var parameter ) {
            this.property = expect int(parameter);
        }
    }

    var exampleObject = ExampleClass(1);
    int n = exampleObject.property // n = 1
    exampleObject.property++;
    n = exampleObject.property // n = 2

Like the example above shows you can manipulate properties of a class directly. There is no way to make a private property.

You can't add an index to an instance at runtime. Fields have to be defined at compile time.

.. code-block:: javascript

    // Using ``ExampleClass`` and ``exampleObject`` from example above
    exampleObject.nonExistantProperty // Asserts error 'The index "nonExistantProperty" does not exist in this instance'

Unlike other types, passing an object does not pass a copy of the object, but a reference to itself. This means that any modifications inside of a function are applied to the original object.

.. code-block:: javascript

    void function initClass(){
        class Container {
            content = null
            constructor ( var pString ) {
                this.content = expect string(pString);
            }
        }
        var con = Container("original string")
        manipulateContainer( con )
        print(con.content) // -> manipulated string
    }

    void function manipulateContainer( var con ){
        con.content = "manipulated string";
    }

You can avoid this by using cloned objects. Use the ``clone`` keyword to create a copy of an object.

.. code-block:: javascript

    // Assumes the 'Container' class from the previous example has already been declared
    void function initClass(){
        var originalObj = Container("original string")
        var clonedObj = clone originalObj
        manipulateContainer( clonedObj )
        printt(orignalObj.content, clonedObj.content) // -> original string, manipulated string
    }

    void function manipulateContainer( var con ){
        con.content = "manipulated string";
    }

It's also possible to create an instance without calling the constructor.

.. code-block:: javascript

    // Using 'ExampleClass' from previous examples
    var e = ExampleClass.instance()
    e.constructor(1) // Constructor is a normal function so you can call it manually.

Functions of a class do not have a return type. Define them like this:

.. code-block:: javascript

    function func(){
        return variable; // variable can be of any type
    }

.. warning::

    Respawn's fork doesn't appear to support inheritance. Using the ``extend`` keyword won't compile.

    .. code-block:: javascript

        class Child extends Parent{}

Make sure you check out the squirrel documentation on `classes <http://www.squirrel-lang.org/squirreldoc/reference/language/classes.html>`_ and built in `class instance <http://www.squirrel-lang.org/squirreldoc/reference/language/builtin_functions.html#class-instance>`_ methods for more information.