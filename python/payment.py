import pprint
import time
from eth_account import Account
from web3 import Web3
import sys
import sha3
import requests
Account.enable_unaudited_hdwallet_features()
url = "http://127.0.0.1/v4/nft_fans/notify"
# payment address
address = Web3.toChecksumAddress('0x084a136986966fb42e6353f547b518f53f73f13d')
abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"string","name":"orderid","type":"string"},{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Pay","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[{"internalType":"string","name":"orderid","type":"string"}],"name":"pay","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address payable","name":"target_address","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
nft_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"cost","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"hiddenMetadataUri","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxMintAmountPerTx","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_mintAmount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"mintForAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"revealed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"buri","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cost","type":"uint256"}],"name":"setCost","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxMintAmountPerTx","type":"uint256"}],"name":"setMaxMintAmountPerTx","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_state","type":"bool"}],"name":"setPaused","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_state","type":"bool"}],"name":"setRevealed","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
# dev = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
# pro = 'https://bsc-dataseed.binance.org/'
# env = 'https://kovan.infura.io/v3/31b561c046134b85a884b367c937d46a'
env = 'https://goerli.infura.io/v3/31b561c046134b85a884b367c937d46a'
w3 = Web3(Web3.HTTPProvider(env))
contract = w3.eth.contract(address=address, abi=abi)


def handle_event(receipt):
    result = contract.events.Pay().processReceipt(receipt)
    orderid = result[0]['args']['orderid'].hex()
    sender = result[0]['args']['sender']
    amount = result[0]['args']['amount']

    user_account_buyer = Account.from_mnemonic(sys.argv[2])
    user_address_buyer = user_account_buyer.address
    to_address = user_address_buyer

    user_account_nftowner = Account.from_mnemonic(sys.argv[6])
    user_address_nftowner = user_account_nftowner.address
    w3.eth.default_account = user_account_nftowner
    user_address_nftowner = Web3.toChecksumAddress(user_address_nftowner)
    tokenid = int(sys.argv[1])

    nft_address = Web3.toChecksumAddress(sys.argv[5])
    nft_contract_instance = w3.eth.contract(address=nft_address, abi=nft_abi)

    nonce_nft = w3.eth.get_transaction_count(user_address_nftowner)
    tx_unsign_nft = nft_contract_instance.functions.transferFrom(user_address_nftowner, to_address, tokenid).build_transaction(
        {'from': user_address_nftowner, 'gasPrice': w3.eth.gas_price, 'nonce': nonce_nft})
    tx_sign_nft = user_account_nftowner.sign_transaction(tx_unsign_nft)
    tx_hash_nft = w3.eth.send_raw_transaction(tx_sign_nft.rawTransaction)
    receipt_nft = w3.eth.wait_for_transaction_receipt(tx_hash_nft)
    pprint.pprint(receipt_nft["status"])
    pprint.pprint(receipt_nft["transactionHash"])
    url_request = url + "?orderid=" + str(tokenid) + "&sender=" + sender + "&amount=" + str(amount) + "&nft_address=" + nft_address
    requests.get(url_request)


def log_loop(event_filter, poll_interval):
    while True:
        try:
            for event in event_filter.get_new_entries():
                handle_event(event)
                time.sleep(poll_interval)
        except BaseException as e:
            print(e)


cmd = sys.argv[3]
if not cmd:
    print("format error")
elif cmd == "receipt":
    tx_hash = sys.argv[2]
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)  # 获取Transaction地址执行结果
    handle_event(receipt)
elif cmd == "buy":
    user_account = Account.from_mnemonic(sys.argv[2])
    #user_account = Account.from_key(sys.argv[2])
    orderid = sys.argv[1]
    value = float(sys.argv[4])
    user_address = user_account.address
    w3.eth.default_account = user_account
    user_address = Web3.toChecksumAddress(user_address)
    nonce = w3.eth.get_transaction_count(user_address)
    tx_unsign = contract.functions.pay(orderid).build_transaction(
        {'from': user_address, 'gasPrice': w3.eth.gas_price, 'nonce': nonce, 'value': w3.toWei(value, 'ether')})

    tx_sign = user_account.sign_transaction(tx_unsign)
    tx_hash = w3.eth.send_raw_transaction(tx_sign.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    pprint.pprint(receipt["status"])
    pprint.pprint(receipt["transactionHash"])
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)  # 获取Transaction地址执行结果
    handle_event(receipt)

#block_filter = w3.eth.filter({'fromBlock': 'latest', 'address': address})
#log_loop(block_filter, 2)

