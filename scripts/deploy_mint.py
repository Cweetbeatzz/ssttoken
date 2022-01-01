from brownie import SSTToken
from scripts.helpers import get_account


##########################################################################


def deploy_mint(_addressaccount_to, _uint256amount):
    account = get_account()
    addressaccount = _addressaccount_to
    uint256amount = _uint256amount
    initial_token_deploy = SSTToken[-1]
    get_supply = initial_token_deploy.mint(
        addressaccount, uint256amount, {"from": account}
    )
    print("Mint Successful")


##########################################################################
def main():
    deploy_mint()
