libAttachSQL 0.9.0 RC - Connection Groups
=========================================

:date: 2014-10-14 17:14
:category: MySQL
:tags: MySQL, libAttachSQL, HP, Advanced Technology Group

It has been just over 4 months since I started working on `libAttachSQL <http://libattachsql.org>`_ for HP's Advanced Technology Group.  Today marks the first (and hopefully only) RC release of the library.

Connection Groups
-----------------

The only real new feature that has been added to 0.9.0 is the concept of connection groups which is something I'm pretty excited about.  Internally libAttachSQL uses event loops to supply the non-blocking API.  Connection Groups join a bunch of connections together into a group that uses a single event loop.  This makes things much more efficient internally and makes applications easier to code too.

Here is a simplified example of how to use it (for a more detailed example see our `example in the documentation <http://docs.libattachsql.org/en/latest/api/examples.html#group-conncetions>`_).

First we need to create the group and add connections to it:

.. code-block:: cpp

   group= attachsql_group_create(NULL);
   con[0]= attachsql_connect_create("localhost", 3306, "test", "test", "testdb", NULL);
   attachsql_group_add_connection(group, con[0], &error);
   attachsql_connect_set_callback(con[0], callbk, &con_no[0]);

The ``con`` array is just an array of connection objects and ``con_no`` is just an array of integers so that the callback that I'll show shortly knows which connection number it is (only useful for displaying in this example).  The last three lines there will be repeated multiple times with different array numbers to add connections.

We now send queries to the connections:

.. code-block:: cpp

   attachsql_query(con[0], strlen(query1), query1, 0, NULL, &error);
   attachsql_query(con[1], strlen(query2), query2, 0, NULL, &error);

And so forth until we have sent a query to all the connections we want.

Finally we want to run the connection group until complete:

.. code-block:: cpp

   while(done_count < 3)
   {
     attachsql_group_run(group);
   }

In this example ``done_count`` is simply a global integer which increments as each callback hits EOF.  You could conceivably run various other parts of your application here and then call ``attachsql_group_run()`` again when ready.

I'm going to paste the whole callback here because it should be mostly self-explanatory, it is called when an event occurs and the code reacts to the event:

.. code-block:: cpp

   void callbk(attachsql_connect_t *current_con, attachsql_events_t events, void *context, attachsql_error_t *error)
   {
     uint8_t *con_no= (uint8_t*)context;
     attachsql_query_row_st *row;
     uint16_t columns, col;
     switch(events)
     {
       case ATTACHSQL_EVENT_CONNECTED:
         printf("Connected event on con %d\n", *con_no);
         break;
       case ATTACHSQL_EVENT_ERROR:
         printf("Error exists on con %d: %d", *con_no, attachsql_error_code(error));
         attachsql_error_free(error);
         break;
       case ATTACHSQL_EVENT_EOF:
         printf("Connection %d finished\n", *con_no);
         done_count++;
         attachsql_query_close(current_con);
         break;
       case ATTACHSQL_EVENT_ROW_READY:
         row= attachsql_query_row_get(current_con, &error);
         columns= attachsql_query_column_count(current_con);
         for (col=0; col < columns; col++)
         {
           printf("Con: %d, Column: %d, Length: %zu, Data: %.*s ", *con_no, col, row[col].length, (int)row[col].length, row[col].data);
         }
         attachsql_query_row_next(current_con);
         printf("\n");
         break;
       case ATTACHSQL_EVENT_NONE:
         break;
     }
   }

The EOF call happens when we reach the end of the result set.  You could easily make this a job server here sending more queries when the previous queries are complete.  ROW_READY should be familiar to anyone who has seen previous examples of libAttachSQL.

Release and Packages
--------------------

libAttachSQL 0.9.0RC is out today, there is a source release as well as packages for RHEL & CentOS 6/7 64bit as well as an Ubuntu PPA 12.04/14.04 32bit and 64bit.  Links to all these can be found on the news section of the `libAttachSQL site <http://libattachsql.org/>`_.

