# CassandraNodesAnalysis



In a context of a performance issue related to Cassandra, it is good to check if nodes are unbalanced.

Cassandra provide a command "nodetool cfstats". This helps but in the context of numerous node it gets tedious to check this log for each node and do comparison.

 

I attach below a rough utility to parse cftats logs. There are much better tool to monitor Cassandra performance itself but this helps investigated a Cassandra node we don't have access to.

 

Please also note the utility is showing only data in the "data" keyspace ( keyspace being similar to schema in relational database) used in my projects.

If you don't see the expected table then it's possible the wrong keyspace was picked up by the utility. 

 

This utility helps for instance to quickly determine biggest table in Cassandra and how the load is spread around the cluster:

 

![alt text](https://github.com/merlix1/CassandraNodesAnalysis/blob/master/screenshot.png)

 

Installation instruction are:

 

Install python.

IMPORTANT: python 3 or above  is required. Download the right version.

 

 

https://www.python.org/downloads/

Check python can be executed.

 

 

Then run following commands to import package needed by this utility:

python -mpip install -U pip

python -mpip install -U matplotlib

 

 

Then open python IDE.

Do File->Open, find xavCassandraNodeAnalysis2.

 

 

Then edit path in xavCassandraNodeAnalysis2 file to refer to your files which contains result from running "nodetool cfstats" on each PRPC node:

 

 

path=['C:/python/Logs/3502/before-AFO-i-3502-15.txt',\
      'C:/python/Logs/3503/before-AFO-i-3503-16.txt',\
      'C:/python/Logs/3504/before-AFO.txt',\
      'C:/python/Logs/3505/before-AFO.txt',\
      'C:/python/Logs/4171/before-AFO.txt'
      ]

 

Do "F5" to run it
