import re

import CassandraClass
import MainView

path=[]



path=['C:/PegaDoc/python/Logs/3502/before-AFO-i-3502-15.txt',\
      'C:/PegaDoc/python/Logs/3503/before-AFO-i-3503-16.txt',\
      'C:/PegaDoc/python/Logs/3504/before-AFO.txt',\
      'C:/PegaDoc/python/Logs/3505/before-AFO.txt',\
      'C:/PegaDoc/python/Logs/4171/before-AFO.txt'
      ]




cassandraclusterinstance=CassandraClass.cassandraCluster('folder1')
for idx, pathrow in enumerate(path):
    file=open(pathrow,'r')
    cassandrainstance=CassandraClass.Cassandra()
    cassandrainstance.populate(file)
    cassandraclusterinstance.add_cassandraNode(cassandrainstance)
    






clusterlist={}
clusterlist['folder1']=cassandraclusterinstance

mainviewinst5ance=MainView.MainView(clusterlist)







