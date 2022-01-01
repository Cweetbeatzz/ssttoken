from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3

##########################################################################


def deploy_balanceof(_address):
    account = get_account()
    prev_deploy = SSTToken[-1]
    acc_address = _address
    # account_address = account.address()
    get_balance = prev_deploy.balanceOf(acc_address)
    # bal_in_usd = Web3.toWei(get_balance, "ether")
    print(f"Balance:", {get_balance})


##########################################################################


def main():
    deploy_balanceof("0x643AEEB212E3C4996CD7025C05F2FD622B48621C")
