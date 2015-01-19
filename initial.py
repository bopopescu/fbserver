from utilfile import *
from sklearn.svm import SVC
import numpy as np

class FBInit(object):
    
    _instance = None
    dict = []
    clf = SVC()
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print 'fb init instance'
            cls._instance = super(FBInit, cls).__new__(
                                cls, *args, **kwargs)
            fileUtil = FileUtil()
            cls.dict = [a.encode('utf-8')[:-1] for a in fileUtil.read_file('dict/tdict.txt')]
            cls.dict.extend([a.encode('utf-8')[:-1] for a in fileUtil.read_file('dict/eng.txt')])
            
            x_train = np.loadtxt('data/fselect.txt', delimiter=',', dtype=int)
            y_train = np.loadtxt('data/fresult.txt', dtype=int)
            cls.clf = cls.clf.fit(x_train, y_train)
        return cls._instance
