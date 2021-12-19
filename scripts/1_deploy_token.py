from brownie import OurToken
from scripts.helpful_scripts import get_account, get_contract
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    acc = get_account()
    our_token = OurToken.deploy(initial_supply, {"from": acc})
    print(our_token.name())
    print(our_token.symbol())
