from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


##########################################################################


def deploy_after_token_transfer(_from_address_acc, _to_address_acc, _uint256amount):
    account = get_account()
    from_address_acc = _from_address_acc
    to_address_acc = _to_address_acc
    uint256amount = _uint256amount
    initial_token_deploy = SSTToken[-1]
    get_supply = initial_token_deploy._afterTokenTransfer(
        from_address_acc, to_address_acc, uint256amount, {"from": account}
    )
    get_supply.wait(1)
    print("Successful")


##########################################################################
def main():
    deploy_after_token_transfer()
