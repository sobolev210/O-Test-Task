import pytest
from web3 import EthereumTesterProvider, Web3, exceptions


from core.services.wallet_service import WalletService
from core.models import Wallet


@pytest.fixture
def w3():
    return Web3(EthereumTesterProvider())


@pytest.fixture
def wallet_service(w3):
    return WalletService(w3)


@pytest.fixture
def existing_ethereum_wallet_address(w3):
    account = w3.eth.account.create()
    return account.address


@pytest.mark.django_db
class TestWalletService:

    def test_create_wallet(self, wallet_service):
        assert len(Wallet.objects.all()) == 0
        wallet = wallet_service.create_wallet("ETH")

        assert len(Wallet.objects.all()) == 1
        assert wallet.public_key is not None
        assert wallet.private_key is not None
        assert wallet.currency == "ETH"

    def test_get_balance(self, wallet_service, existing_ethereum_wallet_address):
        balance = wallet_service.get_balance(existing_ethereum_wallet_address)
        assert balance == 0

    def test_get_balance_incorrect_address(self, wallet_service, existing_ethereum_wallet_address):
        with pytest.raises(exceptions.InvalidAddress):
            wallet_service.get_balance("123")
