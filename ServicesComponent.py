import requests
import json

class ServicesComponents():
    
    def get_sudoku_size_4(self,level):
        #GET
        r = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level='+str(level)+'&size=4')
        status = r.status_code
        headers = r.headers['content-type']
        encoding = r.encoding
        response = json.loads(r.text)
        #
        
        if status == 200:
            squares = response['squares']
            return squares
        else:
            return status

    def get_sudoku_size_9(self,level,size):
        #GET
        r = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level='+str(level)+'&size=9')
        status = r.status_code
        headers = r.headers['content-type']
        encoding = r.encoding
        response = json.loads(r.text)
        #
        
        if status == 200:
            squares = response['squares']
            return squares
        else:
            return status
