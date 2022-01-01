from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3

##########################################################################


def deploy_ssttoken_symbol():
    account = get_account()
    initial_token_deploy = SSTToken[-1]
    symbol = initial_token_deploy.symbol()
    print(symbol)
    return symbol


##########################################################################


def main():
    deploy_ssttoken_symbol()
