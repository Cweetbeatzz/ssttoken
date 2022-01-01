from brownie import SSTToken
from scripts.helpers import get_account

##########################################################################


def deploy_snapshot():
    account = get_account()
    initial_token_deploy = SSTToken[-1]
    pausing_contract = initial_token_deploy.snapshot({"from": account})
    pausing_contract.wait(1)
    print("Successfull")


##########################################################################


def main():
    deploy_snapshot()
