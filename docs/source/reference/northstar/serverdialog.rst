Server dialog
============

Server dialog is a way for servers to create a dialog window with the option of up to 4 buttons.

Functions
---------

**Definition:**

.. cpp:function:: void NSSendServerDialog( entity player, ServerDialogData dialog )

Shows the given player the dialog with the data from the struct.

**Example:**

.. code-block::

    ServerDialogData dialog
    dialog.message = "Hello there"
    foreach( entity player in GetPlayerArray() )
        NSSendServerDialog(player, dialog)

**Definition:**

.. cpp:function:: void NSSendMessageServerDialog( entity player, string message )

Send a dialog to a player with only the given message as data.

**Example:**

.. code-block:: javascript

    void function SendMessageToAll()
    {
        foreach(entity player in GetPlayerArray() )
            NSSendMessageServerDialog( player, "Hello There" )
    }

**Definition:**

.. cpp:function:: void NSAddDialogButton( ServerDialogData dialog, string text, void functionref( entity ) callback )

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
            NSSendServerDialog(player, dialog)
    }

Code example
------------

the folowing code produces this output: 

.. code-block::

    ServerDialogData dialog
    dialog.header = "This is the header"
    dialog.message = "this is the body, it is green \n \n Hello There \n \n General Kenobi"
    dialog.messageColor = [0,200,0,100]
    dialog.showSpinner = true
    dialog.showPCBackButton = true
    AddDialogButton( dialog, "Button 1 %%$r2_ui/menus/loadout_icons/primary_weapon/primary_kraber%%", ButtonImcPressed )
    SendServerDialog( player, dialog )


.. figure:: /_static/serverdialog/dialogexample.png
  :align: center
  :class: screenshot

Dialog struct
-------------

All the data in the struct that can be changed by the server.

===================================================       =========================================================================
Name of the struct content and standard value              description of the content
===================================================       =========================================================================
``string header = " "``                                   The headline of the struct.
``string message = " "``                                  The body of text under the headline, it supports newline with ``\n``.
``array<int> messageColor = [161, 161, 161, 255]``        The colour of the message body, in the format of RGBA, if less than 4 values are given the value defaults to 100, additional values are ignored.
``string image = "."``                                    Path to the asset of the image displayed on the left of the text body
``string rightImage = "."``                               Path to the asset of the image displayed on the right of the text body
``bool forceChoice = false``                              unknown 
``bool noChoice = false``                                 unknown
``bool noChoiceWithNavigateBack = false``                 unknown
``bool showSpinner = false``                              Sets the left image as an animated spinner 
``bool showPCBackButton = false``                         Shows an additional button below all other buttons that closes the dialog for the client when pressed, works the same as pressing the ``esc`` button.
``float inputDisableTime = 0``                            How long it takes before the client is able to press a button
``bool darkenBackground = false``                         Darkens the colour of the dialog window slightly
``bool useFullMessageHeight = false``                     Creates a larger dialog window even if there is no text or buttons to fill that space
``array<ServerDialogButtonData> buttonData``              Stores the information added by the ``AddDialogButton`` function 
===================================================       =========================================================================