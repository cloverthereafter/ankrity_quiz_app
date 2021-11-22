import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QFrame, QLineEdit, QRadioButton, QPushButton, QTextEdit, QSpinBox, QButtonGroup,QMessageBox
from PyQt5.QtChart import QChart,  QChartView, QPieSeries
from PyQt5.QtGui import QFont, QPainter, QColor
from PyQt5.QtCore import Qt, QRectF
import csv
import uuid

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Ankrity'
        self.left = 670
        self.top = 190
        self.width = 560
        self.height = 839
        self.setFixedSize(self.width, self.height)
        with open("design.qss",'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.a = 0
        self.code = str(uuid.uuid4)
        self.quiz_code = self.code[20:28]
        self.setObjectName("main-window")
        self.initUI()
        self.l = []
        #self.lst = []
        self.x1 = 1
        self.x2 = 0
        self.count = 0
        self.no_of_crct = 0
        self.no_of_wrong = 0
        self.unattempted = 0
        self.total = 0
        self.flag = 0
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    #create
        self.quiz_label = QLabel(self)
        self.quiz_label.setText("Ankrity")
        self.quiz_label.setObjectName("quiz-label")
        self.quiz_label.move(155,110)

        self.create_btn = QFrame(self)
        self.create_btn.setObjectName("buttons")
        self.create_btn.move(100,350)
        self.create_btn.mousePressEvent = self.create_clicked

        self.create_label = QLabel(self.create_btn)
        self.create_label.setObjectName("frame-heading")
        self.create_label.setText("Create a Quiz")
        self.create_label.move(85,25)

        self.create_expanded = QLabel(self)
        self.create_expanded.setObjectName("frame-exp")
        self.create_expanded.move(75,100)
        self.create_expanded.setVisible(False)

        #second page
        self.back_button_c = QLabel(self.create_expanded)
        self.back_button_c.move(20,5)
        self.back_button_c.setTextFormat(Qt.RichText)
        self.back_button_c.setText("&#8592;")
        self.back_button_c.setObjectName("back_button")
        self.back_button_c.mousePressEvent = self.back_button_clicked

        self.deco = QLabel(self.create_expanded)
        self.deco.setObjectName("deco")
        self.deco.setText("ecmce")
        self.deco.move(175,12)

        self.welcome = QLabel(self.create_expanded)
        self.welcome.move(45,50)
        self.welcome.setText("Welcome!")
        self.welcome.setObjectName("welcome")

        self.qname = QLabel(self.create_expanded)
        self.qname.setText("Name your quiz*:")
        self.qname.setObjectName("input_prompts")
        self.qname.move(80,250)

        self.name_input = QLineEdit(self.create_expanded)
        self.name_input.setObjectName("input")
        self.name_input.move(70,300)
 
        self.start_create_btn = QPushButton(self.create_expanded)
        self.start_create_btn.setText("Start Creating!")
        self.start_create_btn.setObjectName("push-buttons")
        self.start_create_btn.move(70,530)
        self.start_create_btn.clicked.connect(self.start_c_clicked)

        self.req = QLabel(self.create_expanded)
        self.req.setText("*:Required field")
        self.req.setObjectName("ps")
        self.req.move(120,590)

        self.create_q_frame = QLabel(self)
        self.create_q_frame.setObjectName("frame-exp")
        self.create_q_frame.move(75,100)
        self.create_q_frame.setVisible(False)

        self.next_btn = QPushButton(self.create_q_frame)
        self.next_btn.setObjectName("push-buttons")
        self.next_btn.setText("Next")
        self.next_btn.move(15,530)
        self.next_btn.clicked.connect(self.next_clicked)

        self.submit_btn = QPushButton(self.create_q_frame)
        self.submit_btn.setObjectName("push-buttons")
        self.submit_btn.setText("Submit")
        self.submit_btn.move(250, 530)
        self.submit_btn.clicked.connect(self.submit_clicked)

        self.q_frame = QLabel(self.create_q_frame)
        self.q_frame.setObjectName("q-frame")
        self.q_frame.move(5,30)
        self.q_frame.setVisible(False)

        self.question = QLabel(self.q_frame)
        self.question.setObjectName("input_prompts")
        self.question.setText("Question:")
        self.question.move(10,15)

        self.q_input = QTextEdit(self.q_frame)
        self.q_input.setObjectName("question")
        self.q_input.move(10,50)

        self.marks = QLabel(self.q_frame)
        self.marks.setObjectName("input_prompts")
        self.marks.setText("Marks:")
        self.marks.move(10,110)

        self.marks_input = QSpinBox(self.q_frame)
        self.marks_input.setRange(1, 100)
        self.marks_input.setObjectName("time_input")
        self.marks_input.move(105,115)

        self.ans_a = QRadioButton(self.q_frame)
        self.ans_a.move(10, 200)

        self.option_a = QTextEdit(self.q_frame)
        self.option_a.setObjectName("answers")
        self.option_a.move(30, 200)

        self.ans_b = QRadioButton(self.q_frame)
        self.ans_b.move(10, 250)

        self.option_b = QTextEdit(self.q_frame)
        self.option_b.setObjectName("answers")
        self.option_b.move(30, 250)

        self.ans_c = QRadioButton(self.q_frame)
        self.ans_c.move(10, 300)

        self.option_c = QTextEdit(self.q_frame)
        self.option_c.setObjectName("answers")
        self.option_c.move(30, 300)

        self.ans_d = QRadioButton(self.q_frame)
        self.ans_d.move(10, 350)

        self.option_d = QTextEdit(self.q_frame)
        self.option_d.setObjectName("answers")
        self.option_d.move(30, 350)

        self.group1 = QButtonGroup()
        self.group1.addButton(self.ans_a)
        self.group1.addButton(self.ans_b)
        self.group1.addButton(self.ans_c)
        self.group1.addButton(self.ans_d)

        self.ty = QLabel(self)
        self.ty.setObjectName("frame-exp")
        self.ty.move(100, 100)
        self.ty.setVisible(False)

        self.exit = QLabel(self.ty)
        self.exit.setObjectName("welcome")
        self.exit.setText("Thank you!!")
        self.exit.move(15, 150)

        self.ref = QLabel(self.ty)
        self.ref.setObjectName("frame-heading")
        self.ref.setText("Your quiz code is:  {}".format(self.quiz_code))
        self.ref.setWordWrap(True)
        self.ref.move(75, 300)

    #join
        self.join_btn = QFrame(self)
        self.join_btn.setObjectName("buttons")
        self.join_btn.move(100,470)
        self.join_btn.mousePressEvent = self.join_clicked
        #self.join_btn.setVisible(False)

        self.join_label = QLabel(self.join_btn)
        self.join_label.setObjectName("frame-heading")
        self.join_label.setText("Take a Quiz")
        self.join_label.move(85,25)

        self.join_expanded = QLabel(self)
        self.join_expanded.setObjectName("frame-exp")
        self.join_expanded.move(75,100)
        self.join_expanded.setVisible(False)

        #second page
        self.back_button_j = QLabel(self.join_expanded)
        self.back_button_j.move(20,5)
        self.back_button_j.setTextFormat(Qt.RichText)
        self.back_button_j.setText("&#8592;")
        self.back_button_j.setObjectName("back_button")
        self.back_button_j.mousePressEvent = self.back_button_clicked

        self.deco = QLabel(self.join_expanded)
        self.deco.setObjectName("deco")
        self.deco.setText("ecmce")
        self.deco.move(175,12)

        self.welcome = QLabel(self.join_expanded)
        self.welcome.move(55,50)
        self.welcome.setText("Welcome!")
        self.welcome.setObjectName("welcome")

        self.code_input = QLabel(self.join_expanded)
        self.code_input.setText("Enter QUIZ CODE")
        self.code_input.setObjectName("input_prompts")
        self.code_input.move(95, 250)

        self.qcode_input = QLineEdit(self.join_expanded)
        self.qcode_input.setObjectName("input")
        self.qcode_input.move(75, 300)

        self.quiz_frame = QLabel(self)
        self.quiz_frame.setObjectName("frame-exp")
        self.quiz_frame.move(75, 100)
        self.quiz_frame.setVisible(False)
   
        self.Okay_btn = QPushButton(self.join_expanded)
        self.Okay_btn.setText("OK")
        self.Okay_btn.setObjectName("push-buttons")
        self.Okay_btn.move(170,530)
        self.Okay_btn.clicked.connect(self.OK_clicked)

        self.qtitle = QLabel(self.quiz_frame)
        #self.qtitle.setObjectName("input_prompts")
        self.qtitle.setStyleSheet("color: rgb(193, 191, 191); font-size: 50px;")
        self.qtitle.setFixedWidth(300)
        self.qtitle.move(100,5)

        self.a_frame = QLabel(self.quiz_frame)
        self.a_frame.setObjectName("q-frame")
        self.a_frame.move(5,65)
        self.a_frame.setVisible(True)

        self.quest = QLabel(self.a_frame)
        self.quest.setObjectName("input_prompts")
        self.quest.setFixedWidth(200)
        self.quest.move(20,15)

        self.qlabel = QLabel(self.a_frame)
        self.qlabel.setObjectName("input_prompts")
        self.qlabel.setWordWrap(True)
        self.qlabel.setFixedSize(350, 100)
        self.qlabel.move(20, 30)

        self.crct = QLabel(self.a_frame)
        self.crct.setTextFormat(Qt.RichText)
        self.crct.setText("&#10003;")
        self.crct.setObjectName("back_button")
        self.crct.move(10,190)
        self.crct.setVisible(False)

        self.ans_1 = QRadioButton(self.a_frame)
        self.ans_1.move(30,200)
        self.ans_1.toggled.connect(self.radio)

        self.option_1 = QLabel(self.a_frame)
        self.option_1.setObjectName("options")
        self.option_1.setFixedWidth(400)
        self.option_1.setWordWrap(True)
        self.option_1.move(50, 190)

        self.ans_2 = QRadioButton(self.a_frame)
        self.ans_2.move(30, 250)
        self.ans_2.toggled.connect(self.radio)

        self.option_2 = QLabel(self.a_frame)
        self.option_2.setObjectName("options")
        self.option_2.setFixedWidth(400)
        self.option_2.setWordWrap(True)
        self.option_2.move(50, 240)

        self.ans_3 = QRadioButton(self.a_frame)
        self.ans_3.move(30, 300)
        self.ans_3.toggled.connect(self.radio)

        self.option_3 = QLabel(self.a_frame)
        self.option_3.setObjectName("options")
        self.option_3.setFixedWidth(400)
        self.option_3.setWordWrap(True)
        self.option_3.move(50, 290)

        self.ans_4 = QRadioButton(self.a_frame)
        self.ans_4.move(30, 350)
        self.ans_4.toggled.connect(self.radio)

        self.option_4 = QLabel(self.a_frame)
        self.option_4.setObjectName("options")
        self.option_4.setFixedWidth(400)
        self.option_4.setWordWrap(True)
        self.option_4.move(50, 340)

        self.group = QButtonGroup()
        self.group.addButton(self.ans_1)
        self.group.addButton(self.ans_2)
        self.group.addButton(self.ans_3)
        self.group.addButton(self.ans_4)

        self.okay_btn = QPushButton(self.quiz_frame)
        self.okay_btn.setObjectName("push-buttons")
        self.okay_btn.setText("Submit")
        self.okay_btn.move(250, 550)
        self.okay_btn.clicked.connect(self.submit_btn_clicked)

        self.next_q = QPushButton(self.quiz_frame)
        self.next_q.setObjectName("push-buttons")
        self.next_q.setText("Next")
        self.next_q.move(250,550)
        self.next_q.clicked.connect(self.next_q_clicked)
        self.next_q.setVisible(False)

        self.exit_screen = QLabel(self)
        self.exit_screen.setObjectName("frame-exp")
        self.exit_screen.move(75, 100)
        self.exit_screen.setVisible(False)

        self.marks_obtained = QLabel(self.exit_screen)
        self.marks_obtained.setObjectName("options")
        self.marks_obtained.setFixedWidth(200)
        self.marks_obtained.move(100, 60)

        self.thnx = QLabel(self.exit_screen)
        self.thnx.setText("Thank you for taking the quiz :)")
        self.thnx.setWordWrap(True)
        self.thnx.setStyleSheet("color: rgb(193,191,191); font-size:25px; font=weight: bold;")
        self.thnx.move(70,555)

        self.show()

    def create_clicked(self, event):
        self.create_expanded.setVisible(True)
        self.join_btn.setVisible(False)
        self.create_btn.setVisible(False)

    def join_clicked(self, event):
        self.join_expanded.setVisible(True)
        self.join_btn.setVisible(False)
        self.create_btn.setVisible(False)

    def back_button_clicked(self, event):
        self.create_expanded.setVisible(False)
        self.join_expanded.setVisible(False)
        self.join_btn.setVisible(True)
        self.create_btn.setVisible(True)

    def start_c_clicked(self):

        self.instructions = QMessageBox()
        self.instructions.setText("--Fill in  the answers and choose the right one--")
        self.instructions.setObjectName("input_prompts")
        self.instructions.setWindowTitle("Instructions")
        #self.instructions.move(20,95)
        self.instructions.exec_()

        self.create_expanded.setVisible(False)
        self.create_q_frame.setVisible(True)
        self.q_frame.setVisible(True)

        title = self.name_input.text()
        self.l.append([title])

    def next_clicked(self):
        self.a += 1
        questn = self.q_input.toPlainText()
        mark = self.marks_input.value()
        opt_a = self.option_a.toPlainText()
        opt_b = self.option_b.toPlainText()
        opt_c = self.option_c.toPlainText()
        opt_d = self.option_d.toPlainText()
        if self.ans_a.isChecked():
            answr = self.option_a.toPlainText()
        elifself.ans_b.isChecked():
            answr = self.option_b.toPlainText()
        elifself.ans_c.isChecked():
            answr = self.option_c.toPlainText()
        else:
            answr = self.option_d.toPlainText()
        self.l.append([self.a, questn, opt_a, opt_b, opt_c, opt_d, answr, mark])

        self.group1.setExclusive(False)

        self.ans_a.setChecked(False)
        self.ans_b.setChecked(False)
        self.ans_c.setChecked(False)
        self.ans_d.setChecked(False)

        self.group1.setExclusive(True)

        self.q_input.clear()
        self.marks_input.clear()
        self.option_a.clear()
        self.option_b.clear()
        self.option_c.clear()
        self.option_d.clear()

    def submit_clicked(self):
        self.a += 1
        questn = self.q_input.toPlainText()
        mark = self.marks_input.value()
        opt_a = self.option_a.toPlainText()
        opt_b = self.option_b.toPlainText()
        opt_c = self.option_c.toPlainText()
        opt_d = self.option_d.toPlainText()
        if self.ans_a.isChecked():
            answr = self.option_a.toPlainText()
        elifself.ans_b.isChecked():
            answr = self.option_b.toPlainText()
        elifself.ans_c.isChecked():
            answr = self.option_c.toPlainText()
        else:
            answr = self.option_d
        self.l.append([self.a, questn, opt_a, opt_b, opt_c, opt_d, answr, mark])
        #print(self.l)
        self.create_quiz(self.l)

    def create_quiz(self,a):
        with open("{}.csv".format(self.quiz_code),"w",newline='') as f :
            csv_w=csv.writer(f,delimiter=',')
            csv_w.writerows(a)
        #print("successfully created")
        self.ty.setVisible(True)

    def OK_clicked(self):
        self.q_code = self.qcode_input.text()
        self.access_quiz()
        if self.flag == 0:
            self.join_expanded.setVisible(False)
            self.quiz_frame.setVisible(True) 
            self.qtitle.setText(self.l[0][0])
            self.len = len(self.l)
            self.L = self.l[self.x1]
            self.quest.setText("Question "+self.L[0])
            self.qlabel.setText(self.L[1])
            self.option_1.setText(self.L[2])
            self.option_2.setText(self.L[3])
            self.option_3.setText(self.L[4])
            self.option_4.setText(self.L[5])
            

    def submit_btn_clicked(self):
        self.x2 += 1
        if self.x2 <self.len:
            self.marks = int(self.l[self.x2][7])
            self.total += self.marks
            self.ryt_ans = self.l[self.x2][6]
            if self.ans_1.isChecked():
                if self.option_1.text() == self.ryt_ans:
                    self.no_of_crct += 1
                    self.count += self.marks
                    self.crct.setVisible(True)
                    self.crct.move(10, 190)
                else:
                    self.no_of_wrong += 1
                    if self.option_1.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 190)
                    elifself.option_2.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 240)
                    elifself.option_3.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 290)
                    else:
                        self.crct.setVisible(True)
                        self.crct.move(10, 340)
            elif self.ans_2.isChecked():
                if self.option_2.text() == self.ryt_ans:
                    self.no_of_crct += 1
                    self.count += self.marks
                    self.crct.setVisible(True)
                    self.crct.move(10, 240)
                else:
                    self.no_of_wrong += 1
                    if self.option_1.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 190)
                    elifself.option_2.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 240)
                    elifself.option_3.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 290)
                    else:
                        self.crct.setVisible(True)
                        self.crct.move(10, 340)
            elif self.ans_3.isChecked():
                if self.option_3.text() == self.ryt_ans:
                    self.no_of_crct += 1
                    self.count += self.marks
                    self.crct.setVisible(True)
                    self.crct.move(10, 290)
                else:
                    self.no_of_wrong += 1
                    if self.option_1.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 190)
                    elifself.option_2.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 240)
                    elifself.option_3.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 290)
                    else:
                        self.crct.setVisible(True)
                        self.crct.move(10, 340)
            elif self.ans_4.isChecked():
                if self.option_4.text() == self.ryt_ans:
                    self.no_of_crct += 1
                    self.count += self.marks
                    self.crct.setVisible(True)
                    self.crct.move(10, 340)
                else:
                    self.no_of_wrong += 1
                    if self.option_1.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 190)
                    elifself.option_2.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 240)
                    elifself.option_3.text() == self.ryt_ans:
                        self.crct.setVisible(True)
                        self.crct.move(10, 290)
                    else:
                        self.crct.setVisible(True)
                        self.crct.move(10, 340)
            else:
                self.unattempted += 1
                if self.option_1.text() == self.ryt_ans:
                    self.crct.setVisible(True)
                    self.crct.move(10, 190)
                elifself.option_2.text() == self.ryt_ans:
                    self.crct.setVisible(True)
                    self.crct.move(10, 240)
                elifself.option_3.text() == self.ryt_ans:
                    self.crct.setVisible(True)
                    self.crct.move(10, 290)
                else:
                    self.crct.setVisible(True)
                    self.crct.move(10, 340)
        self.okay_btn.setVisible(False)
        self.next_q.setVisible(True)

    def next_q_clicked(self):
        self.x1 += 1
        self.group.setExclusive(False)
        self.ans_1.setChecked(False)
        self.ans_2.setChecked(False)
        self.ans_3.setChecked(False)
        self.ans_4.setChecked(False)
        self.group.setExclusive(True)
        if self.x1 <self.len:
            self.crct.setVisible(False)
            self.L = self.l[self.x1]
            self.quest.setText("Question "+self.L[0])
            self.qlabel.setText(self.L[1])
            self.option_1.setText(self.L[2])
            self.option_2.setText(self.L[3])
            self.option_3.setText(self.L[4])
            self.option_4.setText(self.L[5])
            self.next_q.setVisible(False)
            self.okay_btn.setVisible(True)
        else:
            self.exit_screen.setVisible(True)
            self.marks_obtained.setText("Marks:"+str(self.count)+"/"+str(self.total))
            self.piechart()
            

    def piechart(self):
        self.crct.setVisible(False)
        self.series = QPieSeries()
        self.series.append("Correct", self.no_of_crct)
        self.series.append("Wrong", self.no_of_wrong)
        self.series.append("Unattempted", self.unattempted)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setBackgroundBrush(QColor(10,10,10))
        self.chart.legend().setLabelColor(Qt.gray)

        self.chartview = QChartView(self.chart,self.exit_screen)
        self.chartview.setGeometry(5,100,400,459)
        self.chartview.setStyleSheet("background-color: rgb(10,10,10);")
        #self.chartview.setBackgroundBrush(Qt.darkGray)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview.show()
       

    def access_quiz(self):
        try:
            with open("{}.csv".format(self.q_code),"r",newline='') as f :
                csv_r = csv.reader(f)
                for record in csv_r:
                    self.l.append(record)
                print(self.l)
                self.flag = 0
                return self.l

        except FileNotFoundError:
            self.flag = 1
            self.msg = QMessageBox()
            self.msg.setText("Invalid code")
            self.msg.setObjectName("input_prompts")
            self.msg.setWindowTitle("Message")
            self.msg.exec_()

    def radio(self):
        pass

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
