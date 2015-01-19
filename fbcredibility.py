from base import BaseFBWeb
from utilfile import FileUtil
from database import Database
from initial import FBInit
import os

svm_path = '/home/ubuntu/liblinear-ovo-1.94'
is_db_save = True

class FBCredibility(BaseFBWeb):
    def __init__(self, request):
        self.request = request
    
    def get_credibility(self):
        likes = self.request.args.get('likes')
        comments = self.request.args.get('comments')
        shares = self.request.args.get('shares')
        url = self.request.args.get('url')
        hashtag = self.request.args.get('hashtag')
        images = self.request.args.get('images')
        vdo = self.request.args.get('vdo')
        location = self.request.args.get('location')
        return_id = self.request.args.get('return_id')
        data = {}
        map_result = {}
        map_result['return_id'] = int(return_id)
        map_result['status'] = 0
        data['like_number'] = likes
        data['comment'] = comments
        data['share'] = shares
        data['url'] = url
        data['hashtag'] = hashtag
        data['image'] = images
        data['vdo'] = vdo
        data['is_location'] = location
        lst = []
        lst.append(likes)
        lst.append(comments)
        lst.append(shares)
        lst.append(url)
        lst.append(hashtag)
        lst.append(images)
        lst.append(vdo)
        lst.append(location)
#         input_data= '{},{},{},{},{},{},{},{}'.format(likes, comments, shares, url, hashtag, images, vdo, location)
        y = FBInit.clf.predict(lst)
#         print 'y ', y
#         file_util = FileUtil()
#         file_util.write_input_file2(data, svm_path)
#         command = '{}/predict /tmp/test {}/data/model1 {}/data/predict'.format(svm_path, svm_path, svm_path)
#         os.system(command)
#         out_data = file_util.read_result(svm_path+'/data/predict')
        rating = 10
        map_result['rating'] = int(y)
        return map_result
    
    def get_feedback(self):
        return_id = self.request.args.get('return_id')
        map_result = {}
        
        if is_db_save :
            data = {}
            data['feed_back'] = self.request.args.get('feedback')
            data['like_number'] = self.request.args.get('likes')
            data['comment'] = self.request.args.get('comments')
            data['share'] = self.request.args.get('shares')
            data['url'] = self.request.args.get('url')
            data['hashtag'] = self.request.args.get('hashtag')
            data['image'] = self.request.args.get('images')
            data['vdo'] = self.request.args.get('vdo')
            data['is_location'] = self.request.args.get('location')
            data['user_post'] = self.request.args.get('user_post')
            data['user_feed_back'] = self.request.args.get('user_feed_back')
            data['message'] = self.request.args.get('message')
            data['rating'] = self.request.args.get('rating')
            db = Database()
            db.insert_feedback(data)
            db.close()
            db.close_connection()
            map_result['status'] = 1
        else :
            map_result['status'] = 0
    
        map_result['return_id'] = int(return_id)
        map_result['description'] = 'Thank'
        return map_result
      
class FBCredibilityEL(BaseFBWeb):
    
    def __init__(self, request):
        self.request = request

    def evaluator_credibility(self):
        likes = self.request.args.get('likes')
        comments = self.request.args.get('comments')
        shares = self.request.args.get('shares')
        url = self.request.args.get('url')
        hashtag = self.request.args.get('hashtag')
        images = self.request.args.get('images')
        vdo = self.request.args.get('vdo')
        return_id = self.request.args.get('return_id')
        rating = self.request.args.get('rating')
        location = self.request.args.get('location')
        user_name = self.request.args.get('user_name')
        
        map_result = {}
        map_result['return_id'] = int(return_id)
        map_result['status'] = 0
        
        data = {}
        data['like_number'] = likes
        data['comment'] = comments
        data['share'] = shares
        data['url'] = url
        data['rating'] = rating
        data['hashtag'] = hashtag
        data['image'] = images
        data['vdo'] = vdo
        data['is_location'] = location
        data['user_name'] = user_name
        
        db = Database()
        db.insert2(data)
        db.close()
        db.close_connection()
    
        map_result['status'] = 0
        map_result['description'] = 'success'
        return map_result
     
# if __name__ == '__main__':
#     from sklearn.svm import SVC
#     import numpy as np
#     clf = SVC()
#     x_train = np.loadtxt('data/fselect.txt', delimiter=',', dtype=int)
#     y_train = np.loadtxt('data/fresult.txt', dtype=int)
#     clf = clf.fit(x_train, y_train)
#     lst = []
#     lst.append(3)
#     lst.append(0)
#     lst.append(0)
#     lst.append(0)
#     lst.append(0)
#     lst.append(1)
#     lst.append(0)
#     lst.append(0)
#     print int(clf.predict(lst))
