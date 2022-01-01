from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3

##########################################################################


def deploy_unpause():
    account = get_account()
    initial_token_deploy = SSTToken[-1]
    unpausing_contract = initial_token_deploy.unpause({"from": account})
    unpausing_contract.wait(1)
    print("Contract Started...")


##########################################################################


def main():
    deploy_unpause()
