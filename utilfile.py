import codecs


class StringUtil:

    @staticmethod
    def remove_ne(message):
        return message.replace('<NE>', '').replace('</NE>', '').replace('<AB>', '').replace('</AB>', '')
    

class FileUtil:

    def n_write_file(self, file_name, message):
        print message
        f = open(file_name,'a+b')
        f.write(message+'\n')
        f.close()
        
    def write_file(self, file_name, message):
        with codecs.open(file_name, 'a+b', encoding='utf8') as f:
            f.write(message + '\n')
            f.close()

    def write_file_no_n(self, file_name, message):
         with codecs.open(file_name, 'a+b', encoding='utf8') as f:
            f.write(message)
            f.close()
    
    def write_newfile_n(self, file_name, message):
           self.template_write_file(file_name, message, 'w')
         
    def write_newfile(self, file_name, message):
           self.template_write_file(file_name, message, 'w')
    
    def read_noencode(self, filename):
        f = open(filename)
        lines = f.readlines()
        f.close()
        return lines
     
    def read_file(self, file_name):
        with codecs.open(file_name, 'r', 'utf-8') as file:
            return file.readlines()
        return []
    
    def template_write_file(self, file_name, message, option):
          with codecs.open(file_name, option, encoding='utf8') as f:
            f.write(message)
            f.close()       
