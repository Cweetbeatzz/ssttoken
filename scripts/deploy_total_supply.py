from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


##########################################################################


def deploy_total_supply():
    account = get_account()
    initial_token_deploy = SSTToken[-1]
    get_supply = initial_token_deploy.totalSupply()
    print(f"Total Supply:", {get_supply})
    return get_supply


##########################################################################
def main():
    deploy_total_supply()
