from pycoingecko import CoinGeckoAPI
from nmwrap import NWaccount

addy = input("\ninput your Nimiq address here (leave blank for sample address): ") or "NQ538AAQ43Y6PBFD27DHTNCXFQRMY383EE7P"
#copy and paste this as sample address: NQ56H3BEFK0JXD5LMBGQ3CQR2S7E4J984BL6

nw = NWaccount(addy)
nw.account()
acct = nw.account()
balancefix = int(acct['balance']) / 100000
nimadd = acct['address']

cg = CoinGeckoAPI()
nim1 = cg.get_price(ids='nimiq-2', vs_currencies='usd,php')
nimusd = nim1['nimiq-2']['usd']
nimphp = nim1['nimiq-2']['php']
nimt = round(float(nimphp), 3)
nimtt = round(float(nimusd), 1)
peso = int(balancefix * round(nimt, 3))
usd = int(balancefix * nimusd)

print(nimusd)

print("\nYour wallet address is " + str(nimadd) + "\nYour balance is " + str(balancefix) + " NIM\n")

print("...equivalent to \n" + str(peso) + " PHP\n" + str(usd) + " USD\n")
