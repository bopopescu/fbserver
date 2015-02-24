from pymongo import MongoClient
import json
class BaseCloud(object):
    
    def __init__(self):
        self.conn = MongoClient('mongodb://ds047591.mongolab.com:47591/cloudkey')
#         self.collection = self.db.cloud

class CloudKey(BaseCloud):

    def __init__(self):
        super(CloudKey, self).__init__()
        self.collection_key = self.db.cloud_key
    
    def insert_key(self, key, data):
        data['key'] = key
        self.collection_key.insert(data)
        
    def find(self, key):
        ret = []
        data = {}
        data['key'] = key
        for i in self.collection_key.find(data):
            del i['_id']
            del i['key']
            del i['user_name']
            ret.append(i)
        return ret

class CloudUser(BaseCloud):
    
    def __init__(self):
        super(CloudUser, self).__init__()
        self.collection_user = self.db.user_profile
    
    def insert_user(self, user_name):
        data_ins = {}
        data_ins['user_name'] = user_name
        self.collection_user.insert(data_ins)

#role,1,
#user,    
    def check_user(self, user_name):
        data_find = {}
        data_find['user_name'] = user_name
        if self.collection_user.find(data_find).count() > 0:
            return True
        else:
            return False

if __name__ == '__main__':
    cloud_user = CloudUser()
    print cloud_user.check_user('off')
    
    