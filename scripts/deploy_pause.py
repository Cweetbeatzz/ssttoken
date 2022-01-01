from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3

##########################################################################


def deploy_pause():
    account = get_account()
    initial_token_deploy = SSTToken[-1]
    pausing_contract = initial_token_deploy.pause({"from": account})
    pausing_contract.wait(1)
    print("Contract Paused...")


##########################################################################


def main():
    deploy_pause()
