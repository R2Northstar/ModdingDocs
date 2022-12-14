HTTP Requests
=============

As of v1.12.0, you can now make HTTP requests from Squirrel scripts.
HTTP requests allow you to query online APIs, and retrieve data. 

This is particularly useful for custom APIs you might want to build for your servers, for instance if you want to wrap 
a database with an API so that your servers can save player stats.

.. warning::
    
    For security reasons, private network hosts, such as ``localhost`` or ``192.168.1.106`` are blocked by default, meaning you cannot make HTTP requests to them.
    This includes a blanket ban on IPv6 hosts.

    You are also limited to ``HTTP`` and ``HTTPS`` for protocols. Any other protocols will prevent the request from being made.

Launch Arguments
----------------

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


HTTP API
--------

This section documents all the available functions, structs and enums used to make HTTP request in Squirrel scripts.

.. warning::

    HTTP requests are multithreaded, as such they will run in the background until completion, whether successful or failed.
    Be mindful of how many requests you make at a time, as you may potentially get ratelimited or blacklisted by the remote host.

Data
^^^^

The HTTP system uses a few enums and structs for requests and their callbacks.

.. _httpapi_enums_httpmethod:

.. cpp:enum:: HttpRequestMethod

    Contains the different allowed methods for a HTTP request. Please work.

    .. cpp:member:: GET

        Uses the ``GET`` HTTP method for the request.
        
	.. cpp:member:: POST

        Uses the ``POST`` HTTP method for the request.
	.. cpp:member:: HEAD

        Uses the ``HEAD`` HTTP method for the request.
	.. cpp:member:: PUT

        Uses the ``PUT`` HTTP method for the request.
	.. cpp:member:: DELETE

        Uses the ``DELETE`` HTTP method for the request.
	.. cpp:member:: PATCH

        Uses the ``PATCH`` HTTP method for the request.
	.. cpp:member:: OPTIONS
        
        Uses the ``OPTIONS`` HTTP method for the request.


.. _httpapi_structs_request:

.. cpp:struct:: HttpRequest

    Contains the settings for a HTTP request. This is used for the more flexible :ref:`NSHttpRequest <>` function.

	.. cpp:var:: int method

        :ref:`HTTP method <_httpapi_enums_httpmethod>` used for this HTTP request.
	.. cpp:var:: string url

        Base URL of this HTTP request.
	.. cpp:var:: table< string, array< string > > headers

        Headers used for this HTTP request. Some may get overridden or ignored.
	.. cpp:var:: table< string, array< string > > queryParameters

        Query parameters for this HTTP request.
	.. cpp:var:: string contentType = "application/json; charset=utf-8"

        The content type of this HTTP request. Defaults to application/json & UTF-8 charset.
	.. cpp:var:: string body

        The body of this HTTP request. If set, will override queryParameters.
	.. cpp:var:: int timeout = 60

        The timeout for this HTTP request in seconds. Must be between 1 and 60
	.. cpp:var:: string userAgent
        If set, the override to use for the User-Agent header.