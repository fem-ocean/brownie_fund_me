from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
#from web3 import Web3...since its used in the helpfulscripts

def deploy_fund_me():
    account = get_account()
    #we need to pass our pricefeed address to our fund me contract before "from account below". This is how we pass a variable to the FundMe constructor

    #we will say if we are on a persistent network like rinkeby, use the associated address
    #otherwise, deploy mocks

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS: #
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"] #add diff addresses to brownie config instead of hardcoding thr address
        # The if statement is saying if we are not on a development network, pull the address from the config
    else:
        deploy_mocks() #this line replaces many of the code below for the purpose of refactoring.
        #print(f"The active network is {network.show_active()}")
        #print("Deploying mocks...")

        #if len(MockV3Aggregator) <= 0:
            #The if statement above is saying if the list of the different V3 aggregators deployed is <= 0 then we can deploy it
            # we can then import mockv3Aggregator and deploy it the same way we deployed our other contracts.
            #mock_aggregator = MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from":account})#check what d constructor take to add the parameters. And to get the address thats y assigned.200000000000000000000 was refactored using Web3,toWei(2000, "ether")
           #print("Mocks Deployed!!!")
        
        price_feed_address = MockV3Aggregator[-1].address #mock_aggregator.address...the  -1 indexing helps us access the latest deployed address
            

    fund_me = FundMe.deploy(
        price_feed_address, 
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),)     #since there would be a state change u need to add "from account"...publish_source means we are verifying our contractan we would like to publish our source code
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()