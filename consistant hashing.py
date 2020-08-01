import random
import math
class servers:
    def __init__(self,servers):
        self.servers=servers
        self.active=[True for i in range(self.servers)]
    def shut(self,var):
        if var>=self.servers:
            return "Invalid number"
        else:
            self.active[var]=False
    def start(self,var):
        if var<self.servers:
            self.active[var]=True
        else:
            self.servers+=1
            self.active.append(True)
class req:
    def __init__(self,num):
        self.id=random.randint(1,100)
        self.requests=[random.randint(100,1000) for i in range(self.id)]
        self.cluster=servers(num)
    def run(self):
        pass
    def hash_func(self,var2):
        var2=(var2*23*17)%self.id
        return var2
    def l_hash(self,var):
        l=len(self.requests)
        temp=var*23*19*13
        temp=temp/(17*41)
    def hash(self):
        self.num_hash=math.log(self.id,self.cluster.servers)
        self.hashes=[]
        for i in range(self.cluster.servers):
            self.hashes.append(self.hash_func(i))
        h_max=max(self.hashes)
        for i in range(self.cluster.servers):
            self.hashes[i]=int(self.hashes[i]*(max(self.requests)-1)/h_max)
    def print(self):
        print(self.cluster)
        print(self.cluster.servers)
        print(self.cluster.active)
        print(self.requests)
        print(self.hashes)
        print(self.output)
    def put(self):
        a={i:[] for i in range(self.cluster.servers)}
        end,index=max(self.hashes),self.hashes.index(max(self.hashes))
        servers=[0 for i in range(1000)]
        for i in range(self.cluster.servers):
            print(len(servers))
            print(self.hashes)
            servers[self.hashes[i]]=i
        for i in range(len(self.requests)):
            if self.requests[i]>= end:
                a[0].append(self.requests[i])
            else:
                j=self.requests[i]
                while servers[j]==0:
                    j+=1
                a[servers[j]].append(self.requests[i])
        self.output=a

a=req(5)
a.hash()
a.put()
a.print()