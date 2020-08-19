## Setup

Install the truffle framework with: `npm install -g truffle`

Make sure you have **Ganache** up and running in the background I downloaded the MacOS app https://www.trufflesuite.com/ganache
This runs a local blockchain that you can test and run your solidity contracts on. It automatically gives you 10 accounts with 100 ETH each and runs on http://127.0.0.1:7545 .

When **Ganache** is running in the background.
Run `truffle migrate` to migrate the smart contracts onto your local blockchain.

To get setup for the python scripts:
```
    cd api
    brew install pyenv
    brew install pyenv-virtualenv
    pyenv install 3.7.6
    pyenv virtualenv 3.7.6 mytoken
    pyenv local mytoken
    pip install web3
```
Before running the scripts you have to find the values on your local blockchain for `CONTRACT_OWNER_PRIVATE_KEY` and `TOKEN_CONTRACT_ADDRESS`. These can be found either by looking in ganache under the 'transactions' tab there should be a row that says 'contract created' - the `TOKEN_CONTRACT_ADDRESS` will be the 'created contract address'. Then to find the owner's private key you need to go back into the accounts tab and find the account that does not have 100.00 ETH - the private key of this will be the `CONTRACT_OWNER_PRIVATE_KEY`. You can also do this programmatically: 
1. Run `truffle console`
2. Run `Token.deployed().then(instance => { app = instance})` to get an instance of your deployed contract.
3. Run `app.owner()` to get the address of the owner of the contract, you can then look in Ganache to find the private key for this address to get the `CONTRACT_OWNER_PRIVATE_KEY`.
4. Run `app.address` for the `TOKEN_CONTRACT_ADDRESS`.

There are four different ways to call the script.
For registering a new user:
```
python run.py register
```
For earning:
```
python run.py earn <address> <amount>
```
For burning:
```
python run.py burn <address> <amount>
```
For balance:
```
python run.py balance <address>
```

## Notes and Tips

If you make any changes to smart contracts then you will have to run `truffle migrate --reset` to override the previous contracts. This is because contracts are immutable so you can't change them once they're on the blockchain.

Run `truffle console` to open a JS console where you can interact with your contracts. To get an instance of the election contract run ```Token.deployed().then(instance => { app = instance})``` then you can interact with the `app` object and inspect public interface of the contract.

To run the tests run `truffle test`

I found this article useful - https://levelup.gitconnected.com/dapps-development-for-python-developers-f52b32b54f28.

## Deploying

To run ganache on a remote server I used this article https://medium.com/@rshadmon/how-to-create-a-private-ethereum-blockchain-node-hosted-on-aws-in-5-minutes-for-free-86fc006d3f7a. 

Once you have an instance up and running with the correct firewall rules, ssh into it and run the following commands:
```
sudo apt-get update
sudo apt install npm
sudo npm install -g ganache-cli
ganache-cli --host <private ip address> --port 8545
```
This will then run the ganache client in your server. To deploy your truffle contracts onto the remote blockchian update the `host` of the `test_net` network to be the public ip address of your instance in the `truffle-config.js` file. Then to deploy your contracts run:
```
truffle migrate --network test_net
```