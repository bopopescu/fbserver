from npl import CRFWordSegment

class FBPost(object):
#     old feature
    likes = 0 #ok
    shares = 0 #ok
    comments = 0 #ok
    url = 0 #ok
    hashtags = 0 #ok
    images = 0 #ok
    vdo = 0 #ok
    
#     common feature
    wot_score = 0
    not_wot_score = 0
    word_outside_dict = 0
    
#     only facebook feature
    app_sender = 0 #socialcam, twitter, instagam
    location = 0
    tag_with = 0
    feeling_status = 0
    share_public = 0 #ok
    share_only_friend = 0 #ok
    
    
#   twiiter feature  
    word_count = 0 #ok
    character_length = 0 #ok
    question_mark = 0 #ok
    exclamation_mark = 0 #ok
    day_pass = 0
    
    def __init__(self, likes=None, shares=None, comments=None, url=None, 
                 hashtags=None, images=None, vdo=None, wot_score=None, not_wot_score=None,
                 word_outside_dict=None, app_sender=None, location=None,
                 tag_with=None, feeling_status=None, share_public=None,
                 share_only_friend=None,word_count=None, character_length=None, 
                 question_mark=None, exclamation_mark=None, day_pass=None):
        self.likes = likes
        self.shares = shares
        self.comments = comments
        self.url = url
        self.hashtags = hashtags
        self.images = images
        self.vdo = vdo
        self.wot_score = wot_score
        self.not_wot_score = not_wot_score
        self.word_outside_dict = word_outside_dict
        self.app_sender = app_sender
        self.location = location
        self.tag_with = tag_with
        self.feeling_status = feeling_status
        self.share_public = share_public
        self.share_only_friend = share_only_friend
        self.word_count = word_count
        self.character_length = character_length
        self.question_mark = question_mark
        self.exclamation_mark = exclamation_mark
        self.day_pass = day_pass        
        
#     @property
#     def likes(self):
#         return self._likes
#     @likes.setter
#     def likes(self, val):
#         self._likes = val
    
    def __str__(self, *args, **kwargs):
        str = '''[likes={}, shares={}, comments={}, url={}, hashtag={}, images={}, vdo={}
        , wot_score={}, not_wot_score={}, word_outside_dict={}, app_sender={}, location={},
        tag_with={}, feeling_status={}, share_public={}, share_with_friend={}, word_count={}, character_length={},
        question_mark={}, exclamation_mark={}, day_pass={}]'''
        return str.format(self.likes, 
                          self.shares,
                          self.comments,
                          self.url,
                          self.hashtags,
                          self.images,
                          self.vdo,
                          self.wot_score, self.not_wot_score, self.word_outside_dict,
                          self.app_sender, self.location, self.tag_with, self.feeling_status,
                          self.share_public, 
                          self.share_only_friend,
                          self.word_count, self.character_length,
                          self.question_mark, self.exclamation_mark, self.day_pass)
    
class Test(object):
    data1 = 0
    data2 = 1
    
    def __str__(self, *args, **kwargs):
        return "[data1={},data2={}]".format(self.data1, self.data2)

class ProcessData(object):
    
    def __init__(self, message):
        self.message = message
        
    def pross_char(self, msg_lst):
        q_mark = 0
        ex_mark = 0
        for x in msg_lst:
            if x == '?':
                q_mark = q_mark+1
            if x == '!':
                ex_mark = ex_mark+1
        return q_mark, ex_mark
                
    def process(self):
        print self.message.encode('utf-8')
        crf = CRFWordSegment()
        word_list, char_lst = crf.crfpp(self.message)
        quest_mark, exclamation_mark = self.pross_char(self.message.encode('utf-8'))
        return len(word_list), len(char_lst), quest_mark, exclamation_mark
# test = Test()
# test.data1 = 10
# test.data2 = 30
# print test.data  
   
    