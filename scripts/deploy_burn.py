from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3

##########################################################################


def deploy_burn(_addressaccount, _uint256amount):
    account = get_account()
    addressaccount = _addressaccount
    uint256amount = _uint256amount
    initial_token_deploy = SSTToken[-1]
    burn = initial_token_deploy._burn(addressaccount, uint256amount, {"from": account})
    print("Burn Successful")


##########################################################################
def main():
    deploy_burn()
