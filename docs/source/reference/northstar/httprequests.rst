HTTP Requests
=============

As of v1.12.0, you can now make HTTP requests from Squirrel scripts.
HTTP requests allow you to query online APIs, and retrieve data. 

This is particularly useful for custom APIs you might want to build for your servers, for instance if you want to wrap 
a database with an API so that your servers can save player stats.

Security Limitations
====================

For security reasons, private network hosts are blocked by default, meaning you cannot make HTTP requests to them.
This includes a blanket ban on IPv6 hosts.

You are also limited to HTTP and HTTPS for protocols. Any other protocols will prevent the request from being made.

Launch Arguments
^^^^^^^^^^^^^^^^

There are a few launch arguments you may use to bypass some of the limitations, or outright disable HTTP requests.

These should be applied to your client or server's launch commandline.

.. list-table:: Launch Arguments

    * - Name
      - Description
    * - ``-allowlocalhttp``
      - Disables private network checks for HTTP requests, allowing any IPv4 and IPv6 host to be used.
    * - ``-disablehttprequests``
      - Disables HTTP requests. Any attempts at making requests will fail.
    * - ``-disablehttpssl``
      - Disables SSL verifications, useful when the host's SSL certificate is invalid, and insecure HTTP cannot be used.

