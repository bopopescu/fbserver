from database import Database
from sklearn import metrics
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from filtercomputation import FilterComputation

class OffLine(object):
    db = Database() 
    half = 362
    
    yes = 735
    no = 910
    
    def __init__(self):
        self.prepareData()
        
    def processOffLine(self):
        pass
    
#     def getListTrain(self):
#         sql = "select message from filter_el limit 1, %d"%self.half
#         lstTrain = self.db.select_q(sql)
#         return lstTrain
#     
#     def getListTest(self):
#         sql = "select sholdbe, message from filter_el limit %d, %d"%(self.half+1, self.half*2)
#         lstTest = self.db.select_q(sql)
#         return lstTest
    
    def prepareData(self):
        sql1no = "select message from filter where sholdbe = 'no' limit 1,900"
        sql2no = "select sholdbe, message from filter where sholdbe ='no' limit 901, 950"
        sql2yes = "select sholdbe, message from filter where sholdbe = 'yes' limit 1,50"
        self.lstTrain = self.db.select_inv_fbfiler(sql1no)
        self.lstTest = self.db.select_q(sql2no)
        self.lstTest.extend(self.db.select_q(sql2yes))
    
    def computeWithNoCorpus(self, message, corpus, d):
        cosSim = FilterComputation()
        distance = cosSim.computeCos(message, corpus)
        for x in distance[1:]:      
            if x > d:
#                 print 'x ',x,' d ',d
                return 'no'
        return 'yes'
    
    def scoreConvert(self, score):
        if score == 'yes':
            return 1
        else:
            return 0
    
    def findBestDistance(self):
        print '*** start ****'
        d = 0.1
#         y_true = []
#         y_pred = []
        result = {}
        for x in range(0,10):
            y_true = []
            y_pred = []
            for dataIndex in range(0, len(self.lstTest)):
                dataTest = self.lstTest[dataIndex]
#                 y_true.append(dataTest[0])
                y_true.append(self.scoreConvert(dataTest[0]))
                isFilter = self.computeWithNoCorpus(dataTest[1], self.lstTrain, d)
                y_pred.append(self.scoreConvert(isFilter))
            print y_true
            print y_pred
            f1 = metrics.f1_score(y_true, y_pred)
            f1_mac = f1_score(y_true, y_pred, average='macro') 
            print 'd : ',d,' f1 : ',f1,' f1 mac : ',f1_mac
            result[d] = f1
            print classification_report(y_true, y_pred)
#             print 'result ', result
            d = d+0.1
        print result
        print '*** end ******'
    
offLine = OffLine()
# lst = offLine.getListTest()
# print lst[0]
offLine.findBestDistance()