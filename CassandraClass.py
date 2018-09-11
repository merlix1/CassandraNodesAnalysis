import re

class Table:
    def __init__(self,name):
        self.name=name
        self.data={}
        
    def add_spaceusedtotal(self,space):
        self.spaceusedtotal=space
    def add_localwritelatency(self,lwlatency):
        self.localwritelatency=lwlatency


class KeySpace:
    def __init__(self,key):
        self.listtable=[]
        self.name=key
        
    def add_table(self, table):
        tmptable=Table(table)
        self.listtable.append(tmptable)


    def get_tablecolumnvalue(self, column):
       
        tmpmap={}
        
        for intable in self.listtable:
            tmpmap[intable.name]=intable.data[column]
        return tmpmap

    
        

class Cassandra:
    def __init__(self):
        self.listkeyspace=[]
        
        
    def add_keyspace(self, key):
        tmpkeyspace=KeySpace(key)
        self.listkeyspace.append(tmpkeyspace)

    def populate(self, file):

        self.name=file.name
        print("the name of the file is:"+self.name)
        
        patternKeyspace = re.compile('Keyspace: (.+)')
        patternTable = re.compile('		Table: (.+)')
        patternSpaceUsedTotal=re.compile('Space used \(total\): (\d+)')
        patternLocalwritelatencynan=re.compile('Local write latency: NaN')
        patternLocalwritelatency=re.compile('Local write latency: (\d+\.\d+)')
        patternDecimalExtraction=re.compile('(\d+\.\d+)')
        patternIntegerExtraction=re.compile('(\d+)')
        
        #Populating the cassandra instance.

        intable=False
        intableline=0
        for line in file:
            
            m=patternKeyspace.match(line)
            if m:
                #Adding KeySpace to Cassandra db
                self.add_keyspace(m.group(1))
                
            t=patternTable.match(line)
            if t:
                #Adding table to Keyspace
                
                self.listkeyspace[-1].add_table(t.group(1))
                intable=True

            if(intable):
                intableline=intableline+1
                #print(line)
                #print(intableline)
                
                tmpdata=line[line.index(':'):]
                ##print("data before"+tmpdata)
                #remove non alpha numerical character at begnining
                tmpdata=re.sub("[^0-9\.]", "", tmpdata)
                ##print("data middle"+tmpdata)
                #need to make sure data convertible to int
                k=patternDecimalExtraction.match(tmpdata)
                l=patternIntegerExtraction.match(tmpdata)
               
                if l:
                    tmpdata=l.group(1)
                else:
                    tmpdata=1

                #print("data after"+str(tmpdata))
                
                self.listkeyspace[-1].listtable[-1].data[line[:line.index(':')]]=tmpdata
                
                if(intableline==25):
                   intable=False
                   intableline=0
                   
                
                
            s=patternSpaceUsedTotal.search(line)

            #Adding space used total
            if s:
                self.listkeyspace[-1].listtable[-1].add_spaceusedtotal(s.group(1))

            s1=patternLocalwritelatencynan.search(line)
            

            if s1:
                self.listkeyspace[-1].listtable[-1].add_localwritelatency('0')
                
            else:
                s2=patternLocalwritelatency.search(line)
                if s2:
                   
                    self.listkeyspace[-1].listtable[-1].add_localwritelatency(s2.group(1))
            

class cassandraCluster:
        def __init__(self,name):
            self.listcassandranode={}
            self.name=name

        def add_cassandraNode(self, node):
            self.listcassandranode[node.name]=node

     
            
                
