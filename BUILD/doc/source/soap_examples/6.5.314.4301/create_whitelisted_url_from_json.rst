
Create Whitelisted Url From JSON
==========================================================================================

Get a whitelisted url object, add ' API TEST' to the url_regex of the whitelisted url object, delete any pre-existing whitelisted url with the new url_regex, then create a new whitelisted url object with the new url_regex


Step 1 - Authenticate to the SOAP API via /auth
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/auth
* HTTP Method: GET
* Elapsed Time: 0:00:00.007380
* `Step 1 Request Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_1_request.txt>`_
* `Step 1 Response Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_1_response.txt>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip, deflate", 
      "Connection": "keep-alive", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "password": "VGFuaXVtMjAxNSE=", 
      "username": "QWRtaW5pc3RyYXRvcg=="
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-length": "135", 
      "content-type": "text/plain; charset=us-ascii"
    }


Step 2 - Get the server version via /info.json
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/info.json
* HTTP Method: GET
* Elapsed Time: 0:00:00.006730
* `Step 2 Request Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_2_request.txt>`_
* `Step 2 Response Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_2_response.json>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip, deflate", 
      "Connection": "keep-alive", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6922-c6924768f0749f065a818926b06de2a4da74c8f3d64ad752386557a9d4f379fb3163056e554fd9456cbbf5312d38b3a58994b4ee3cc7a51655f4cdf0f4bdf31c"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-length": "86180", 
      "content-type": "application/json"
    }


Step 3 - Issue a GetObject to find an object
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.287918
* `Step 3 Request Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_3_request.xml>`_
* `Step 3 Response Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_3_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "480", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6922-c6924768f0749f065a818926b06de2a4da74c8f3d64ad752386557a9d4f379fb3163056e554fd9456cbbf5312d38b3a58994b4ee3cc7a51655f4cdf0f4bdf31c"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-encoding": "gzip", 
      "content-type": "text/xml;charset=UTF-8", 
      "transfer-encoding": "chunked"
    }


Step 4 - Issue a GetObject to find the object to be deleted
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.275546
* `Step 4 Request Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_4_request.xml>`_
* `Step 4 Response Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_4_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "480", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6922-c6924768f0749f065a818926b06de2a4da74c8f3d64ad752386557a9d4f379fb3163056e554fd9456cbbf5312d38b3a58994b4ee3cc7a51655f4cdf0f4bdf31c"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-encoding": "gzip", 
      "content-type": "text/xml;charset=UTF-8", 
      "transfer-encoding": "chunked"
    }


Step 5 - Issue a DeleteObject to delete an object
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.009114
* `Step 5 Request Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_5_request.xml>`_
* `Step 5 Response Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_5_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "538", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6922-c6924768f0749f065a818926b06de2a4da74c8f3d64ad752386557a9d4f379fb3163056e554fd9456cbbf5312d38b3a58994b4ee3cc7a51655f4cdf0f4bdf31c"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-length": "957", 
      "content-type": "text/xml;charset=UTF-8"
    }


Step 6 - Issue an AddObject to add an object
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.022226
* `Step 6 Request Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_6_request.xml>`_
* `Step 6 Response Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_6_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "575", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6922-c6924768f0749f065a818926b06de2a4da74c8f3d64ad752386557a9d4f379fb3163056e554fd9456cbbf5312d38b3a58994b4ee3cc7a51655f4cdf0f4bdf31c"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-length": "866", 
      "content-type": "text/xml;charset=UTF-8"
    }


Step 7 - Issue a GetObject on the recently added object in order to get the full object
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.001966
* `Step 7 Request Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_7_request.xml>`_
* `Step 7 Response Body <../_static/soap_outputs/create_whitelisted_url_from_json_step_7_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "589", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6922-c6924768f0749f065a818926b06de2a4da74c8f3d64ad752386557a9d4f379fb3163056e554fd9456cbbf5312d38b3a58994b4ee3cc7a51655f4cdf0f4bdf31c"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-length": "837", 
      "content-type": "text/xml;charset=UTF-8"
    }


.. rubric:: Footnotes

.. [#] this file automatically created by BUILD/build_api_examples.py