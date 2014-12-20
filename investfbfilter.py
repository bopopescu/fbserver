from database import *
from filtercomputation import *

class InvFBFilter(object):
    
    def getAllMessage(self):
        db = Database()
        sql = "select message from filter_el"
        lst = db.select_inv_fbfiler(sql)
        str = ''
        i = 0;
        for x in lst:
            if i%2 == 0:
                str = str+"<tr bgcolor='gray'><td>"+x+"</td></tr>"
            else:
                str = str+"<tr><td>"+x+"</td></tr>"
            i=i+1
        return self.templateCall(str)
    
    def getTData(self):
        sql = 'select message from filter_el where sholdbe = "yes"'
        db = Database()
        lst = db.select_inv_fbfiler(sql)
        str = ''
        i = 0
        for x in lst:
            if i%2 == 0:
                str = str+"<tr bgcolor='gray'><td>"+x+"</td></tr>"
            else:
                str = str+"<tr><td>"+x+"</td></tr>"
            i = i+1
        return self.templateCall(str)
        
    def getQueryData(self, message):
        str = ''
        filterComp = FilterComputation()
        m = filterComp.invFBFilter(message)
        i = 0;
        str = str+"<tr><td>tf-idf</td><td>message</td></tr>"
        for k in m.keys():
            data = k
            tf_value = m[k]
#             print type(tf_value)
#             tf_value = str(m[k])
#             print tf_value
            tf_str = '%.2f'%tf_value
            if i%2 == 0:
                str = str+"<tr bgcolor='gray'><td>"+tf_str+"</td><td>"+data+"</td></tr>"
            else:
                str = str+"<tr><td>"+tf_str+"</td><td>"+data+"</td></tr>"
            i=i+1          
        return self.templateCall(str)
    
    def templateCall(self, str):
        return '''
<html>
  <head>
    <title>Investigation FB Filter</title>
  </head>
  <body>
      <form action='/invfbfilter'>
          <input type='text' name='q'/>
          <input type='submit' value='query'/>
      </form>
      <table>
    ''' + str + '''
      </table>
  </body>
</html>
'''
    