from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QMenu, QAction
from PyQt5 import uic
import sys



class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("Tic Tac Toe")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #f0f0f0")
        
        # Loading UI File:
        uic.loadUi("tictow_game.ui", self)
        
        # Counter for button clicks and win check
        self.counter = 0
        
        # Game Board co-ordinates
        self.posible_win = [['X', 'X', 'X'], ['X', 'O', 'O'], ['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X'], ['O', 'O', 'X'], ['X', 'O', 'O'], ['X', 'X', 'O']]
        
        # Game Matrix
        self.game_matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        
        # Buttopn and crosponding co-ordinates
        self.location = {"pushButton": [0, 0], "pushButton_2": [1,0], "pushButton_3": [2, 0], "pushButton_4": [0, 1], "pushButton_5": [1, 1], "pushButton_6": [2, 1], "pushButton_7": [0, 2], "pushButton_8": [1, 2], "pushButton_9": [2, 2]}
         
        self.button1 = self.findChild(QPushButton, "pushButton")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_19")
        
        self.button1.clicked.connect(lambda: self.button_clicked(self.button1))
        self.button2.clicked.connect(lambda: self.button_clicked(self.button2))
        self.button3.clicked.connect(lambda: self.button_clicked(self.button3))
        self.button4.clicked.connect(lambda: self.button_clicked(self.button4))
        self.button5.clicked.connect(lambda: self.button_clicked(self.button5))
        self.button6.clicked.connect(lambda: self.button_clicked(self.button6))
        self.button7.clicked.connect(lambda: self.button_clicked(self.button7))
        self.button8.clicked.connect(lambda: self.button_clicked(self.button8))
        self.button9.clicked.connect(lambda: self.button_clicked(self.button9))
        
        self.button10.clicked.connect(self.reset)
        
        self.label = self.findChild(QLabel, "label_2")
        
        # get x score label
        self.X_sc_value = 0
        self.X_score = self.findChild(QLabel, "label_5")
        
        # get o score label
        self.O_sc_value = 0
        self.O_score = self.findChild(QLabel, "label_6")
        
        # get draw score label
        self.draw_sc_value = 0
        self.draw_score = self.findChild(QLabel, "label_8")
        
        
    def button_clicked(self, button):
        if button.text() == "":
            if self.counter % 2 == 0:
                button.setText("X")
                button.setStyleSheet("background-color: red; color: white")
                button.setEnabled(False)

                temp_location = self.location[button.objectName()]
                self.game_matrix[temp_location[0]][temp_location[1]] = "X"
                
            else:
                button.setText("O")
                button.setStyleSheet("background-color: blue; color: white")
                button.setEnabled(False)
                
                temp_location = self.location[button.objectName()]
                self.game_matrix[temp_location[0]][temp_location[1]] = "O"

            self.counter += 1
            self.check_for_win(button)
        else:
            QMessageBox.information(self, "Error", "This box is already used")
       
    
    def check_for_win(self, button):
        # check for win
        first_player = "X"
        second_player = "O"

        # # print game matrix on console Also
        # for  row in range(3):
        #     for col in range(3):
        #         print(self.game_matrix[row][col], end=" ")
        #     print()
        # print("-----------------")
        
        row_1 = self.game_matrix[:][0]
        row_2 = self.game_matrix[:][1]
        row_3 = self.game_matrix[:][2]
        
        col_1 = [col[0] for col in self.game_matrix]
        col_2 = [col[1] for col in self.game_matrix]
        col_3 = [col[2] for col in self.game_matrix]
        
        diag_1 = [self.game_matrix[0][0], self.game_matrix[1][1], self.game_matrix[2][2]]
        diag_2 = [self.game_matrix[0][2], self.game_matrix[1][1], self.game_matrix[2][0]]
        
        moves = [row_1, row_2, row_3, col_1, col_2, col_3, diag_1, diag_2]
        
        for move in moves:
            if move.count(first_player) == 3:
                self.label.setText("X is the winner")
                self.label.setStyleSheet("background-color: red; color: white")
                self.X_sc_value += 1
                self.X_score.setText(str(self.X_sc_value))
                self.diable_all_buttons()
                # self.hide_button(button)
                return 0
            elif move.count(second_player) == 3:
                self.label.setText("O is the winner")
                self.label.setStyleSheet("background-color: blue; color: white")
                self.O_sc_value += 1
                self.O_score.setText(str(self.O_sc_value))
                self.diable_all_buttons()
                return 0
        
        if self.counter % 9 == 0:
            self.label.setText("No one won")
            self.label.setStyleSheet("background-color: black; color: white")
            self.draw_sc_value += 1
            self.draw_score.setText(str(self.draw_sc_value))
            self.diable_all_buttons()
            return 0
            
            
    def hide_button(self, button):
        all_reset_button_list = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]
        for btn in all_reset_button_list:
            btn.setVisible(False)
            
    def show_button(self):
        all_reset_button_list = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]
        for btn in all_reset_button_list:
            btn.setVisible(True)
        

    def diable_all_buttons(self):
        all_reset_button_list = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]
        
        for btn in all_reset_button_list:
            btn.setEnabled(False)
        
    
    def reset(self):
        self.counter = 0
        
        # Confirm reset
        # rset = QMessageBox.question(self, "Reset", "Are you sure you want to reset the game?", QMessageBox.Yes | QMessageBox.No)
        
        all_reset_button_list = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]
        
        self.label.setText("")
        self.label.setStyleSheet("background-color:  rgb(0, 85, 127); color: black")
        for button in all_reset_button_list:
            button.setText("")
            button.setStyleSheet("background: #ccc; background-color: aqua; border: 1px solid #000000;")
            button.setEnabled(True)
            
        # reset the game matrix
        for i in range(3):
            for j in range(3):
                self.game_matrix[i][j] = "_"
        
        # self.show_button()
                


if __name__ == "__main__":
    app = QApplication([])
    UiMain = UI()
    UiMain.show()
    sys.exit(app.exec_())