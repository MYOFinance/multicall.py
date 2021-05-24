from enum import IntEnum


class Network(IntEnum):
    Mainnet = 1
    Kovan = 42
    Rinkeby = 4
    Görli = 5
    xDai = 100
    Polygon_Mainnet = 137
    Polygon_Mumbai = 80001
    BSC = 56


MULTICALL_ADDRESSES = {
    Network.Mainnet: '0xeefBa1e63905eF1D7ACbA5a8513c70307C1cE441',
    Network.Kovan: '0x2cc8688C5f75E365aaEEb4ea8D6a480405A48D2A',
    Network.Rinkeby: '0x42Ad527de7d4e9d9d011aC45B31D8551f8Fe9821',
    Network.Görli: '0x77dCa2C955b15e9dE4dbBCf1246B4B85b651e50e',
    Network.xDai: '0xb5b692a88BDFc81ca69dcB1d924f59f0413A602a',
    Network.Polygon_Mainnet: '0x00214Df1c38d22Dcf43baA81b4c86AD2B9d6300F',
    Network.Polygon_Mumbai: '0xA3e7Af097dbB1AA1118744FF0C4c7CC4aC2f597F',
    Network.BSC: '0x1Ee38d535d541c55C9dae27B12edf090C608E6Fb',
}