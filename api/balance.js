const fs = require('fs');
const Web3 = require('web3');
const dotenv = require('dotenv')
dotenv.config();

// const provider = new Web3('http://127.0.0.1:7545');
let web3 = new Web3('http://127.0.0.1:7545')
//web3
const contractJSON = JSON.parse(fs.readFileSync('./contracts/Token.json'), 'utf8');
const abi = contractJSON.abi;

const contract = new web3.eth.Contract(abi, process.env.CONTRACT_ADDRESS);

let receiverAccount = '0xf96026bCb580B28b9Cb977dfB9DF28E29d89367b'

contract.methods.balances(receiverAccount).call().then(receipt => {
  console.log('**********BALANCE*****************:')
  console.log(receipt)
})
