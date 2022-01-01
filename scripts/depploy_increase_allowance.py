from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


######################################qu####################################


def deploy_increase_allowance(_address_spender, _uint256_addedValue):
    account = get_account()
    spender = _address_spender
    addedValue = _uint256_addedValue
    initial_token_deploy = SSTToken[-1]
    transaction = initial_token_deploy.increaseAllowance(
        spender, addedValue, {"from": account}
    )
    print("Transaction Successful")


######################################qu####################################


def main():
    deploy_increase_allowance()
