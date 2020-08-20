import json
import sys
from web3 import Web3, HTTPProvider

CONTRACT_OWNER_PRIVATE_KEY = "f0a80534b109d17c1a66c4b4c84a12787bea85203bd02ace90ec74ca4fad61a8"

def __setup_contract():
    TOKEN_CONTRACT_ADDRESS = "0x137533Cf7941b41e558B439D075F278Bc4Fd7d34"
    # compile your smart contract with truffle first
    truffleFile = json.load(open('./contracts/Token.json'))
    abi = truffleFile['abi']
    bytecode = truffleFile['bytecode']

    # Connect web3 to Ganache
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
    print(f'Are we connected to the blockchain??? {w3.isConnected()}')
    # Get address of your contract i.e. the Token contract
    contract_address = Web3.toChecksumAddress(TOKEN_CONTRACT_ADDRESS)  # modify

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    # Contract instance in concise mode
    return w3.eth.contract(abi=abi, address=contract_address), w3

def __register():
    contract_instance, w3 = __setup_contract()

    account = w3.eth.account.create()
    # Rather than printing out here we will write to Firebase with the address and to some KMS equivalent with the private key
    print("Address:")
    print(account.address)
    print('Private Key:')
    print(account.privateKey.hex())


def __earn(user_address, amount):
    contract_instance, w3 = __setup_contract()
    # Take the private key of the owner of the contract in order to earn points.
    acct = w3.eth.account.privateKeyToAccount(CONTRACT_OWNER_PRIVATE_KEY)
    owner_address = acct.address

    tx = contract_instance.functions.earn(user_address, int(amount)).buildTransaction(
        {'nonce': w3.eth.getTransactionCount(owner_address)})
    # Get tx receipt to get contract address
    signed_tx = w3.eth.account.signTransaction(tx, CONTRACT_OWNER_PRIVATE_KEY)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    event = contract_instance.events.Earn().processReceipt(tx_receipt)
    print('Transaction Receipt:')
    print(tx_receipt)
    print('Event:')
    print(event)


def __burn(user_address, amount):
    contract_instance, w3 = __setup_contract()
    # Take the private key of the owner of the contract in order to burn points.
    acct = w3.eth.account.privateKeyToAccount(CONTRACT_OWNER_PRIVATE_KEY)
    owner_address = acct.address

    tx = contract_instance.functions.burn(user_address, int(amount)).buildTransaction(
        {'nonce': w3.eth.getTransactionCount(owner_address)})
    # Get tx receipt to get contract address
    signed_tx = w3.eth.account.signTransaction(tx, CONTRACT_OWNER_PRIVATE_KEY)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    event = contract_instance.events.Burn().processReceipt(tx_receipt)
    print('Transaction Receipt:')
    print(tx_receipt)
    print('Event:')
    print(event)


def __balance(user_address):
    contract_instance, w3 = __setup_contract()
    # Find the address of the person you want the balance of
    print(contract_instance.functions.balances(user_address).call())

def run():
    if sys.argv[1] == 'register':
        __register()
    elif sys.argv[1] == 'earn':
        __earn(user_address=sys.argv[2], amount=sys.argv[3])
    elif sys.argv[1] == 'balance':
        __balance(user_address=sys.argv[2])
    elif sys.argv[1] == 'burn':
        __burn(user_address=sys.argv[2], amount=sys.argv[3])

if __name__ == '__main__':
    run()
