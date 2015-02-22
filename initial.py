from utilfile import *
from config import Config
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
            cls.dict = [a.encode('utf-8')[:-1] for a in fileUtil.read_file(Config.base_dir+'dict/tdict.txt')]
            cls.dict.extend([a.encode('utf-8')[:-1] for a in fileUtil.read_file(Config.base_dir+'dict/eng.txt')])
            
            x_train = np.loadtxt(Config.base_dir+'data/fselect.txt', delimiter=',', dtype=int)
            y_train = np.loadtxt(Config.base_dir+'data/fresult.txt', dtype=int)
            cls.clf = cls.clf.fit(x_train, y_train)
        return cls._instance
