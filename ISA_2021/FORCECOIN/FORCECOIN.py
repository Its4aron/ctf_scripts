import hashlib 
import string
def get_letters():
    helper = 'flag{L3m'
    ls = ['849d8f0974d2a081d83330f7183604df', '884cb3cd32cb2a6d5c645432a344fbbb', 'bce419f01d3e788dc8b21e8a2c7abfdc', '7ed269b23f5aa08ff9027a1b798a79ac', '9ff7c4366ad5bbe5b51bf6417cd1424a', '88ff232e07a2755f6a92af51b9bf9737', 'b88aff7d11354c59bec8cc7e45040169', '4bf148341e925de63f7069e321fd4cba', '1db8fd170c9d4580a125e1bfb98ea99e', 'c3c54e9d72f38482699cccc85ccabf37', '7d4e4ef06142ba28771d8d8d203a4570']
    for find in ls:
        for i in string.printable: 
            x = helper + i
            mded5 = hashlib.md5(x.encode())
            mded5 = mded5.hexdigest()
            if find == mded5:
               helper += i
    print(helper)
get_letters()

