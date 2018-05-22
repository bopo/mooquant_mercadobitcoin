
import mooquant.logger
from mooquant import broker

btc_symbol = "btcbrl"
logger = mooquant.logger.getLogger("mercadobitcoin")


class BTCTraits(broker.InstrumentTraits):
    def roundQuantity(self, quantity):
        return round(quantity, 8)
