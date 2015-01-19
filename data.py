from npl import CRFWordSegment
from initial import FBInit
import json, re

class FBPost(object):
#     old feature
    likes = 0 #ok
    shares = 0 #ok
    comments = 0 #ok
    hashtags = 0 #ok
    images = 0 #ok
    vdo = 0 #ok
    
#     common feature
    url = 0 #ok
    word_in_dict = 0 #ok
    word_outside_dict = 0 #ok
    num_of_number_in_sentense = 0 #ok
    
#     only facebook feature
    app_sender = 0 #socialcam, twitter, instagam
    share_with_location = 0 #ok
    share_with_non_location = 0 #ok
    tag_with = 0 #ok
    feeling_status = 0 #ok
    share_public = 0 #ok
    share_only_friend = 0 #ok    
    
#   twiiter feature  
    word_count = 0 #ok
    character_length = 0 #ok
    question_mark = 0 #ok
    exclamation_mark = 0 #ok
#     day_pass = 0
    
# other data
    message = ''
    cred_value = ''
    
    def __init__(self, likes=None, shares=None, comments=None, url=None, 
                 hashtags=None, images=None, vdo=None, wot_score=None,
                 word_outside_dict=None, app_sender=None, share_with_location=None,
                 tag_with=None, feeling_status=None, share_public=None,
                 share_only_friend=None,word_count=None, character_length=None, 
                 question_mark=None, exclamation_mark=None):
        self.likes = likes
        self.shares = shares
        self.comments = comments
        self.url = url
        self.hashtags = hashtags
        self.images = images
        self.vdo = vdo
        self.word_outside_dict = word_outside_dict
        self.app_sender = app_sender
        self.share_with_location = share_with_location
        self.tag_with = tag_with
        self.feeling_status = feeling_status
        self.share_public = share_public
        self.share_only_friend = share_only_friend
        self.word_count = word_count
        self.character_length = character_length
        self.question_mark = question_mark
        self.exclamation_mark = exclamation_mark   
        
#     @property
#     def likes(self):
#         return self._likes
#     @likes.setter
#     def likes(self, val):
#         self._likes = val
    
    def __str__(self, *args, **kwargs):
        return json.dumps(self.to_dict(), indent=4, separators=(',', ': '))
    
    def to_dict(self):
        d = {}
        for k, v in [(x, getattr(self, x)) for x in dir(self) if not x.startswith('_')]:
            if not hasattr(v, '__call__'): d[k] = v # skip methods
        return d

class ProcessData(object):
    
    def __init__(self, message):
        self.message = message
        
    def pross_char(self, msg_lst):
        q_mark = 0
        ex_mark = 0
        digit_in_sen = 0
        for x in msg_lst:
            if x == '?':
                q_mark = q_mark+1
            if x == '!':
                ex_mark = ex_mark+1
            if x.isdigit():
                digit_in_sen += 1
        return q_mark, ex_mark, digit_in_sen
    
    def pre_process(self, msg):
        new_msg = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', msg)
        return new_msg
         
    def process(self, fbPost):
        print self.message.encode('utf-8')
        crf = CRFWordSegment()
#         print 'message lenght ', len(self.message.encode('utf-8'))
        if len(self.message.encode('utf-8')) == 0:
            fbPost.word_count = 0
            fbPost.character_length = 0
            fbPost.question_mark = 0
            fbPost.exclamation_mark = 0
            fbPost.word_outside_dict = 0
            fbPost.word_in_dict = 0
            fbPost.num_of_number_in_sentense = 0            
            return
        process_msg = self.pre_process(self.message)
        word_list, char_lst = crf.crfpp(process_msg)
#         print 'word list ', word_list
#         print 'char list ', char_lst
        quest_mark, exclamation_mark , digit_in_sen = self.pross_char(char_lst)
        w_count = 0
        word_list = [w for w in word_list if w.encode('utf-8') != ' ']        
        for w in word_list:
            w = w.encode('utf-8')
            if w in FBInit().dict:
                w_count += 1
        fbPost.word_count = len(word_list)
        fbPost.character_length = len(char_lst)
        fbPost.question_mark = quest_mark
        fbPost.exclamation_mark = exclamation_mark
        fbPost.word_outside_dict = len(word_list)-w_count
        fbPost.word_in_dict = w_count
        fbPost.num_of_number_in_sentense = digit_in_sen
#         return len(word_list), len(char_lst), quest_mark, exclamation_mark, w_count, len(word_list)-w_count
        

   
    