from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


##########################################################################
def deploy_transfer(_recipient, _amount):
    account = get_account()
    initial_token_deploy = SSTToken[-1]
    recipent = _recipient
    amount = _amount
    transfer = initial_token_deploy.transfer(recipent, amount, {"from": account})
    print(f"Successfully Transfered: {amount * 10 ** 18} SST")


##########################################################################


def main():
    deploy_transfer("0x1671921C6D1B285CDCD1EEF9973E8D9AE622F5C2", 100)
