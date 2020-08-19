sudo apt-get update
sudo apt install npm

sudo npm install -g ganache-cli
ganache-cli --host 10.128.0.2 --port 8545 -m '' &
