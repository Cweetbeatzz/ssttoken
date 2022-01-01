from brownie import SSTToken
from scripts.helpers import get_account
from web3 import Web3


######################################qu####################################


def deploy_transfer_from(_sender, _recipient, _amount):
    account = get_account()
    sender = _sender
    recipent = _recipient
    amount = _amount
    initial_token_deploy = SSTToken[-1]
    transfer = initial_token_deploy.transferFrom(
        sender, recipent, amount, {"from": account}
    )
    transfer.wait(1)
    print(
        f"Successfully Transfered: {amount * 10 ** 18} SST From {sender} to {_recipient}"
    )


def main():
    deploy_transfer_from()
