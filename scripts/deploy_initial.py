from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


##########################################################################
initial_supply = 1000 * 10 ** 18 or Web3.toWei(1000, "ether")


def deploy_initial():
    account = get_account()
    initial_token_deploy = SSTToken.deploy({"from": account})
    print("Deploy Successful")
    print(initial_token_deploy.name())
    print(initial_token_deploy.address())


##########################################################################
def main():
    deploy_initial()
