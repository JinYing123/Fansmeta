import pprint
from eth_account import Account
from web3 import Web3
import sys
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import fast_gas_price_strategy, slow_gas_price_strategy,medium_gas_price_strategy
Account.enable_unaudited_hdwallet_features()


env = 'https://goerli.infura.io/v3/31b561c046134b85a884b367c937d46a/'
w3 = Web3(Web3.HTTPProvider(env))


w3.middleware_onion.inject(geth_poa_middleware, layer=0)

cmd = sys.argv[2]

if not cmd:
    print("Address is empty,Format:python main.py user_address cmd ....others")
elif cmd == "balance":
    user_address = Web3.toChecksumAddress(sys.argv[1])
    balance = w3.eth.get_balance(user_address)
    print(balance)
else:
    print(Web3.toText(hexstr="0x0000000000000000000000005d6c443ba08fbccf699c05c5a32133f764a62930"))
    print("command not exist")

