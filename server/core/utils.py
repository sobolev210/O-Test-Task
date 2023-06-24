from web3 import Web3, EthereumTesterProvider
from django.conf import settings


def get_ethereum_node_connection() -> Web3:
    try:
        w3 = Web3(Web3.HTTPProvider(settings.REMOTE_NODE_ENDPOINT))
        assert w3.is_connected() is True
        return w3

    except AssertionError:
        raise RuntimeError("Could not connect to Ethereum node.")

    except Exception as e:
        raise RuntimeError(f"Error when connecting to Ethereum node. Error message: {e}")
