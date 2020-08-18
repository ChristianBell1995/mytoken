import json
import sys
from web3 import Web3, HTTPProvider

def __setup_contract():
    TOKEN_CONTRACT_ADDRESS = "0x03978B294209dFEa2E41Be5F99ec67bc4CE03fd3"
    CONTRACT_OWNER_ADDRESS = "0x811ec12357C81397DD48822335a9239C3005c3F9"
    # compile your smart contract with truffle first
    truffleFile = json.load(open('./contracts/Token.json'))
    abi = truffleFile['abi']
    bytecode = truffleFile['bytecode']

    # Connect web3 to Ganache
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
    print(w3.isConnected())
    # Get address of your contract i.e. the Token contract
    contract_address = Web3.toChecksumAddress(TOKEN_CONTRACT_ADDRESS)  # modify

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    # Contract instance in concise mode
    return w3.eth.contract(abi=abi, address=contract_address), w3

def __earn():
    contract_instance, w3 = __setup_contract()
    # The first time earning it may be a new user so we might want to create an account for them although this might happen in another method
    new_account = w3.eth.account.create()
    print("Address:")
    print(new_account.address)
    print('Private Key:')
    print(new_account.privateKey.hex())


    # Take the private key of the owner of the contract in order to earn points.
    CONTRACT_OWNER_PRIVATE_KEY = "fe4c8c9f704a0b1b55904aeaafeb07a09f100bdd877597b71cf71942f4f90a9f"
    private_key = CONTRACT_OWNER_PRIVATE_KEY  # modify
    acct = w3.eth.account.privateKeyToAccount(private_key)
    account_address = acct.address

    # To get owner of the contract:
    # contract_instance.functions.owner().call()

    tx = contract_instance.functions.earn(new_account.address, 1).buildTransaction(
        {'nonce': w3.eth.getTransactionCount(account_address)})
    # Get tx receipt to get contract address
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print('Transaction Receipt:')
    print(tx_receipt)

    print(tx_hash.hex())

def __burn():
    contract_instance, w3 = __setup_contract()


def __balance():
    contract_instance, w3 = __setup_contract()
    # Find the address of the person you want the balance of
    address = "0xb7B7657F1604e2a1469F7419AB1317Ce57EA06C5"
    print(contract_instance.functions.balances(address).call())

def run():
    if sys.argv[1] == 'earn':
        __earn()
    elif sys.argv[1] == 'balance':
        __balance()
    elif sys.argv[1] == 'burn':
        __burn()

if __name__ == '__main__':
    run()
