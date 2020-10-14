# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expert_system.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from collections import Counter
import random

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(774, 804)
        font = QtGui.QFont()
        font.setPointSize(13)
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(30, 100, 121, 31))
        self.label_name.setObjectName("label_name")
        self.label_age = QtWidgets.QLabel(Form)
        self.label_age.setGeometry(QtCore.QRect(30, 140, 121, 31))
        self.label_age.setObjectName("label_age")
        self.label_insurance = QtWidgets.QLabel(Form)
        self.label_insurance.setGeometry(QtCore.QRect(30, 180, 121, 31))
        self.label_insurance.setObjectName("label_insurance")
        self.textEdit_name = QtWidgets.QTextEdit(Form)
        self.textEdit_name.setGeometry(QtCore.QRect(180, 100, 301, 31))
        self.textEdit_name.setObjectName("textEdit_name")
        self.textEdit_age = QtWidgets.QTextEdit(Form)
        self.textEdit_age.setGeometry(QtCore.QRect(180, 140, 301, 31))
        self.textEdit_age.setObjectName("textEdit_age")
        self.textEdit_insurance = QtWidgets.QTextEdit(Form)
        self.textEdit_insurance.setGeometry(QtCore.QRect(180, 180, 301, 31))
        self.textEdit_insurance.setObjectName("textEdit_insurance")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(550, 60, 181, 181))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_photo = QtWidgets.QPushButton(Form)
        self.pushButton_photo.setGeometry(QtCore.QRect(550, 266, 181, 31))
        self.pushButton_photo.setObjectName("pushButton_photo")
        self.pushButton_photo.clicked.connect(self.get_photo)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 9, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 246, 451, 51))
        self.pushButton.clicked.connect(self.diagnose)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_questions = QtWidgets.QLabel(Form)
        self.label_questions.setGeometry(QtCore.QRect(30, 319, 701, 41))
        self.label_questions.setText("")
        self.label_questions.setObjectName("label_questions")
        self.label_answer_yes_or_no = QtWidgets.QLabel(Form)
        self.label_answer_yes_or_no.setGeometry(QtCore.QRect(30, 370, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_answer_yes_or_no.setFont(font)
        self.label_answer_yes_or_no.setObjectName("label_answer_yes_or_no")
        self.textEdit_answer = QtWidgets.QTextEdit(Form)
        self.textEdit_answer.setGeometry(QtCore.QRect(233, 370, 351, 31))
        self.textEdit_answer.setObjectName("textEdit_answer")
        self.pushButton_confirm = QtWidgets.QPushButton(Form)
        self.pushButton_confirm.setGeometry(QtCore.QRect(600, 370, 131, 31))
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.pushButton_confirm.clicked.connect(self.get_answer)
        self.label_output = QtWidgets.QLabel(Form)
        self.label_output.setGeometry(QtCore.QRect(30, 410, 701, 181))
        self.label_output.setText("")
        self.label_output.setObjectName("label_output")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 609, 701, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_expected_disease = QtWidgets.QLabel(self.widget)
        self.label_expected_disease.setObjectName("label_expected_disease")
        self.horizontalLayout.addWidget(self.label_expected_disease)
        self.label_expected_disease_2 = QtWidgets.QLabel(self.widget)
        self.label_expected_disease_2.setText("")
        self.label_expected_disease_2.setObjectName("label_expected_disease_2")
        self.horizontalLayout.addWidget(self.label_expected_disease_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_doctor = QtWidgets.QLabel(self.widget)
        self.label_doctor.setObjectName("label_doctor")
        self.horizontalLayout_2.addWidget(self.label_doctor)
        self.label_doctor_2 = QtWidgets.QLabel(self.widget)
        self.label_doctor_2.setText("")
        self.label_doctor_2.setObjectName("label_doctor_2")
        self.horizontalLayout_2.addWidget(self.label_doctor_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_doctor_speciality = QtWidgets.QLabel(self.widget)
        self.label_doctor_speciality.setObjectName("label_doctor_speciality")
        self.horizontalLayout_5.addWidget(self.label_doctor_speciality)
        self.label_doctor_spciality_2 = QtWidgets.QLabel(self.widget)
        self.label_doctor_spciality_2.setText("")
        self.label_doctor_spciality_2.setObjectName("label_doctor_spciality_2")
        self.horizontalLayout_5.addWidget(self.label_doctor_spciality_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_room = QtWidgets.QLabel(self.widget)
        self.label_room.setObjectName("label_room")
        self.horizontalLayout_3.addWidget(self.label_room)
        self.label_room_2 = QtWidgets.QLabel(self.widget)
        self.label_room_2.setText("")
        self.label_room_2.setObjectName("label_room_2")
        self.horizontalLayout_3.addWidget(self.label_room_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_cost = QtWidgets.QLabel(self.widget)
        self.label_cost.setObjectName("label_cost")
        self.horizontalLayout_4.addWidget(self.label_cost)
        self.label_cost_2 = QtWidgets.QLabel(self.widget)
        self.label_cost_2.setText("")
        self.label_cost_2.setObjectName("label_cost_2")
        self.horizontalLayout_4.addWidget(self.label_cost_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Expert System"))
        self.label_name.setText(_translate("Form", "Patient Name"))
        self.label_age.setText(_translate("Form", "Patient Age"))
        self.label_insurance.setText(_translate("Form", "Patient Insurance"))
        self.label.setText(_translate("Form", "photo"))
        self.pushButton_photo.setText(_translate("Form", "Load Photo"))
        self.label_2.setText(_translate("Form", "DIAGNOSTIC EXPERT SYSTEM"))
        self.pushButton.setText(_translate("Form", "START DIAGNOSIS"))
        self.label_answer_yes_or_no.setText(_translate("Form", "Answer with yes / no :"))
        self.textEdit_answer.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_confirm.setText(_translate("Form", "Confirm"))
        self.label_expected_disease.setText(_translate("Form", "Expected Disease"))
        self.label_doctor.setText(_translate("Form", "Doctor"))
        self.label_doctor_speciality.setText(_translate("Form", "Doctor Speciality"))
        self.label_room.setText(_translate("Form", "Room"))
        self.label_cost.setText(_translate("Form", "Cost"))

    def initialize(self):
        diseases = {
            'Coronary artery disease (CAD)':
                ['pain', 'numbness in the chest', 'dizziness', 'weakness', 'fatigue', 'nausea', 'vomiting'],
            'Stroke':
                ['numbness', 'weakness', 'fatigue in one side of the body', 'difficulty speaking'],
            'Lower respiratory infections (LRI)':
                ['shortness of breath', 'weakness', 'fatigue', 'fever', 'cough'],
            'Chronic obstructive pulmonary disease (COPD)':
                ['cough', 'shortness of breath', 'wheezing', 'chest tightness'],
            'Lung cancer':
                ['cough', 'shortness of breath', 'chest pain', 'weakness', 'fatigue', 'weight loss'],
            'Diabetes mellitus (DM)':
                ['weakness', 'fatigue', 'nausea', 'weight loss', 'blurred vision'],
            'hyperthyroidism':
                ['weight loss', 'fatigue', 'weakness', 'rapid heart rate', 'nervousness'],
            'Allergy':
                ['nausea', 'vomiting', 'wheezing', 'dizziness', 'itching', 'swelling'],
            'Arthritis':
                ['fatigue', 'pain', 'swelling', 'joint redness', 'joint warmth'],
            'Asthma':
                ['shortness of breath', 'chest pain', 'chest tightness', 'wheezing'],
            'HIV':
                ['nausea', 'vomiting', 'fatigue', 'cough', 'shortness of breath', 'fever'],
            'diarrhoeal diseases':
                ['fever', 'nausea', 'abdominal pain and cramps', 'bloating'],
            'Cirrhosis':
                ['weakness', 'weight loss', 'itching', 'nausea', 'pain', 'vomiting'],
            'acute bronchitits':
                ['cough', 'fatigue', 'shortness of breath', 'fever', 'chest discomfort'],
            'heart failure':
                ['weakness', 'fatigue', 'cough', 'shortness of breath', 'wheezing', 'swelling']
        }
        x = []
        for i in diseases:
            x += diseases[i]

        x = [i.lower() for i in x]

        stats = Counter(x)

        return diseases, stats

    def eliminate_when_yes(self, diseases_dict, symptom):
        to_eliminate = []
        for disease in diseases_dict:
            if symptom not in diseases_dict[disease]:
                to_eliminate.append(disease)
        for disease in to_eliminate:
            diseases_dict.pop(disease)
        return diseases_dict

    def get_symptom(self, stats):
        for symptom, count in stats.items():
            if count == max(stats.values()):
                return symptom

    def eliminate_when_no(self, diseases_dict, symptom):
        to_eliminate = []
        for disease in diseases_dict:
            if symptom in diseases_dict[disease]:
                to_eliminate.append(disease)
        for disease in to_eliminate:
            diseases_dict.pop(disease)
        return diseases_dict

    def update_stats(self, diseases, not_to_repeat):
        x = []
        for i in diseases:
            x += diseases[i]

        x = [i.lower() for i in x]
        stats = Counter(x)
        for i in not_to_repeat:
            stats.pop(i)
        return stats

    def get_stats(self, diseases):
        x = []
        for i in diseases:
            x += diseases[i]

        x = [i.lower() for i in x]
        stats = Counter(x)
        return stats

    ans = ""
    def get_answer(self):
        self.ans = self.textEdit_answer.toPlainText()
        self.textEdit_answer.setText("")
        self.hasBeenProcessed = True

    def generate_dr_cost_room(self, expected_disease):
        doctors = ['Dr.William Hartnell',
                   'Dr.Patrick Troughton',
                   'Dr.Jon Pertwee',
                   'Dr.Tom Baker',
                   'Dr.Peter Davison',
                   'Dr.Colin Baker',
                   'Dr.Sylvester McCoy',
                   'Dr.Paul McGann',
                   'Dr.Christopher Eccleston',
                   'Dr.David Tennant',
                   'Dr.Matt Smith']

        dr_speciality = {'Dr.William Hartnell': 'cardiologist',
                         'Dr.Patrick Troughton': 'Neurologist',
                         'Dr.Jon Pertwee': 'pulmonologist',
                         'Dr.Tom Baker': 'Endocrinologist',
                         'Dr.Peter Davison': 'allergist',
                         'Dr.Colin Baker': 'Rheumatologists',
                         'Dr.Sylvester McCoy': 'gastroenterologist',
                         'Dr.Paul McGann': 'pulmonologist',
                         'Dr.Christopher Eccleston': 'gynecologist',
                         'Dr.David Tennant': 'Endocrinologist',
                         'Dr.Matt Smith': 'pulmonologist'}

        disease_speciality = {
            'Coronary artery disease (CAD)': 'cardiologist',
            'Stroke': 'Neurologist',
            'Lower respiratory infections (LRI)': 'pulmonologist',
            'Chronic obstructive pulmonary disease (COPD)': 'pulmonologist',
            'Lung cancer': 'pulmonologist',
            'Diabetes mellitus (DM)': 'Endocrinologist',
            'hyperthyroidism': 'Endocrinologist',
            'Allergy': 'allergist',
            'Arthritis': 'Rheumatologists',
            'Asthma': 'allergist',
            'HIV': 'gynecologist',
            'diarrhoeal diseases': 'gastroenterologist',
            'Cirrhosis': 'gastroenterologist',
            'acute bronchitits': 'pulmonologist',
            'heart failure': 'cardiologist'
        }

        doctor = doctors[random.randint(0, 10)]
        room = random.randint(150, 250)

        if disease_speciality[expected_disease] == dr_speciality[doctor]:
            cost = 50
        else:
            cost = 100

        return doctor, room, cost, dr_speciality[doctor]

    def get_photo(self):
        w = QtWidgets.QWidget()
        filename = QtWidgets.QFileDialog.getOpenFileName(w, 'Open File', '/')
        print(filename)
        pixmap = QPixmap(filename[0]).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.show()

    def diagnose(self):
        diseases, stats = self.initialize()
        symptoms_not_to_repeat = []
        while len(diseases) >= 2:
            symptom = self.get_symptom(stats)
            self.label_questions.setText("Do you have {} ?".format(symptom))
            print("Do you have {} ?".format(symptom))
            #ans = input("Do you have {} ?".format(symptom))
            #ans = self.get_answer()

            self.hasBeenProcessed = False
            while (self.hasBeenProcessed is not True):
                QtCore.QCoreApplication.processEvents()

            print(self.ans)
            #print("exit loop")

            if self.ans == "yes":
                expected_disease = self.eliminate_when_yes(diseases, symptom)
                symptoms_not_to_repeat.append(symptom)
                stats = self.update_stats(diseases, symptoms_not_to_repeat)
            elif self.ans == "no":
                expected_disease = self.eliminate_when_no(diseases, symptom)
                stats = self.get_stats(diseases)
                stats = self.update_stats(diseases, symptoms_not_to_repeat)
            else:
                print("please only answer with yes/no")
                pass

            # stats = update_stats(diseases, symptoms_not_to_repeat)
            # stats.pop(symptom)

            output = ""
            for i in diseases:
                output += str(diseases[i]) + "\n"
            self.label_output.setText("Expected-to-have Symptoms" + "\n" + output)

            ### pprint(diseases)
            ### pprint(stats)
            ### print("")

        ### print("Expected Disease is {}".format(list(expected_disease.keys())[0]))
        expected_disease = list(expected_disease.keys())[0]
        doctor, room, cost, dr_speciality = self.generate_dr_cost_room(expected_disease)
        self.label_expected_disease_2.setText(expected_disease)
        self.label_doctor_2.setText(doctor)
        self.label_doctor_spciality_2.setText(dr_speciality)
        self.label_room_2.setText(str(room))
        self.label_cost_2.setText(str(cost))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
