import os
import warnings
import logging
import ipfshttpclient

from brownie.exceptions import BrownieEnvironmentWarning

from yearn.apy import calculate_apy, get_samples, ApyError
from yearn.v1.registry import Registry as RegistryV1
from yearn.v2.registry import Registry as RegistryV2

from yearn.v2.vaults import Vault as VaultV2
from yearn.v2.strategies import Strategy as StrategyV2

warnings.simplefilter("ignore", BrownieEnvironmentWarning)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("yearn.apy")


def main():
    address = os.environ.get("IPFS_NODE_ADDRESS")
    key = os.environ.get("IPFS_NODE_KEY")
    secret = os.environ.get("IPFS_NODE_SECRET")

    client = ipfshttpclient.connect(address, auth=(key, secret))
    print(client.id())

    # data = []

    # samples = get_samples()

    # v1_registry = RegistryV1()

    # for vault in v1_registry.vaults:
    #     apy = calculate_apy(vault, samples)
    #     data.append({"product": apy.type, "name": vault.name, "apy": apy.net_apy})

    # v2_registry = RegistryV2()

    # for vault in v2_registry.vaults:
    #     try:
    #         apy = calculate_apy(vault, samples)
    #         data.append({"product": apy.type, "name": vault.name, "apy": apy.net_apy})
    #     except ApyError as error:
    #         logger.error(error)
    #     except Exception as error:
    #         print(vault)
    #         raise error

    # data.sort(key=lambda x: -x["apy"])
    # print(tabulate(data, floatfmt=",.0%"))