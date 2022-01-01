from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


######################################qu####################################


def deploy_approve(_spender, _amount):
    spender = _spender
    amount = _amount
    account = get_account()
    initial_token_deploy = SSTToken[-1]
    get_approve = initial_token_deploy.approve(spender, amount, {"from": account})
    print("Transaction Approved")


##########################################################################
def main():
    deploy_approve()
