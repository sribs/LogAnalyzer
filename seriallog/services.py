import json

class ErrorKeyWordsProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()

class ErrorKeyWords:
    __jsonpath = '/tmp/err_file.json'
    __err_file = None

    @classmethod
    def get_error_keywords(cls):
        with open(cls.__jsonpath,'r') as err_file:
            cls.__err_file = json.loads(err_file.read())
            print(cls.__err_file)
            return cls.__err_file

    @classmethod
    def set_error_keywords(cls,new_error): 
        if cls.__err_file is not None:
            cls.__err_file += new_error
        else:
            cls.error_keywords()
            cls.set_error_keywords(new_error)

    @classmethod    
    def update_error_keywords(cls,new_error):
        print(new_error)
        with open(cls.__jsonpath,'w+') as err_file:
            cls.set_error_keywords(new_error)
            err_file.write(json.dumps(cls.__err_file,indent=4))

def yield_huge_files(file_des,err_keywords=ErrorKeyWords.get_error_keywords()):
    for line in file_des:
        for keyword in err_keywords:
            line_str = line.decode("utf-8")
            if keyword['issue'] in line_str.lower():
                yield line_str