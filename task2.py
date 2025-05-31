import yfinance as yf
import pandas as pd
# Define your portfolio
portfolio = {
    'AAPL': {'shares': 10, 'buy_price': 150},
    'MSFT': {'shares': 5, 'buy_price': 280},
    'GOOGL': {'shares': 3, 'buy_price': 2500},
    'TSLA': {'shares': 4, 'buy_price': 650}
}

# Fetch current data and calculate metrics
rows = []
for ticker, data in portfolio.items():
    stock = yf.Ticker(ticker)
    current_price = stock.history(period='1d')['Close'].iloc[-1]
    
    shares = data['shares']
    buy_price = data['buy_price']
    market_value = shares * current_price
    cost_basis = shares * buy_price
    gain_loss = market_value - cost_basis
    return_pct = (gain_loss / cost_basis) * 100

    rows.append([
        ticker, shares, buy_price, round(current_price, 2),
        round(cost_basis, 2), round(market_value, 2),
        round(gain_loss, 2), round(return_pct, 2)
    ])

# Create a DataFrame
df = pd.DataFrame(rows, columns=[
    'Ticker', 'Shares', 'Buy Price', 'Current Price',
    'Cost Basis', 'Market Value', 'Gain/Loss', 'Return (%)'
])

# Display the result
print("\n📊 Portfolio Summary:\n")
print(df)
print("\nTotal Market Value: ${:,.2f}".format(df['Market Value'].sum()))
print("Total Gain/Loss: ${:,.2f}".format(df['Gain/Loss'].sum()))
