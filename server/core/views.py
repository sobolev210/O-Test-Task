from rest_framework import viewsets
from rest_framework.response import Response
from web3 import Web3

from .utils import get_ethereum_node_connection


class WalletViewSet(viewsets.GenericViewSet):
    queryset = None  # update
    serializer_class = None  # update
    w3: Web3 = get_ethereum_node_connection()

    def list(self, request):
        return Response("List of wallets (balances included)")

    def create(self, request):
        account = self.w3.eth.account.create()
        return Response(
            f"Wallet created. Address: {account.address}, "
            f"private key: {account.key}, "
            f"balance: {self.w3.eth.get_balance(account.address)}",
        )
