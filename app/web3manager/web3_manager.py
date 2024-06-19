from web3 import Web3, HTTPProvider
from eth_account import Account


class Web3Manager():
    
    rpc = {
        'eth':{
            'rpc': 'https://uk.rpc.blxrbdn.com',
            'name': 'Ethereum Mainnet',
            'currency': 'eth'
            },
        'arbitrum_one':{
            'rpc': 'https://bsc-rpc.publicnode.com',
            'name': 'Arbitrum One',
            'currency': 'eth'
            },
        'arbitrum_nova':{
            'rpc': 'https://arbitrum-nova-rpc.publicnode.com',
            'name': 'Arbitrum Nova',
            'currency': 'eth'
            },
        'base':{
            'rpc': 'https://base-rpc.publicnode.com',
            'name': 'Base',
            'currency': 'eth'
            },
        'polygon':{
            'rpc': 'https://polygon-bor-rpc.publicnode.com',
            'name': 'Polygon Mainnet',
            'currency': 'matic'
            },
        'optimism':{
            'rpc': 'https://op-pokt.nodies.app',
            'name': 'OP Mainnet',
            'currency': 'eth'
            },
        'linea':{
            'rpc': 'https://linea.decubate.com',
            'name': 'Linea',
            'currency': 'eth'
            }
        }
    
    def connect_node(self, rpc_chein):
        rpc = self.rpc[rpc_chein]['rpc']
        return Web3(HTTPProvider(rpc))
    
    def get_chein_info(self, chein):
        '''Вывод данных о сети'''
        web3 = self.connect_node(chein)
        if web3:
            print(
                "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
                f"Name chain: {self.rpc[chein]['name']}\n"
                f"Gas price: {web3.eth.gas_price}\n"
                f"Current block number: {web3.eth.block_number}\n"
                f"Number of current chain is {web3.eth.chain_id}\n"
                "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
                )
        else:
            print('Eror. Connecting to the node failed!!!')

    def get_checksum_address(self, wallet_address):
        try:
            return Web3.to_checksum_address(wallet_address)
        except:
            return 

    def get_balance_wallet_by_chein(self, wallet_address, chein):
        checksum_address = self.get_checksum_address(wallet_address)
        web3 = self.connect_node(chein)
        balance_in_wei = web3.eth.get_balance(checksum_address)
        balance_in_eth = web3.from_wei(balance_in_wei, 'ether')
        return balance_in_eth

w3manager = Web3Manager()