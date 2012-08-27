.. _api-overview:

===================
Overview and Basics
===================

.. warning::
  The Kegbot Web API is a work in progress. It should not be considered stable
  until Kegbot Server v1.0 is released.

Quick Examples
==============

Itching to get started? Here are some quick, real-life examples.  For the full
listing of API endpoints and actions, see :ref:`api-endpoints`.

Get tap status
--------------

.. code-block:: javascript

  $ curl http://demo.kegbot.org/api/taps

Record a drink (anonymous user)
-------------------------------

.. code-block:: javascript

  $ curl http://demo.kegbot.org/api/taps/kegboard.flow0 \
    -F ticks=100

Record a drink (specific user)
------------------------------

.. code-block:: javascript

  $ curl http://demo.kegbot.org/api/taps/kegboard.flow0 \
    -F ticks=100 \
    -F username=mikey

Authenticate a token
--------------------

.. code-block:: javascript

  $ curl http://demo.kegbot.org/api/auth-tokens/rfid.1234/?api_key=abcd


URL Scheme
==========

Endpoints in the Kegbot API follow a predictable URL scheme whenever possible.
The general convention is ``/<noun>/<id>/``, or ``/<noun>/<id>/<subresource>/``.

The ``noun`` portion is typically a *pluralized* core Kegbot data type: "kegs",
"drinks", and so on.  The ``id`` portion is a unique identifier for that type of
noun (typically a string or opaque id).  For example, ``/users/mikey`` returns
basic information about that user, and ``/users/mikey/drinks`` returns his
detailed drink list.

In most places, ``id`` can be omitted in order to return a bulk listing for that
resource type.  For example, ``/kegs/12`` lists details about about eg #12, and
``/kegs`` lists all kegs.


Data Format
===========

The response from an endpoint is a JSON dictionary.  Normal (non-error)
responses always contain a single top-level entry named ``result``, containing
the endpoint's response data as specified in :ref:`api-endpoints`.

Dates and times are always expressed in the UTC time zone, in ISO8601 string
format.

Error Handling
==============

If an error occurred or the request could not be processed, the response will
instead have the top-level field ``error``, as shown below:

.. code-block:: javascript
  
  {
    "error" : {
      "code" : "PermissionDenied",
      "message" : "You do not have permission to view this resource."
    }
  }

The ``code`` field lists a specific error code, and the ``message`` field
contains a human-readable explanation.  For a complete list of possible error
codes, see :ref:`api-error-codes`.

In addition to the Kegbot error codes, the API server will also use HTTP status
codes to indicate success (200) or failure (400).  Clients *must* handle
non-200 responses, which may be caused by heavy load, server error, or other
exceptional circumstances.

.. _api-pagination:

Pagination
==========

In some cases, Kegbot limits the number of records it will return in a single
query.  For these queries, an additional top-level field ``paging`` will appear
in a successful response.  See the :ref:`api-drink-list` section for an
example.

Most endpoints do *not* paginate their results; those that do must specify this
behavior.

.. _api-security:

Security & Authentication
=========================

An endpoint will be in one of two modes:

* **Open.** Anyone can navigate to the endpoint and read its data.
* **Restricted.** An API key is required to read or update the endpoint.

.. note::
  When the Kegbot's privacy settings are set to "Members Only", **Open**
  endpoints can only be accessed while logged in *or* with an API key.

All staff and superuser accounts are granted API keys.  The key can be
found (or reset) by logging in to the account profile page.  Example value:

  100000018fe5b1e373a18d7dbb3e51917058aaa7

This token can be supplied multiple ways:

* **HTTP Request Header:** ``X-Kegbot-Api-Key`` (preferred)
* **HTTP GET/POST Parameter:** ``api_key``

Publishing
==========

In addition to reading and querying data, the web API can be used for inserting
and modifying records.  These are implemented as HTTP ``POST`` operations.

