from PyQt5 import QtCore, QtWidgets
import yfinance as yf
import plotly.graph_objs as go
from PyQt5.QtWidgets import QMessageBox


class Ui_stock1(object):
    def realtime(self):
        if self.stock_name.text()=="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Please enter a stock symbol")

            # setting Message box window title
            msg.setWindowTitle("Exception Error :(")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            # start the app
            retval = msg.exec_()
            return
        # Raw Package

        # Market Data

        # Graphing/Visualization
        import datetime as dt

        # Override Yahoo Finance
        yf.pdr_override()

        # stock = input("Enter a stock ticker symbol: ")

        # Retrieve stock data frame (df) from yfinance API at an interval of 1m
        df = yf.download(tickers=self.stock_name.text(), period='1d', interval='1m')

        # print(df)

        # Declare plotly figure (go)
        fig = go.Figure()

        fig.add_trace(go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'], name='market data'))

        fig.update_layout(
            title=str(self.stock_name.text()) + ' Live Share Price:',
            yaxis_title='Stock Price (INR per Shares)')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

        fig.show()

    def setupUi(self, stock1):
        stock1.setObjectName("stock1")
        stock1.resize(597, 355)
        stock1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(stock1)
        self.centralwidget.setObjectName("centralwidget")
        self.stock_name = QtWidgets.QLineEdit(self.centralwidget)
        self.stock_name.setGeometry(QtCore.QRect(200, 120, 201, 41))
        self.stock_name.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                      "font: 15pt \"Comic Sans MS\";")
        self.stock_name.setText("")
        self.stock_name.setObjectName("stock_name")
        self.show_graph = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.realtime())
        self.show_graph.setGeometry(QtCore.QRect(200, 220, 201, 61))
        self.show_graph.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                      "font: 10pt \"Comic Sans MS\";")
        self.show_graph.setObjectName("show_graph")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 40, 281, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 14pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        stock1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(stock1)
        self.statusbar.setObjectName("statusbar")
        stock1.setStatusBar(self.statusbar)

        self.retranslateUi(stock1)
        QtCore.QMetaObject.connectSlotsByName(stock1)
        self.show_graph.setDefault(True)
        self.show_graph.setAutoDefault(True)

    def retranslateUi(self, stock1):
        _translate = QtCore.QCoreApplication.translate
        stock1.setWindowTitle(_translate("stock1", "Real Time Graph"))
        self.show_graph.setText(_translate("stock1", "Click to show graph"))
        self.label.setText(_translate("stock1", "Enter stock symbol below"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    stock1 = QtWidgets.QMainWindow()
    ui = Ui_stock1()
    ui.setupUi(stock1)
    stock1.show()
    sys.exit(app.exec_())
