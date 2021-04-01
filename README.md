![Nimiq Watch API Python wrapper](https://github.com/frvfrvr/frvfrvr/blob/master/wrapper1.png?raw=true)

# nimiq.watch-pythonwrapper

Python 3.x Wrapper for Nimiq Watch API

### Installation

```bash
git clone https://github.com/frvfrvr/nimiq.watch-pythonwrapper.git
cd nimiq.watch-pythonwrapper
pip3 install -r requirements.txt
python3 test.py
```
*test.py* script contains a sample Nimiq wallet address you can use when you run *test.py*

Leave the input dialog blank and see the sample address and balance.


You can also donate to this Nimiq address with this button:
[![Donate NIM](https://www.nimiq.com/accept-donations/img/donationBtnImg/light-blue-small.svg)](https://wallet.nimiq.com/nimiq:NQ56H3BEFK0JXD5LMBGQ3CQR2S7E4J984BL6)

### Usage

1. Change directory to wrapper's folder

```bash
cd nimiq.watch-pythonwrapper
```
2. Create a Python 3 script and import it with this:

```python
from nmwrap import NWaccount
nw = NWaccount('Nimiq wallet address')
```
