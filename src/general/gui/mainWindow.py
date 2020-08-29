import sys
import re

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem


sys.path.append("qt-creator/hsp-saas/")
from MainWindow import Ui_MainWindow

sys.path.append("../tools")
from classloader import classloader
from bidict import bidict

sys.path.append("../")
import baseApiInterface as baseApiInterface

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    serviceNameToServiceMap=bidict()
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.cl=classloader()
        self.cl.importAllPythonFiles()
        for category in self.cl.getAllCategories():
            self.cb_input_category.addItem(category[0].upper() + category[1:])
            self.cb_output_category.addItem(category[0].upper() + category[1:])
        self.cb_input_category.currentIndexChanged.connect(lambda: self.changeCategory(self.cb_input_category))
        self.cb_output_category.currentIndexChanged.connect(lambda: self.changeCategory(self.cb_output_category))

        self.serviceNameToServiceMap=bidict()
        for service in baseApiInterface.baseApiInterface.__subclasses__():
            self.serviceNameToServiceMap[service]=service.name

        self.changeCategory(self.cb_input_category)
        self.changeCategory(self.cb_output_category)

        self.cb_input_service.currentIndexChanged.connect(lambda: self.changeService(self.cb_input_service))
        self.cb_output_service.currentIndexChanged.connect(lambda: self.changeService(self.cb_output_service))

        self.changeService(self.cb_input_service)
        self.changeService(self.cb_output_service)
        
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(self.accept)



    def changeCategory(self, combobox):
        serviceCombobox=None
        if combobox == self.cb_input_category:
            serviceCombobox=self.cb_input_service
            rowCount=self.tb_input_auth.rowCount()
            for item in range(0,self.tb_input_auth.rowCount()):
                self.tb_input_auth.removeRow((rowCount-1)-item)
            self.tb_input_auth.update()
        else:
            serviceCombobox=self.cb_output_service
            rowCount=self.tb_output_auth.rowCount()
            for item in range(0,self.tb_output_auth.rowCount()):
                self.tb_output_auth.removeRow((rowCount-1)-item)
            self.tb_output_auth.update()
        serviceCombobox.clear()

        rowCount=self.tb_value_matching.rowCount()
        for item in range(0,rowCount):
            self.tb_value_matching.removeRow((rowCount-1)-item)
        self.tb_value_matching.update()

        for service in baseApiInterface.baseApiInterface.__subclasses__():
            print(service.name + " " + service.id_tag + " ")
            if combobox.currentText().lower() in service.id_tag.split('#'):
                #print("is in tag " + combobox.currentText().lower())
                serviceCombobox.addItem(service.name)
        serviceCombobox.update()

    def changeService(self, combobox):
        rowCount=self.tb_value_matching.rowCount()
        for item in range(0, rowCount):
            self.tb_value_matching.removeRow((rowCount-1)-item)
        self.tb_value_matching.update()

        if combobox.currentText() != '' and combobox.currentText() != None:
            service=self.serviceNameToServiceMap.inverse[combobox.currentText()][0]
            authbox=None
            if combobox == self.cb_input_service:
                authbox=self.tb_input_auth
                rowCount=self.tb_input_auth.rowCount()
                for item in range(0,self.tb_input_auth.rowCount()):
                    self.tb_input_auth.removeRow((rowCount-1)-item)
                self.tb_input_auth.update()
            else:
                authbox=self.tb_output_auth
                rowCount=self.tb_output_auth.rowCount()
                for item in range(0,self.tb_output_auth.rowCount()):
                    self.tb_output_auth.removeRow((rowCount-1)-item)
                self.tb_output_auth.update()
            for entry in service.authInfo:
                rowPosition=authbox.rowCount()
                authbox.insertRow(rowPosition)
                item=QTableWidgetItem(str(entry))
                authbox.setItem(rowPosition, 0, item)
                item.setFlags(QtCore.Qt.ItemIsEditable)
            authbox.update()


            if self.cb_output_service.currentText() != None and self.cb_input_service.currentText() != None:
                outputDO=self.serviceNameToServiceMap.inverse[self.cb_output_service.currentText()][0].correspondingDataObjectClass
                inputDO=self.serviceNameToServiceMap.inverse[self.cb_input_service.currentText()][0].correspondingDataObjectClass
                if outputDO != None and inputDO != None:
                    lmembers = [attr for attr in dir(outputDO) if not callable(getattr(outputDO, attr)) and not attr.startswith("__")]
                    rmembers = [attr for attr in dir(inputDO) if not callable(getattr(inputDO, attr)) and not attr.startswith("__")]

                    for m in lmembers:
                        qcombo_s2 = QtWidgets.QComboBox(self.centralWidget)
                        qcombo_s2.setGeometry(QtCore.QRect(350, 80, 281, 25))
                        qcombo_s2.setObjectName("cb_qcombo_s2")
                        qcombo_s2.setEditable(True)

                        for n in rmembers:
                            qcombo_s2.addItem(str(n))

                        rowPosition=self.tb_value_matching.rowCount()
                        self.tb_value_matching.insertRow(rowPosition)
                        itemCol0=QTableWidgetItem(str(m))   
                        itemCol2=QTableWidgetItem(None)   
                        self.tb_value_matching.setItem(rowPosition, 0, itemCol0)
                        self.tb_value_matching.setCellWidget(rowPosition, 1, qcombo_s2)
                        self.tb_value_matching.setItem(rowPosition, 2, itemCol2)
                        self.tb_value_matching.update()
                        
                    'choose attributes of input-service which are equal or close to the attributes of the output service'         
                    for row in range(0, self.tb_value_matching.rowCount()):
                        index = self.tb_value_matching.cellWidget(row, 1).findText(self.tb_value_matching.item(row,0).text(), QtCore.Qt.MatchFixedString)
                        if index >= 0:
                            self.tb_value_matching.cellWidget(row, 1).setCurrentIndex(index)
                        else:
                            index = self.tb_value_matching.cellWidget(row, 1).findText('*' + self.tb_value_matching.item(row,0).text() + '*', QtCore.Qt.MatchWildcard)
                            if index >= 0:
                                self.tb_value_matching.cellWidget(row, 1).setCurrentIndex(index)
                            else:
                                index=-1
                                matched=False
                                for item in range(0, self.tb_value_matching.cellWidget(row, 1).count()):
                                    self.tb_value_matching.cellWidget(row, 1).setCurrentIndex(item)
                                    regex=re.compile(self.tb_value_matching.cellWidget(row, 1).currentText(), re.IGNORECASE)
                                    if re.search(regex, self.tb_value_matching.item(row,0).text()):
                                        matched=True
                                        break
                                if not matched:
                                     self.tb_value_matching.cellWidget(row, 1).setCurrentIndex(-1)
 

    def reject(self):
        self.close()

    def accept(self):
        lservice = self.serviceNameToServiceMap.inverse[self.cb_output_service.currentText()][0]
        lservice = lservice()
        lAuthInfoDict=dict()
        for row in range(0, self.tb_output_auth.rowCount()):
            if self.tb_output_auth.item(row, 1) == None:
                self.tb_output_auth.setItem(row, 1, QTableWidgetItem(str("")))
            lAuthInfoDict[self.tb_output_auth.item(row, 0).text()]=self.tb_output_auth.item(row, 1).text()
        lservice.authInfo = lAuthInfoDict
 
        rservice = self.serviceNameToServiceMap.inverse[self.cb_input_service.currentText()][0]
        rservice = rservice()
        rAuthInfoDict=dict()
        for row in range(0, self.tb_input_auth.rowCount()):
            if self.tb_input_auth.item(row, 1) == None:
                self.tb_input_auth.setItem(row, 1, QTableWidgetItem(str("")))
            rAuthInfoDict[self.tb_input_auth.item(row, 0).text()]=self.tb_input_auth.item(row, 1).text()
        rservice.authInfo = rAuthInfoDict


#self, substrIdTag = None, filterOptions = [], transformationOptions = [], addAggOptions = []
        'define the transformationOptions'
        transformationOptions=[]
        rowCount=self.tb_value_matching.rowCount()
        for row in range(0, rowCount-1):
            l=dict()
            if hasattr(lservice.correspondingDataObjectClass, self.tb_value_matching.cellWidget(row,1).currentText()):
                l[str(self.tb_value_matching.item(row,0).text())] = '$' + str(self.tb_value_matching.cellWidget(row,1).currentText())
                transformationOptions.append(l)
            else:
                l[str(self.tb_value_matching.item(row,0).text())] = str(self.tb_value_matching.cellWidget(row,1).currentText())
                transformationOptions.append(l)

        'define the filterOptions'
        filterOptions=[]
        rowCount=self.tb_value_matching.rowCount()
        for row in range(0, rowCount-1):
            l=dict()
            if not str(self.tb_value_matching.item(row,2).text()) == '':
                l[str(self.tb_value_matching.cellWidget(row,1).currentText())] = str(self.tb_value_matching.item(row,2).text())
                filterOptions.append(l)

        #a23e749b14acda2f61fde476dba9f317abb9d5425fc13a542b535239a6a77515
        #lservice.uniqueCalendarId='kst496bmane3rty9b7'
        errMsgExtract="data could not be extracted from input service; "
        errMsgInject="data could not be injected in output service; "
        errOccuredExtract=False
        errOccuredInject=False
        try:
            rservice.extractFromAPI()
        except:
            errMsgExtract=errMsgExtract+str(sys.exc_info()[1])
            errOccuredExtract=True
        
        try:
            lservice.requestInjectionInAPI(transformationOptions=transformationOptions, filterOptions=filterOptions)
        except:
            errMsgInject=errMsgInject+str(sys.exc_info()[1])
            errOccuredInject=True
        if errOccuredExtract:
            print(errMsgExtract)
        if errOccuredInject:
            print(errMsgInject)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
