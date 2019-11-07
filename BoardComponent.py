class Error(Exception):
    pass

class Board():

    def __init__(self,board):
        self.dicb = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[]}
        self.board = board
        for j in self.board[slice(0,9,1)]:
            self.dicb['a'].append(j)
        for j in self.board[slice(9,18,1)]:
            self.dicb['b'].append(j)
        for j in self.board[slice(18,27,1)]:
            self.dicb['c'].append(j)
        for j in self.board[slice(27,36,1)]:
            self.dicb['d'].append(j)
        for j in self.board[slice(36,45,1)]:
            self.dicb['e'].append(j)
        for j in self.board[slice(45,54,1)]:
            self.dicb['f'].append(j)
        for j in self.board[slice(54,63,1)]:
            self.dicb['g'].append(j)
        for j in self.board[slice(63,72,1)]:
            self.dicb['h'].append(j)
        for j in self.board[slice(72,81,1)]:
            self.dicb['i'].append(j)    
        

    def is_modifiable(self, letter, col):
        if self.dicb[letter][col] != ' ':
            return True
        else:
            return False

    def validate_row(self, row, value):
        for x in self.dicb[row]:
            if x == str(value):
                return False
        return True

    def validate_column(self, column, value):

        for j in 'abcdefghi':
            if self.dicb[j][column - 1] == value:
                return False             
        return True
        
    def validate_region(self,x,y,n):
        """ Parte 1 """
        if x == 0 or x == 1 or x == 2:
            for y in range(3):
                if self.dicb[x+3][y] == n:
                    return(False)
                if self.dicb[x+6][y] == n:
                    return(False)
        if x == 3 or x == 4 or x == 5:
            for y in range(3):
                if self.dicb[x+3][y] == n:
                    return(False)
                if self.dicb[x+6][y] == n:
                    return(False)
        if x == 6 or x == 7 or x == 8:
            for y in range(3):
                if self.dicb[x-3][y] == n:
                    return(False)
                if self.dicb[x-6][y] == n:
                    return(False)


        """ Parte 2 """
        if x == 9 or x == 10 or x == 11:
            for y in range(3):
                if self.dicb[x+3][y] == n:
                    return(False)
                if self.dicb[x+6][y] == n:
                    return(False)
        if x == 12 or x == 13 or x == 14:
            for y in range(3):
                if self.dicb[x+3][y] == n:
                    return(False)
                if self.dicb[x+6][y] == n:
                    return(False)
        if x == 15 or x == 16 or x == 17:
            for y in range(3):
                if self.dicb[x-3][y] == n:
                    return(False)
                if self.dicb[x-6][y] == n:
                    return(False)

        """ Parte 3 """
        if x == 18 or x == 19 or x == 20:
            for y in range(3):
                if self.dicb[x+3][y] == n:
                    return(False)
                if self.dicb[x+6][y] == n:
                    return(False)
        if x == 21 or x == 22 or x == 23:
            for y in range(3):
                if self.dicb[x+3][y] == n:
                    return(False)
                if self.dicb[x+6][y] == n:
                    return(False)
        if x == 24 or x == 25 or x == 26:
            for y in range(3):
                if self.dicb[x-3][y] == n:
                    return(False)
                if self.dicb[x-6][y] == n:
                    return(False)

        
        return(True)
     
    def get_region(self, x, col):
        array = []

        y = col - 1

        if x == 'a' or x == 'b' or x == 'c':
            if y == 0 or y == 1 or y == 2:
                for j in range(3):
                    array.append(self.dicb['a'][j])
                for j in range(3):
                    array.append(self.dicb['b'][j])
                for j in range(3):
                    array.append(self.dicb['c'][j])
            if y == 3 or y == 4 or y == 5:
                for j in range(3):
                    array.append(self.dicb['a'][j + 3])
                for j in range(3):
                    array.append(self.dicb['b'][j + 3])
                for j in range(3):
                    array.append(self.dicb['c'][j + 3])
            if y == 6 or y == 7 or y == 8 :
                for j in range(3):
                    array.append(self.dicb['a'][j + 6])
                for j in range(3):
                    array.append(self.dicb['b'][j + 6])
                for j in range(3):
                    array.append(self.dicb['c'][j + 6])


        if x == 'd' or x == 'e' or x == 'f':
            if y == 0 or y == 1 or y == 2:
                for j in range(3):
                    array.append(self.dicb['d'][j])
                for j in range(3):
                    array.append(self.dicb['e'][j])
                for j in range(3):
                    array.append(self.dicb['f'][j])
            if y == 3 or y == 4 or y == 5:
                for j in range(3):
                    array.append(self.dicb['d'][j + 3])
                for j in range(3):
                    array.append(self.dicb['e'][j + 3])
                for j in range(3):
                    array.append(self.dicb['f'][j + 3])
            if y == 6 or y == 7 or y == 8 :
                for j in range(3):
                    array.append(self.dicb['d'][j + 6])
                for j in range(3):
                    array.append(self.dicb['e'][j + 6])
                for j in range(3):
                    array.append(self.dicb['f'][j + 6])

        if x == 'g' or x == 'h' or x == 'i':
            if y == 0 or y == 1 or y == 2:
                for j in range(3):
                    array.append(self.dicb['g'][j])
                for j in range(3):
                    array.append(self.dicb['h'][j])
                for j in range(3):
                    array.append(self.dicb['i'][j])
            if y == 3 or y == 4 or y == 5:
                for j in range(3):
                    array.append(self.dicb['g'][j + 3])
                for j in range(3):
                    array.append(self.dicb['h'][j + 3])
                for j in range(3):
                    array.append(self.dicb['i'][j + 3])
            if y == 6 or y == 7 or y == 8 :
                for j in range(3):
                    array.append(self.dicb['g'][j + 6])
                for j in range(3):
                    array.append(self.dicb['h'][j + 6])
                for j in range(3):
                    array.append(self.dicb['i'][j + 6])


        return array


    def place(self, tupla, v):
        value = str(v)
        a , b = tupla
        try:
            if self.dicb[a][b - 1] == ' ': 
                if self.validate_row(a,value) == True:
                    if self.validate_column(b,value) == True:
                        if self.validate_region(a,b,value) == True:
                            print(self.dicb[a][b - 1])
                            self.dicb[a][b - 1] = value
                            self.dicb[a][b - 1]
                        else:
                            print('--------Existe en region')
                    else:
                        print('--------Existe en columna')
                else:
                    print('--------Existe en fila: ')
            else:
                print('--------No es modificable en ')
        except Error:
            print('Intente otra vez')

    def validate_number(self, coordinates, value):

        pass

    def is_finished(self):
        for x in self.dicb['a']:
            if x == ' ':
                return False
        for x in self.dicb['b']:
            if x == ' ':
                return False
        for x in self.dicb['c']:
            if x == ' ':
                return False
        for x in self.dicb['d']:
            if x == ' ':
                return False
        for x in self.dicb['e']:
            if x == ' ':
                return False
        for x in self.dicb['f']:
            if x == ' ':
                return False
        for x in self.dicb['g']:
            if x == ' ':
                return False
        for x in self.dicb['h']:
            if x == ' ':
                return False
        for x in self.dicb['i']:
            if x == ' ':
                return False
        return True


    def show_board(self):

        shownb = \
            self.dicb['a'][0] + ' ' + self.dicb['a'][1] + ' ' + self.dicb['a'][2] + ' |' + self.dicb['a'][3] + ' ' + self.dicb['a'][4] + ' ' + self.dicb['a'][5] + ' |' + self.dicb['a'][6] + ' ' + self.dicb['a'][7] + ' ' + self.dicb['a'][8] + ' \n' \
            + self.dicb['b'][0] + ' ' + self.dicb['b'][1] + ' ' + self.dicb['b'][2] + ' |' + self.dicb['b'][3] + ' ' + self.dicb['b'][4] + ' ' + self.dicb['b'][5] + ' |' + self.dicb['b'][6] + ' ' + self.dicb['b'][7] + ' ' + self.dicb['b'][8] + ' \n' \
            + self.dicb['c'][0] + ' ' + self.dicb['c'][1] + ' ' + self.dicb['c'][2] + ' |' + self.dicb['c'][3] + ' ' + self.dicb['c'][4] + ' ' + self.dicb['c'][5] + ' |' + self.dicb['c'][6] + ' ' + self.dicb['c'][7] + ' ' + self.dicb['c'][8] + ' \n' \
            + '------+------+------\n' \
            + self.dicb['d'][0] + ' ' + self.dicb['d'][1] + ' ' + self.dicb['d'][2] + ' |' + self.dicb['d'][3] + ' ' + self.dicb['d'][4] + ' ' + self.dicb['d'][5] + ' |' + self.dicb['d'][6] + ' ' + self.dicb['d'][7] + ' ' + self.dicb['d'][8] + ' \n' \
            + self.dicb['e'][0] + ' ' + self.dicb['e'][1] + ' ' + self.dicb['e'][2] + ' |' + self.dicb['e'][3] + ' ' + self.dicb['e'][4] + ' ' + self.dicb['e'][5] + ' |' + self.dicb['e'][6] + ' ' + self.dicb['e'][7] + ' ' + self.dicb['e'][8] + ' \n' \
            + self.dicb['f'][0] + ' ' + self.dicb['f'][1] + ' ' + self.dicb['f'][2] + ' |' + self.dicb['f'][3] + ' ' + self.dicb['f'][4] + ' ' + self.dicb['f'][5] + ' |' + self.dicb['f'][6] + ' ' + self.dicb['f'][7] + ' ' + self.dicb['f'][8] + ' \n' \
            + '------+------+------\n' \
            + self.dicb['g'][0] + ' ' + self.dicb['g'][1] + ' ' + self.dicb['g'][2] + ' |' + self.dicb['g'][3] + ' ' + self.dicb['g'][4] + ' ' + self.dicb['g'][5] + ' |' + self.dicb['g'][6] + ' ' + self.dicb['g'][7] + ' ' + self.dicb['g'][8] + ' \n' \
            + self.dicb['h'][0] + ' ' + self.dicb['h'][1] + ' ' + self.dicb['h'][2] + ' |' + self.dicb['h'][3] + ' ' + self.dicb['h'][4] + ' ' + self.dicb['h'][5] + ' |' + self.dicb['h'][6] + ' ' + self.dicb['h'][7] + ' ' + self.dicb['h'][8] + ' \n' \
            + self.dicb['i'][0] + ' ' + self.dicb['i'][1] + ' ' + self.dicb['i'][2] + ' |' + self.dicb['i'][3] + ' ' + self.dicb['i'][4] + ' ' + self.dicb['i'][5] + ' |' + self.dicb['i'][6] + ' ' + self.dicb['i'][7] + ' ' + self.dicb['i'][8] + ' \n' \
        
        return shownb
        