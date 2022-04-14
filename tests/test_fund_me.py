from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest  


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1) 
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee #assert keyword is used for debugging. if condition is false, assertion is raised.
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    #fund_me.withdraw({"from": bad_actor}) #from Fundme.sol, only the oowner is allowed to call this function.What happens if som1else tries to call the withdraw function.
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor}) #we are saying we want u to revert when u try to call this line
