from PyQt6.QtWidgets import QMainWindow
from .windows.main_ui import Ui_MainWindow
from .web3manager.web3_manager import w3manager

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.serch_btn.clicked.connect(self.get_balanses_wallet)
        
    def get_balanses_wallet(self):
        wallet_adress = self.wallet_line.text()
        if wallet_adress:
            self.eth_label.setText(str(w3manager.get_balance_wallet_by_chein(wallet_adress, 'eth')) + ' eth')
            self.arbitrum_one_label.setText(str(w3manager.get_balance_wallet_by_chein(wallet_adress, 'arbitrum_one')) + ' eth')
            self.base_label.setText(str(w3manager.get_balance_wallet_by_chein(wallet_adress, 'base')) + ' eth')
            self.arbitrum_nova_label.setText(str(w3manager.get_balance_wallet_by_chein(wallet_adress, 'arbitrum_nova')) + ' eth')
            self.polygon_label.setText(str(w3manager.get_balance_wallet_by_chein(wallet_adress, 'polygon')) + ' eth')
            self.optimism_label.setText(str(w3manager.get_balance_wallet_by_chein(wallet_adress, 'optimism')) + ' eth')
            self.linea_label.setText(str(w3manager.get_balance_wallet_by_chein(wallet_adress, 'linea')) + ' eth')