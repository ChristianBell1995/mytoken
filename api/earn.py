import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

TOKEN_CONTRACT_ADDRESS = ""

# compile your smart contract with truffle first
truffleFile = json.load(open('./contracts/Token.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']

# Connect web3 to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
print(w3.isConnected())

new_accountt = w3.eth.account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
print(new_accountt)
# Get address of your contract i.e. the Token contract
contract_address = Web3.toChecksumAddress(TOKEN_CONTRACT_ADDRESS) #modify
# Take a private key from one of the accounts in order to load into web3
private_key = "" #modify
acct = w3.eth.account.privateKeyToAccount(private_key)
account_address = acct.address

# Instantiate and deploy contract
contract = w3.eth.contract(abi=abi, bytecode=bytecode)
# Contract instance in concise mode
contract_instance = w3.eth.contract(abi=abi, address=contract_address, ContractFactoryClass=ConciseContract)
# import pdb; pdb.set_trace()
# To get owner of the contract:
# contract_instance.functions.owner().call()

tx = contract_instance.earn("", 1, transact={'nonce': w3.eth.getTransactionCount(account_address) })
#Get tx receipt to get contract address
signed_tx = w3.eth.account.signTransaction(tx, key)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
print('Transaction Receipt:')
print(tx_receipt)

print(tx_hash.hex())