const fs = require('fs');
const Web3 = require('web3');
const dotenv = require('dotenv')
dotenv.config();

// const provider = new Web3('http://127.0.0.1:7545');
let web3 = new Web3('http://127.0.0.1:7545')
//web3
const contractJSON = JSON.parse(fs.readFileSync('./contracts/Token.json'), 'utf8');
const abi = contractJSON.abi;

// let contractAddress = "0x9055770A94f1A933688548872144F76373BFB76a"
const contract = new web3.eth.Contract(abi, process.env.CONTRACT_ADDRESS);

// let ownerAccount = '0xDCD70A8ddE44aa36ACCB933f4164CD2532E1653E';
let receiverAccount = '0xf96026bCb580B28b9Cb977dfB9DF28E29d89367b'

contract.methods.earn(receiverAccount, 5).send({
  from: process.env.OWNER_ACCOUNT,
}).then(receipt => {
  console.log('**********EARN RECEIPT*****************:')
  console.log(receipt)
  console.log('**********END RECEIPT*****************')
  const amount = receipt['events']['Earn']['returnValues']['amount']
  const user = receipt['events']['Earn']['returnValues']['user']
  console.log(`User: ${user} earned ${amount} points`)
})
