Serverside RUI
======

Northstar 1.10 introduced a server API that allows sending clients messages to display in client predefined RUIs.

Polls
------

.. image:: /_static/serversiderui/vote.png
  :align: center
  :class: screenshot

.. cpp:function:: void function NSCreatePollOnPlayer( entity player, string header, array<string> options, float duration )

.. cpp:function:: int function NSGetPlayerResponse( entity player )

 Large Message
 ------

.. image:: /_static/serversiderui/largemessage.gif
  :align: center
  :class: screenshot
  
.. cpp:function:: void function NSSendLargeMessageToPlayer( entity player, string title, string description, float duration, string image )

Info
------

.. image:: /_static/serversiderui/info.gif
  :align: center
  :class: screenshot

.. cpp:function:: void function NSSendInfoMessageToPlayer( entity player, string text )

PopUp
------

.. image:: /_static/serversiderui/popup.gif
  :align: center
  :class: screenshot

.. cpp:function:: void function NSSendPopUpMessageToPlayer( entity player, string text )

Announcement
------

.. image:: /_static/serversiderui/announcement.gif
  :align: center
  :class: screenshot

.. cpp:function:: void function NSSendAnnouncementMessageToPlayer( entity player, string title, string description, vector color, int priority, int style )

Status
------

.. image:: /_static/serversiderui/status.gif
   :align: center
   :class: screenshot

.. cpp:function:: void function NSCreateStatusMessageOnPlayer( entity player, string title, string description, string id )
.. cpp:function:: void function NSEditStatusMessageOnPlayer( entity player, string title, string description, string id  )
.. cpp:function:: void function NSDeleteStatusMessageOnPlayer( entity player, string id  )
