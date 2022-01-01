from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


######################################qu####################################


def deploy_decrease_allowance(_address_spender, _uint256_subtractedValue):
    account = get_account()
    spender = _address_spender
    subtractedValue = _uint256_subtractedValue
    initial_token_deploy = SSTToken[-1]
    transaction = initial_token_deploy.decreaseAllowance(
        spender, subtractedValue, {"from": account}
    )
    print("Transaction Successful")


##########################################################################
def main():
    deploy_decrease_allowance()
