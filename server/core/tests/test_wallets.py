import json

import pytest
from web3 import EthereumTesterProvider, Web3, exceptions

from core.models import Wallet
from core.services.wallet_service import WalletService


@pytest.fixture
def w3():
    return Web3(EthereumTesterProvider())


@pytest.fixture
def wallet_service(w3):
    return WalletService(w3)


@pytest.fixture
def existing_ethereum_wallet(w3):
    return w3.eth.account.create()


def check_private_key_is_encrypted(encrypted_private_key):
    assert type(encrypted_private_key) == dict
    assert "crypto" in encrypted_private_key


@pytest.mark.django_db
class TestWalletService:

    def test_create_wallet(self, wallet_service):
        assert len(Wallet.objects.all()) == 0

        wallet = wallet_service.create_wallet("ETH")

        assert len(Wallet.objects.all()) == 1
        assert wallet.private_key is not None
        assert wallet.currency == "ETH"
        check_private_key_is_encrypted(json.loads(wallet.private_key))

    def test_get_balance(self, wallet_service, existing_ethereum_wallet):
        balance = wallet_service.get_balance(existing_ethereum_wallet.address)
        assert balance == 0

    def test_get_balance_incorrect_address(self, wallet_service):
        with pytest.raises(exceptions.InvalidAddress):
            wallet_service.get_balance("123")
