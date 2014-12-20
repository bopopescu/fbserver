from npl import CRFWordSegment

class FBPost(object):
#     old feature
    likes = 0
    shares = 0
    comments = 0
    url = 0
    hashtags = 0
    images = 0
    vdo = 0
    
#     common feature
    wot_score = 0
    not_wot_score = 0
    word_outside_dict = 0
    
#     only facebook feature
    app_sender = 0
    place = 0
    gps = 0
    tag_with = 0
    is_public = 0
    
    
#   twiiter feature  
    word_count = 0
    character_length = 0
    question_mark = 0
    exclamation_mark = 0
    day_pass = 0
    
    def __init__(self, likes=None, shares=None, comments=None, url=None, 
                 hashtags=None, images=None, vdo=None, wot_score=None, not_wot_score=None,
                 word_outside_dict=None, app_sender=None, place=None,
                 gps=None, tag_with=None, is_public=None,
                 word_count=None, character_length=None, question_mark=None,
                 exclamation_mark=None, day_pass=None):
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
        self.place = place
        self.gps = gps
        self.tag_with = tag_with
        self.is_public = is_public
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
        , wot_score={}, not_wot_score={}, word_outside_dict={}, app_sender={}, place={},
        gps={}, tag_with={}, is_public={}, word_count={}, character_length={},
        question_mark={}, exclamation_mark={}, day_pass={}]'''
        return str.format(self.likes, 
                          self.shares,
                          self.comments,
                          self.url,
                          self.hashtags,
                          self.images,
                          self.vdo,
                          self.wot_score, self.not_wot_score, self.word_outside_dict,
                          self.app_sender, self.place, self.gps, self.tag_with,
                          self.is_public, self.word_count, self.character_length,
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
   
    