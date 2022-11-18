import pprint
from eth_account import Account
from web3 import Web3
import sys
from web3.middleware import geth_poa_middleware
from mnemonic import Mnemonic
from web3.gas_strategies.time_based import fast_gas_price_strategy, slow_gas_price_strategy,medium_gas_price_strategy
Account.enable_unaudited_hdwallet_features()

root_address = "0x5d6c443bA08fBCcF699C05c5A32133F764A62930"


dev = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
pro = 'https://bsc-dataseed.binance.org/'
env = pro
w3 = Web3(Web3.HTTPProvider(env))



cmd = sys.argv[2]

if not cmd:
    print("Address is empty,Format:python main.py user_address cmd ....others")
elif cmd == "create_wallet":
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=128)
    account = w3.eth.account.from_mnemonic(words, account_path="m/44'/60'/0'/0/0")
    private_key = account.privateKey.hex()
    address = Web3.toChecksumAddress(account.address)
    print(private_key)
    print(address)
    print(words)
