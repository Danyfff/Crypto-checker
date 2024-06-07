from web3 import Web3, HTTPProvider


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
            'rpc': 'https://1rpc.io/linea',
            'name': 'Linea',
            'currency': 'eth'
            }
        }
    
    def __connect_node(self, rpc_chein):
        return Web3(HTTPProvider(rpc_chein))
    
    def get_chein_info(self, chein):
        '''Вывод данных о сети'''
        web3 = self.__connect_node(self.rpc[chein]['rpc'])
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

    def get_balance_wallet_by_chein(self, checksum_address, chein):
        web3 = self.__connect_node(self.rpc[chein]['rpc'])
        return web3.eth.get_balance(checksum_address)

    def get_balance_wallet(self, wallet_address):
        checksum_address = self.get_checksum_address(wallet_address)
        if checksum_address:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
                  f"Address: {wallet_address}")
        else:
            print('EROR: There is no such address')
            return
        
        for chein in self.rpc:
            name_chein = self.rpc[chein]['name']
            print(f'{name_chein}: {self.get_balance_wallet_by_chein(checksum_address, chein)}')
            
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

w3manager = Web3Manager()