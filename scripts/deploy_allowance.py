from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


######################################qu####################################


def deploy_allowance(_address_owner, _address_spender):
    account = get_account()
    owner = _address_owner
    spender = _address_spender
    initial_token_deploy = SSTToken[-1]
    get_approve = initial_token_deploy.allowance(owner, spender)
    print("Successful")


######################################qu####################################


def main():
    deploy_allowance()
