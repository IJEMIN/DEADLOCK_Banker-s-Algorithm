import os

class Bankers(object):
    def __init__(self, totalResource):
        #initiating
        self.RESOURCE = totalResource

    def SignProcesses(self, max_, allocated_):
        self.max = max_
        self.allocated = allocated_
        self.need = self.CalcNeed()
        self.avaliable = self.CalcAvaliable()
        self.finished = [False]*len(self.allocated)

    def Difference(self,a,b):
        #return matrix subtracted from a by b
        res = []
        for i in range(len(a)):
            tmp = []
            for j in range(len(a[i])):
                tmp.append(a[i][j]-b[i][j])
            res.append(tmp)
        return res



    def CalcNeed(self):
        #calc request by subtracting signed matrix from max matrix
        return self.Difference(self.max,self.allocated)

    def CalcAvaliable(self):
        """Calc Avaliable Resource"""
        a = self.allocated
        res = []
        for j in range(len(a[0])):
            tmp = 0
            for i in range(len(a)):
                tmp += a[i][j]
            res.append(self.RESOURCE[j] - tmp)
        return res

    def ExecuteProcess(self,index):

        #check if less avaliable than Request
        for i in range(0,len(self.RESOURCE)):
            if self.avaliable[i] < self.need[index][i]:
                #if avaliable source is not enough, HOLD process and insert to the ReadyQ
                return False

        #check END here

        #allocatring what they need.
        for i in range(0,len(self.RESOURCE)):
            self.allocated[index][i] = self.max[index][i]
            self.need[index][i] = 0
            #refreshing need and avaliable matrix
        
        self.avaliable = self.CalcAvaliable()
        return True

    def TempSafeCheckAfterRelease(self):
        #check if at least one request can be done after previous process done. not check whole sequances.
        #if every element of Requests can't accepted after previous process done, this mean it is not safe state
        for i in range(0,len(self.allocated)):
            for k in range (0,len(self.RESOURCE)):
                if self.avaliable[k] >= self.need[i][k]:
                    return True
        return False
       

    def print_matrixes(self):
        print "_____________________________________________"
        print "MAX\t\tAllocated\tNeed"
        for idx in range(len(self.max)):
            print "%s\t%s\t%s" % (self.max[idx],self.allocated[idx], self.need[idx])
        print "_____________________________________________"
        print "Resources:"
        print "Total: %s\tAvailable: %s\n" % (self.RESOURCE, self.avaliable)

    def ReleasingProcess(self,index):
        for i in range(0,len(self.RESOURCE)):
            self.finished[index] = True
            self.allocated[index][i] = 0
        self.avaliable = self.CalcAvaliable()

    def Execute(self):
        i = 0
        while(1):

            

            if self.finished[i] == False:
                print "Executing..."
                print "Request: "
                print self.need[i]
                if self.ExecuteProcess(i):
                    print "Dispatching Done..."

                    self.print_matrixes()

                    print "-----Releasing Process------"

                    self.ReleasingProcess(i)

                    self.print_matrixes()

                    if not (self.TempSafeCheckAfterRelease()):
                        print "SAFE STATE: NOT SAFE - There are no sequances can avoid Deadlock"
                        return False
                else:
                    print "HOLD: not enough Resource"
            
            if i == len(self.allocated)-1:
                i = 0
            else:
                i += 1
            
            check = True
            for k in range(0,len(self.allocated)):
                if self.finished[k] == False:
                    check = False
                    break
            if check == True:
                return True
                break
            #check if every element of Q is false


print "start here"
total_resources = [6, 5, 7, 6]
b = Bankers(total_resources)

max = [
    [3, 3, 2, 2],
    [1, 2, 3, 4],
    [1, 3, 5, 0],
]
allocated = [
    [1, 2, 2, 1],
    [1, 0, 3, 3],
    [1, 2, 1, 0],
]
b.SignProcesses(max, allocated)


b.print_matrixes()
b.Execute()



print ("OTHER CASE")
total_resources = [10, 10, 8, 5]
c = Bankers(total_resources)
max = [
        [10, 8, 2,5],
        [6, 1, 3,1],
        [3, 1, 4,2],
        [5, 4, 2,1]
    ]
allocated = [
        [3, 0, 0,3],
        [1, 1, 2,0],
        [2, 1, 2,1],
        [0, 0, 2,0]
    ]
c.SignProcesses(max, allocated)

c.print_matrixes()
c.Execute()

os.system("pause")