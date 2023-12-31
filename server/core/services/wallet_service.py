import json

from django.conf import settings
from web3 import Web3, exceptions
from eth_account.account import Account

from core.models import Wallet


class WalletService:

    def __init__(self, ethereum_node_connection: Web3):
        self.w3 = ethereum_node_connection

    def create_wallet(self, currency: str):
        account = self.w3.eth.account.create()
        encrypted_private_key = Account.encrypt(account.key, settings.PRIVATE_KEY_ENCRYPTION_PASS)
        wallet = Wallet(
            currency=currency,
            public_key=account.address,
            private_key=json.dumps(encrypted_private_key)
        )
        wallet.save()
        return wallet

    def get_balance(self, address: str):
        try:
            balance_wei = self.w3.eth.get_balance(address)
            return self.w3.from_wei(balance_wei, 'ether')
        except exceptions.InvalidAddress:
            print(f"Attempt to get balance for invalid address: {address}")
            raise

