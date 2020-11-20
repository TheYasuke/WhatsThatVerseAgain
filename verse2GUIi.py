# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Verse2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import WhatsThatVerseApp

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 548)
        Dialog.setAutoFillBackground(False)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_3.setSpacing(7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verseStackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.verseStackedWidget.setAutoFillBackground(True)
        self.verseStackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verseStackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verseStackedWidget.setObjectName("verseStackedWidget")
        self.verseStackedWidgetPage1 = QtWidgets.QWidget()
        self.verseStackedWidgetPage1.setObjectName("verseStackedWidgetPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verseStackedWidgetPage1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
    
        self.verseLabel = QtWidgets.QLabel(self.verseStackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.verseLabel.setFont(font)
        self.verseLabel.setObjectName("verseLabel")
        self.verticalLayout_2.addWidget(self.verseLabel)
        
        self.verseEnter = QtWidgets.QLineEdit(self.verseStackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.verseEnter.setFont(font)
        self.verseEnter.setObjectName("verseEnter")
        self.verticalLayout_2.addWidget(self.verseEnter)
       
        self.versionLabel = QtWidgets.QLabel(self.verseStackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.versionLabel.setFont(font)
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout_2.addWidget(self.versionLabel)
        
        self.versionEnter = QtWidgets.QLineEdit(self.verseStackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.versionEnter.setFont(font)
        self.versionEnter.setObjectName("versionEnter")
        self.verticalLayout_2.addWidget(self.versionEnter)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)

        self.searchButton = QtWidgets.QPushButton(self.verseStackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchButton.setFont(font)
        self.searchButton.setIconSize(QtCore.QSize(16, 32))
        self.searchButton.setAutoRepeat(True)
        self.searchButton.setAutoDefault(True)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.showResults)
        self.verticalLayout_2.addWidget(self.searchButton)

        self.verseStackedWidget.addWidget(self.verseStackedWidgetPage1)

        self.resultsPage = QtWidgets.QWidget()
        self.resultsPage.setObjectName("resultsPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.resultsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.resultLabel = QtWidgets.QLabel(self.resultsPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resultLabel.setFont(font)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)

        self.resultBox = QtWidgets.QTextBrowser(self.resultsPage)
        self.resultBox.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.resultBox.setFont(font)
        self.resultBox.setObjectName("resultBox")
        self.verticalLayout.addWidget(self.resultBox)

        self.deepSearchButton = QtWidgets.QPushButton(self.resultsPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deepSearchButton.setFont(font)
        self.deepSearchButton.setObjectName("deepSearchButton")
        self.verticalLayout.addWidget(self.deepSearchButton)
        self.deepSearchButton.clicked.connect(self.deepSearch)

        self.NewSearchButton = QtWidgets.QPushButton(self.resultsPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NewSearchButton.setFont(font)
        self.NewSearchButton.setObjectName("NewSearchButton")
        self.NewSearchButton.clicked.connect(self.showSearch)
        self.verticalLayout.addWidget(self.NewSearchButton)

        self.verseStackedWidget.addWidget(self.resultsPage)
        self.gridLayout_3.addWidget(self.verseStackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.verseStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Whats That Verse Again?"))
        self.verseLabel.setText(_translate("Dialog", "Enter Phrase:"))
        self.versionLabel.setText(_translate("Dialog", "Enter Version:"))
        self.searchButton.setText(_translate("Dialog", "Search"))
        self.NewSearchButton.setText(_translate("Dialog", "New Search"))

    def showResults(self, Dialog):
        
        self.verse = self.verseEnter.text()
        self.version = self.versionEnter.text()
        self.results=10
        self.pages=0
        _translate = QtCore.QCoreApplication.translate
        
        if any(c.isalpha() for c in self.version) and any(c.isalpha() for c in self.verse):#if verse and version has characters continue
            self.verseStackedWidget.setCurrentIndex(1)
            self.deepSearchButton.setText(_translate("Dialog", "Deep Search"))
            self.deepSearchButton.setEnabled(True)

            if type(WhatsThatVerseApp.main(self.verse,self.version,self.results,self.pages)) is dict:
                #print(WhatsThatVerseApp.passageDict)
                if not WhatsThatVerseApp.bibleDict:
                    self.resultLabel.setText(_translate("Dialog", "No Results:"))
                    self.resultBox.append("Maybe try a Deep Search?")
                    return

                for scripture, passage in WhatsThatVerseApp.passageDict.items():
                    self.resultBox.append(f"<span style='font-weight:bold;text-decoration: underline;'>{scripture}</span>")
                    self.resultBox.append(f"<span style='font-weight:normal;'>{passage}</span>")
                    self.resultBox.append("")
                self.resultLabel.setText(_translate("Dialog", "{} Results:".format(len(WhatsThatVerseApp.passageDict))))
                self.resultBox.moveCursor(QtGui.QTextCursor.Start)
            
            else:#If invalid version or phrase isnt found
                self.resultLabel.setText(_translate("Dialog", "No Results:"))
                self.resultBox.append("Please check the Bible version.")
                self.deepSearchButton.setEnabled(False)
            '''
                self.resultLabel.setText(_translate("Dialog", "No Results:"))
                if WhatsThatVerseApp.bibleDict:
                    self.resultBox.append("Please check the Bible version.")
                    self.deepSearchButton.setEnabled(False)
                else:
                    print("test")
                    print(WhatsThatVerseApp.bibleDict)
                    self.resultBox.append("Maybe try a Deep Search?")
                #Disable deep searach if bad version, else ask for deep search
            '''
    def showSearch(self): 
        self.verseStackedWidget.setCurrentIndex(0)
        self.verseEnter.clear()
        self.resultBox.clear()
        WhatsThatVerseApp.passageDict.clear()
        WhatsThatVerseApp.bibleDict.clear()
     
    def deepSearch(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.resultBox.clear()
        WhatsThatVerseApp.passageDict.clear()
        WhatsThatVerseApp.bibleDict.clear()
        self.results+=20
        self.pages+=1

        if self.pages < 5:
            WhatsThatVerseApp.main(self.verse,self.version,self.results,self.pages)
            for scripture, passage in WhatsThatVerseApp.passageDict.items():
                    self.resultBox.append(f"<span style='font-weight:bold;text-decoration: underline;'>{scripture}</span>")
                    self.resultBox.append(f"<span style='font-weight:normal;'>{passage}</span>")
                    self.resultBox.append("")
            self.resultLabel.setText(_translate("Dialog", "{} Results:".format(len(WhatsThatVerseApp.passageDict))))
            self.deepSearchButton.setText(_translate("Dialog", "Deep Search ({})".format(self.pages)))
            self.resultBox.moveCursor(QtGui.QTextCursor.Start)
        else:
            self.resultBox.clear()
            self.resultBox.append("No new results. Please do new search.")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('cross2.png'))
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
