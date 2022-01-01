from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


##########################################################################


def deploy_before_token_transfer(_from_address_acc, _to_address_acc, _uint256amount):
    account = get_account()
    from_address_acc = _from_address_acc
    to_address_acc = _to_address_acc
    uint256amount = _uint256amount
    initial_token_deploy = SSTToken[-1]
    get_supply = initial_token_deploy._beforeTokenTransfer(
        from_address_acc, to_address_acc, uint256amount
    )
    get_supply.wait(1)
    print("Successful")


##########################################################################
def main():
    deploy_before_token_transfer()
