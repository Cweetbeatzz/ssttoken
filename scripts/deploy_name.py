from brownie import SSTToken
from scripts.helpers import get_account

##########################################################################


def deploy_ssttoken():
    account = get_account()
    initial_token_deploy = SSTToken[-1]
    name = initial_token_deploy.name()
    print(name)
    return name
