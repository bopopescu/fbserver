# -*- coding: UTF-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from database import *
from crf import *
import sys, os, math
import numpy as np
import copy
from utilfile import FileUtil

class InstanceFilterData(object):
#     print 'instanace'
    _instance = None
    _lst = []
    _lstFilter = []
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InstanceFilterData, cls).__new__(
                                cls, *args, **kwargs)
            db = Database()
            cls._lst = db.select_filter_el()
            crfWordSeg = CRFWordSegment()
            for x in cls._lst:
                if x != '':
                    segMsg = crfWordSeg.crfpp(x)
#                     print ' '.join(segMsg)
                    cls._lstFilter.append(' '.join(segMsg))
        return cls._instance
    
    def getFilterData(self):
        return self._lstFilter

class CRFWordSegment(object):
    
    def process_ans(self, lst):
        b_str = ''
        ans_str = ''
        for line_data in lst:
            try :
                data = line_data.split('\t')
                b_data = data[3][:-1]
                if b_data == 'B':
                    b_str = b_str + 'B'
                else:
                    b_str = b_str + 'I'
                ans_str = ans_str+data[0]
            except Exception, e:
                b_str = b_str+'B'
                ans_str = ans_str+' '
        return b_str, ans_str
                              

    def crfpp(self, msg):
        crf = CRF()
        fileUtil = FileUtil()
        crf.create_file_input(msg)
        os.system('crf_test -m model1 crf.test.data > crf.result')

        lst = fileUtil.read_file('crf.result')
#         lst = [a for a in lst if a != u'\n']
#         str_ans = reduce(lambda x,y:x+y, [a.split('\t')[0] for a in lst])
         
        # ans = reduce(lambda x,y:x+y, [a.split('\t')[3][:-1] for a in lst])
#         lst_col3 = [a.split('\t')[3][:-1] for a in lst]
        lst_col3, str_ans = self.process_ans(lst)
        lst_ans = [n for (n, e) in enumerate(lst_col3) if e == 'B']
        result_lst = []
        for i in range(len(lst_ans)-1):
            a = lst_ans[i]
            b = lst_ans[i+1]
            result_lst.append(str_ans[a:b])
        result_lst.append(str_ans[b:len(str_ans)])
        return result_lst    

class FilterComputation(object):
    
    def __init__(self):
        pass
        
    def findResutl(self, result):
        for x in result:
            if x > 0.4:
                return 'no'
        return 'yes'
       
    def debugResult(self, result, document):
        for x in range(0, len(result)):
            print ' d ',result[x],' -- ',document[x]
    
    def computeCos(self, message, corpus):
        try:
            crfWordSeg = CRFWordSegment()
            lstInput = crfWordSeg.crfpp(message)
            inMessage = ' '.join(lstInput)
            documents = copy.copy(corpus)
            documents.insert(0, inMessage)
            tfidf_vectorizer = TfidfVectorizer()
            tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
            result_lst = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
            result = result_lst[0]
            return result      
        except Exception as e:
            print e
    
    def invFBFilter(self, message):
        try:
            crfWordSeg = CRFWordSegment()
            lstInput = crfWordSeg.crfpp(message)
            inMessage = ' '.join(lstInput)
            insData = InstanceFilterData()
            lst = insData.getFilterData()
            documents = copy.copy(lst)
            documents.insert(0, inMessage)
            tfidf_vectorizer = TfidfVectorizer()
            tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
            result_lst = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
            result = result_lst[0]
            map = {}
            for x in range(0, len(documents)):
                key = documents[x]
                value = result[x]
                map[key] = value
#             print map
            return map
        except Exception as e:
            print e
        
    def isFilterMessage(self, message):
        try:
            crfWordSeg = CRFWordSegment()
            lstInput = crfWordSeg.crfpp(message)
            inMessage = ' '.join(lstInput)
            insData = InstanceFilterData()
            lst = insData.getFilterData()
            documents = copy.copy(lst)
            documents.insert(0, inMessage)
            tfidf_vectorizer = TfidfVectorizer()
            tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
            result_lst = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
            result = result_lst[0]
#             self.debugResult(result, documents)
            return self.findResutl(result[1:])
#             if b:
#                 return b, data
#             else:
#                 print '******************* else'
#                 maxIndex = max(result)
#                 data = documents[np.where(result == maxIndex)[0][0]]
#                 print 'data : ',data
#                 return b, data
                
        except Exception as e:
            print e
            
# u = unicode('ทดสอบ', 'utf-8')
# filter = FilterComputation()
# filter.isFilterMessage(u)            
