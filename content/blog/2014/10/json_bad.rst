Why JSON is bad for applications
================================

:date: 2014-10-31 15:22
:category: General
:tags: HP, Advanced Technology Group

Today I read an article about how company X has improved things by amongst other things ditching JSON after 2 years of using it.  Before I start on this subject I should say that JSON does have its place.  If you have a web application where a browser is talking to a web server and in particular uses JavaScript then JSON is a good fit.

I've discussed this issue several times before with `Brian Aker <http://krow.net/>`_ who works with me at HP's Advanced Technology Group and in the past I have been hit with the issues I'm going to talk about here.

JSON is human readable and easy to parse, that cannot be denied and for prototyping is good in a pinch.  The first problem comes when you need to validate data.  I've been stung many times by one end trying to read/write the JSON in a slightly different format to the other end, the end result is always not pretty.  This is one advantage that XML and SOAP has going for it over JSON since validation is easier.  I'm personally not a fan of XML but there are many who are.

There are additional problems when you start using mobile platforms.  Mobile networks are unreliable, you may have a good 3G signal but it is possible to only get dial-up speed through it due to all the other users.  JSON is verbose, XML more so which requires more data transfer.  Whilst this can be resolved with protocol compression it will require additional decoding on the client side to do this.  In addition data conversion will be needed in many cases for numeric fields.

The biggest problem with JSON is versioning.  As you add more features to your application there will likely come a time where you need to change the data structure for your messages.  Often you can't guarantee that your client is using the same version of the software as your server so backwards and forwards compatibility problems can arise.  Resolving these often makes the JSON messages very complex to create and decode.  This is not as much of a problem for web applications because the browser usually grabs an update version of the JavaScript on execution.  So changing the data format at any time is easy as long as both ends agree on the format.

The solution
------------

For many applications the data you are sending is directly from a database or at least data that has been modified since being read from a database.  So you will likely want the data model for your messages to match this as much as possible.  This is where `Google's Protocol Buffers <https://developers.google.com/protocol-buffers/>`_ fit nicely.

Protocol Buffers allow you to specify a schema for the data in a human readable format, it actually looks a little like a database schema.  They will automatically validate the data for you and have versioning built-in.  This means you can make your code easily backwards and forwards compatible.

There is a positive and negative side to the data transfer of Protocol Buffers.  It is a binary protocol.  This means it takes up minimal bandwidth on the wire but also means that it is very hard to interpret the data without the schema.  The same could be said if you were given InnoDB table data without the schemas.  It also means it may be possible to compress the data further with something like LZO or DEFLATE.

I recommend application developers consider Protocol Buffers instead of JSON when they are next developing a server/client application.
