# OSRS-NET
Simple OSRS API wrapper for Grand Exchange prices and Hiscores levels/experience.

Can be installed easily from PyPi with `pip install osrs_net`

## Example
```python
# GRAND EXCHANGE PRICE EXAMPLE
>>> from osrs_net import GrandExchange as GE
>>> whip_id = GE.item_id_from_name('abyssal whip')
>>> whip_id
4151
>>> whip_price = GE.latest_price_by_id(whip_id)
>>> whip_price['high']
1932360
>>> whip_price_low = GE.latest_price_by_name('abyssal whip')['low']
>>> whip_price_low
1911689

# HISCORES STATS EXAMPLE
>>> from osrs_net import hiscores
>>> seute = hiscores.lookup_player('seute')
>>> seute.get_level('slayer')
99
>>> seute_slayer = seute.get_stat('slayer')
>>> seute_slayer.experience
13774066
>>> seute_slayer.rank
139575
>>> seute_slayer.level
99
```
