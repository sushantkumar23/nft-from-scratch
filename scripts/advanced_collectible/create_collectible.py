from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_breed
import time

STATIC_SEED = 123


def main():
    dev = accounts.add(config['wallets']['from_key'])
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    transaction = advanced_collectible.createCollectible(
        STATIC_SEED, "None", {"from": dev}
    )
    transaction.wait(1)
    time.sleep(35)
    request_id = transaction.events['requestedCollectible']['requestId']
    token_id = advanced_collectible.requestIdToTokenId(request_id)
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    print(f'Dog breed of tokenId {token_id} is {breed}')
    
