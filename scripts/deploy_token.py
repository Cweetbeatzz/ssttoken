from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3

##########################################################################
def deploy_initial():
    account = get_account()
    initial_token_deploy = SSTToken.deploy({"from": account})
    print(initial_token_deploy.address)
    print("Token Deployed...")


##########################################################################
def main():
    deploy_initial()


##########################################################################
