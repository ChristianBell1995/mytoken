const Web3 = require('web3');

// const provider = new Web3('http://127.0.0.1:7545');
let web3 = new Web3('http://127.0.0.1:7545')

const newAccount = web3.eth.accounts.create()
console.log(newAccount)
