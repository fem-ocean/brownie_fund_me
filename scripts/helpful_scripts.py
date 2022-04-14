from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "mainnet-fork-dev"]

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

        #means if the network is in development we are going to use the account with zero syntax otherwise we will pull fromm our config

        #we will add wallets in our config file. check brownie-config.yaml for this.

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")

    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from":get_account()})#check what d constructor take to add the parameters. And to get the address thats y assigned.200000000000000000000 was refactored using Web3,toWei(2000, "ether")
        print("Mocks Deployed!!!")
