Complex types
=============

Within squirrel there are many ways to store information, but when storing an unspecified amount of information, or storing information on a player-by-player basis, you need to use ``arrays`` or ``tables``.

Strings
-------

Strings in squirrel represent an array of chars, however chars are not their own type in squirrel, as they are represent by integers. To initialize a sting yo use the ``string`` keyword:

.. code-block:: javascript

  string Hello = "World"

You can get the integer value of any char with the ``[index]`` like in arrays, however this only returns the ASCII value of that character.
To get the string of the char, you need to:

.. code-block:: javascript

  int charInt = Hello[0]
  int charString = charint.tostring()

build in functions can be found on the official site `here <http://www.squirrel-lang.org/squirreldoc/reference/language/builtin_functions.html#string>`_ .

Arrays
------

Arrays can store large sets of data and are indexed using numbers, starting from 0, and are declared using ``array<type> arrayname`` the <type> identifier can be ignored but will result in the array being of the type ``var``.
  
.. code-block:: javascript

    array<int> numbers = [1,2,3,4,5,6,7,8,9,10]

    printt(numbers[0])
    >>1
    printt(numbers[5])
    >>6


adding and removing values from arrays can be done using ``.append(value)`` and ``.remove(index)``. 

additionally the index of values can be found using the ``.find`` function and the length by using the ``.len()`` function:

.. code-block:: javascript

    array<int> numbers = [1,2,3,4,5,6,7,8,9,10]

    printt(numbers.find(3))
    >>2
    printt(numbers[5])
    >>6
    numbers.remove(5)
    printt(numbers[5])
    >>7
    printt(numbers.len())
    >>9
    array<int> empty = []
    empty.append(5)
    printt(empty[0])
    >>5


Build in functions for arrays can be found `here <http://www.squirrel-lang.org/squirreldoc/reference/language/builtin_functions.html#id1>`_

Tables
------
Tables are similar to arrays but with one primary difference, rather than use a numerical index system tables allow you do define your own indexes, similar to pythons ``dict`` type.
Creation of a table is done in a similar way to arrays, however may have 2 types declared for the type of the index and the type of the content, much like arrays this will default to ``var`` if ignored

There are multiple ways to define a table with the ``[]`` when declaring a key you type a literal

.. code-block:: javascript

    table<string, int> numberofletters = {
      ["hello"] = 5,
      world = 5
    }

    table<int, int> numberSquared = {
      [2] = 4,
      [4] = 16
    }

unlike arrays however adding values to tables cannot be done using ``.append`` or similar means, as the index must also be declared, adding to tables is done using the ``<-`` operator like so.

.. code-block:: javascript

    table<entity, int> playerkills = {}
    foreach(entity player in GetPlayerArray())
        playerkills[player] <- 5

To read a value from a table you use the array syntax but instead of an index you write your key:

.. code-block:: javascript
    
    printt(playerKills[player])
    >> 5

The build in functions for arrays can be found `here <http://www.squirrel-lang.org/squirreldoc/reference/language/builtin_functions.html#table>`_

.. warning:: 

  The functions ``table.key()`` and ``table.value()`` are disabled in rSquirrel, as an alternative you can use: ``TableKeysToArray(table)``


Structs
--------
Structs are a way of storing multiple variables in one object. To create a struct you just write:

.. code-block:: javascript

    struct ExampleStruct {}
    
Inside the brackets you can declare all the variables your struct should contain, you can also directly assign a standard value to a variable, if you dont override this value it will automatically be assigned.

You can not only pass variables but also functions with:``*return type* functionref(*argument type*) *Name in the struct*``.

.. code-block:: javascript
  
    struct ExampleStruct {
      int VariableInt
      string VariableString
      array<int> VariableArray
      int Optional = 1
      
      void functionref() ExampleVoidFuncton //you need to assign a function that returns nothing and takes no arguments
      string functionref(string) ExampleStringFunction //here you need to assign a function that returns a string and takes a string as an argument
    }
    
You then need to create instances of your struct to use it, like this:

.. code-block:: javascript
      
      //functions we need to assign, they are placeholders
      void function VoidFuntion(){
        //do sth
        return
      }
      void function StringFunction(string s){
        return s
      }

      ExampleStruct structOne = {
        VariableInt = 1,
        VariableString = "Hello World",
        VariableArray = [1,2,3],
        ExampleVoidFunction = VoidFunction,
        ExampleStringFunction = StringFuntion,
        ... 
      }
                                  
      ExampleStruct stuctTwo =  {
        VariableInt = 3,
        VariableString = "Hello Modders",
        VariableArray = [4,5,6],
        ExampleVoidFunction = VoidFunction,
        ExampleStringFunction = StringFuntion,
        Optional = 2
      }
      

For values that we do not declare like ``Optional`` in the case of ``structOne`` we just add a ``...`` as an argument.
Now that we have two instances we can get the values out of it like this:

.. code-block:: javascript

      printt(structOne.VariableInt)
      >> 1
      printt(structOne.VariableString)
      >> Hello World
      printt(stuctOne.Optional)
      >> 1

      // here you can see that we did not specifically declare the variable but it still has a value that was assigned in the struct directly
      foreach(int a in structOne.VariableArray)
        printt(a)
      >>1
      >>2
      >>3
      print(structOne.ExampleStringFunction("Hello"))
      >>Hello
 
In struct one we have defined that ``ExampleStringFunction`` is assigned to ``StringFunction`` so we get the output if that function as a result.
      
We can do the same thing for ``structTwo``:


.. code-block:: javascript

      printt(structTwo.VariableInt)
      >> 2
      printt(structTwo.VariableString)
      >> Hello Modders
      printt(stuctTwo.Optional)
      >> 2
      // Now that we gave Optional a value the old one is overriten 
      foreach(int a in structTwo.VariableArray)
        printt(a)
      >>4
      >>5
      >>6
      printt(structTwo.ExampleStringFunction("Hello"))
      >>Hello
      //Since we gave it the same function the result is also the same

Now that we have a struct we can also pass it as an argument in functions or return the struct from a function:

.. code-block:: javascript 

    ExampleStruct function ChangeTheStruct(ExampleStruct struct){
        if(struct.VariableInt == 1)
            return struct
        else{
          struct.VariableInt = 1        
        }
        return struct
        
    }

You can also nest structs like this:

.. code-block:: javascript

    struct NewStruct{
      Examplestruct CoolStruct
      int CoolVariable
    }
    NewStruct s = {
      CoolStruct = structOne,
      CoolVariable = 1
    }
    //we now have a struct inside a struct
    printt(s.CoolStruct.VariableInt)
    >>1
    
    
``CoolStruct`` has the value of ``structOne`` we defined above thus the value output is the value from ``structOne.VariableInt``.

In the same way you can also use it as a type for arrays or tables:

.. code-block:: javascript 

    array<ExampleStruct> StructArray = []
    StructArray.append( structOne )
    printt(StructArray[0].VariableInt)
    >>1
    
    table<ExampleStruct, bool> StuctTable= {structOne: false}
    printt(StuctTable[stuctOne])
    >>false
    
Alternatively you can define a struct and directly have it as an instance, the difference is that you can not create multiple strcuts of this type.
This might be particularly useful when you want to share multiple variables at once between multiple files.
You create one just like a regular struct, but the name is behind the closing bracket, like this:

.. code-block:: javascript

    struct {
      int CoolInt
      string CoolString
    } file
    
Now you do not need to create an instance to give the struct a value:

.. code-block:: javascript

    file.CoolInt = 5
    printt(file.CoolInt)
    >>5

When interacting with this type of struct the same rules apply as for the regular struct.


Complex types can also all be nested.
