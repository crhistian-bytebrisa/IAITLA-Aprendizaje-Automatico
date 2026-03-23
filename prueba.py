from alpaca.trading.client import TradingClient

client = TradingClient("PKGDJHPBXIO3QTVYDDZO4JRBQE","GvqQ44ocqYj1Kuivf4e9CiRek7s5E728x1vQtckZiTuz")

print(client.get_account().buying_power)
print(client.get_account().cash)
print(client.get_account().account_number)
