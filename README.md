## Setup

Install the truffle framework with: `npm install -g truffle`

Make sure you have **Ganache** up and running in the background I downloaded the MacOS app https://www.trufflesuite.com/ganache
This runs a local blockchain that you can test and run your solidity contracts on. It automatically gives you 10 accounts with 100 ETH each and runs on http://127.0.0.1:7545 .

When **Ganache** is running in the background.
Run `truffle migrate` to migrate the smart contracts onto your local blockchain.

To run the python scripts:
```
    cd api
    brew install pyenv
    brew install pyenv-virtualenv
    pyenv install 3.7.6
    pyenv virtualenv 3.7.6 mytoken
    pyenv local mytoken
    pip install web3
```

## Notes and Tips

If you make any changes to smart contracts then you will have to run `truffle migrate --reset` to override the previous contracts. This is because contracts are immutable so you can't change them once they're on the blockchain.

Run `truffle console` to open a JS console where you can interact with your contracts. To get an instance of the election contract run ```Token.deployed().then(instance => { app = instance})``` then you can interact with the `app` object and inspect public interface of the contract.

To run the tests run `truffle test`
