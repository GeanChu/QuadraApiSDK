import asyncio
from src.rest.client.account import AccountRoutes
from decouple import config
import pandas as pd


base_url = 'https://unified-api.quadra.trade'
api_key = 'q9ddI7vmDubsC9OC4a30IBeOyKP1wPBC'
secret_key = 'an8ECh7ZIxy44nFZrenmAeueQeGbWLnUB+13yp20U8/CZMln'


async def get_venues():
    # Public Routes Class
    client = AccountRoutes(base_url, api_key, secret_key)
    # Get contracts
    response = await client.venues()
    data = response['data']
    return data


if __name__ == '__main__':
    venues = asyncio.run(get_venues())
    venues_df = pd.DataFrame(venues)
    print(venues)
