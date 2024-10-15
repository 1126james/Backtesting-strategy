import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.test import GOOG

class tin(Strategy):
    initial_investment = 100000
    pieces = 5
    piece_value = initial_investment / pieces
    current_investment = piece_value
    profit_target = 1.5  # 50% profit target
    loss_threshold = 0.7  # -30% loss threshold

    def init(self):
        self.price = self.data.Close

    def next(self):
        current_price = self.price[-1]  # Use the latest price
        size = self.current_investment // current_price

        if not self.position:
            # Enter the market with the initial piece
            self.buy(size=size)
        
        else:
            # Check if the profit target is reached
            if self.position.pl >= self.current_investment * (self.profit_target - 1):
                self.position.close()
            
            # Check for the loss threshold
            elif self.position.pl <= -self.current_investment * (1 - self.loss_threshold):
                # Close all position if no more money
                if self.current_investment >= self.initial_investment:
                    self.position.close()
                # Add another piece if available
                elif self.current_investment < self.initial_investment:
                    self.current_investment += self.piece_value
                    size = self.piece_value // current_price
                    self.buy(size=size)

# Load data
data = GOOG  # Example data from the library

# Run the backtest
bt = Backtest(data, tin, cash=20000, commission=.002)
stats = bt.run()
bt.plot()