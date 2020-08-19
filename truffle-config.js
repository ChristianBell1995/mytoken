const path = require("path");

module.exports = {
  // See <http://truffleframework.com/docs/advanced/configuration>
  // to customize your Truffle configuration!
  contracts_build_directory: path.join(__dirname, "api/contracts"),
  networks: {
    develop: {
      port: 8545
    },
    test_net: {
      host: "",
      port: 8545,
      network_id: "*",
      from: "0x4d48EA8D7E989f85A8c61DA2b8D8601926BC6c6D",
      gas:4600000,
    }
  }
};
