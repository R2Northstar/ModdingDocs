Server dialog
============

Server dialog is a way for servers to create a dialog window with the option of up to 4 buttons.

Functions for starting a dialog on a player.

**Definition:**

.. cpp:function:: void SendServerDialog( entity player, ServerDialogData dialog )

Shows the given player the dialog with the data from the struct.

**Example:**

.. code-block:: javascript

    ServerDialogData dialog
    dialog.message = "Hello there"
    foreach( entity player in GetPlayerArray() )
        SendServerDialog(player, dialog)

**Definition:**

.. cpp:function:: void SendMessageServerDialog( entity player, string message )

Send a dialog to a player with only the given message as data.

**Example:**

.. code-block:: javascript

    void function SendMessageToAll()
    {
        foreach(entity player in GetPlayerArray() )
            SendMessageServerDialog( player, "Hello There" )
    }

.. figure:: /_static/serverdialog/messageexample.png
  :align: center
  :class: screenshot

**Definition:**

.. cpp:function:: void AddDialogButton( ServerDialogData dialog, string text, void functionref( entity ) callback )

Add one button to the given struct, the text is localised. The callback function is called when the player the dialog is send to clicks the button

**Example:**

.. code-block:: javascript

    void function SendDialogToAll()
    {
        ServerDialogData dialog
        dialog.message = "Hello there"
        AddDialogButton(dialog, "Button 1 %%$r2_ui/menus/loadout_icons/primary_weapon/primary_kraber%%", void function(entity player):() {
            printt(player.GetPlayerName(), " pressed button 1" )
        })
        foreach( entity player in GetPlayerArray() )
            SendServerDialog(player, dialog)
    }

.. figure:: /_static/serverdialog/buttonexample.png
  :align: center
  :class: screenshot

Dialog struct
-------------

All the data in the struct that can be changed by the server.

* ``string header = " "``
The headline of the struct.

* ``string message = " "``
The body of text under the headline, it supports newline with ``\n``.

* ``array<int> messageColor = [161, 161, 161, 255]``
The colour of the message body, in the format of RGBA, if less than 4 values are given the value defaults to 100.

* ``string image = "."``
Path to the asset of the image displayed on the left of the text body

* ``string rightImage = "."``
Path to the asset of the image displayed on the right of the text body

* ``bool forceChoice = false``

* ``bool noChoice = false``

* ``bool noChoiceWithNavigateBack = false``

* ``bool showSpinner = false``

* ``bool showPCBackButton = false``

* ``float inputDisableTime = 0``

* ``bool darkenBackground = false``

* ``bool useFullMessageHeight = false``

* ``array<ServerDialogButtonData> buttonData``
Stores the information added by the ``AddDialogButton`` function 
