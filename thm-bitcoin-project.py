investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000


def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    usd_value = bitcoin_amount * bitcoin_value_usd
    return usd_value


def check_if(item):
    if item < 30000:
        print("Investment below $30,000! SELL!")
    else:
        print("Investment above $30,000")


inv = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
check_if(inv)
