import yfinance as yf
import matplotlib as plt

# Intro
print("-------Welcome to Oliver's Stock Analysis Program!-------")

# Get stock ticker input from the user
ticker_symbol1 = input("What's the stock ticker?: ")
ticker_data = yf.download(ticker_symbol1, period="5y")  # Download stock data for a 5-year period

# Download TNX data
ticker_interest = yf.download("^TNX", period="5y")

# Gather Stock History
if input("Input 'h' for historical data: ").lower() == 'h':
    print("Here's five years of data!")
    print(ticker_data.info())

# Create a single figure with a single axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Stock Price Data
ax.plot(ticker_data.index, ticker_data['Close'], label='Stock Price', color='blue')
ax.set_ylabel('Price', color='blue')
ax.set_title(f"Stock Price and Federal Funds Interest Rates for {ticker_symbol1}")
ax.tick_params(axis='y', labelcolor='blue')

# Add Interest Rate Data as a second y-axis on the right side
ax2 = ax.twinx()
ax2.plot(ticker_interest.index, ticker_interest['Close'], label='Interest Rate', color='orange')
ax2.set_ylabel('Interest Rate', color='orange')

# Set common x-axis label
ax.set_xlabel('Date')

# Combine the legends from both axes
ax.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()