from BoardComponent import Board

EXAMPLE_BOARD = " 6 3  8 4" \
    "537 9    " \
    " 4   63 7" \
    " 9  51238" \
    "         " \
    "71362  4 " \
    "3 64   1 " \
    "    6 523" \
    "1 2  9 8 "


class Interfaz:

    board = Board(EXAMPLE_BOARD)
        

    def set_valor_x(self,x):
        if self.x == 'a' or self.x == 'b' or self.x == 'c' or self.x == 'd' or self.x == 'e' or self.x == 'f' or self.x == 'g' or self.x == 'h' or self.x == 'i':
            return True
        else:
            print('La fila no existe')
            return False
            
    def set_valor_y(self,y):
        if self.y < 1 or self.y > 9:
            print('La columna no existe')
            return False
        else:
            return True
    
    def play(self):
        print('Bienvenido a sudoku!')
        while self.board.is_finished() == False:
            print('Su Tablero es:')
            print(self.board.show_board())

            self.x = str(input('Elija fila, pueden se : a,b,c,d,e,f,g,h,i: '))
            if self.set_valor_x(self.x) == True:
                self.y = int(input('Elija columna , pueden se : 1,2,3,4,5,6,7,8,9: '))
                if self.set_valor_y(self.y) == True:
                    self.value = str(input('Escriba un numero:'))
                    self.board.place((self.x,self.y),self.value)

