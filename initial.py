from utilfile import *

class FBInit(object):
    
    _instance = None
    th_dict = []
    en_dict = []
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print 'fb init instance'
            cls._instance = super(FBInit, cls).__new__(
                                cls, *args, **kwargs)
            fileUtil = FileUtil()
            cls.th_dict = [a.encode('utf-8')[:-1] for a in fileUtil.read_file('tdict.txt')]
        return cls._instance
