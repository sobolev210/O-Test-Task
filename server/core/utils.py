from web3 import Web3, EthereumTesterProvider


def get_ethereum_node_connection():
    try:
        w3 = Web3(EthereumTesterProvider())
        assert w3.is_connected() is True
        return w3

    except AssertionError:
        raise RuntimeError("Could not connect to Ethereum node.")

    except Exception as e:
        raise RuntimeError(f"Error when connecting to Ethereum node. Error message: {e}")
