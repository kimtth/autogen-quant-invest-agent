
# Best time to buy/sell: Sell in May, buy in October.

## Overview

🤑Agent-based stock analysis and investment strategy application using 🎰AutoGen framework, focusing on MSFT stock.

- Review historical stock performance of Microsoft from the past 10-20 years.
- Identify patterns and trends.
- Autogen Agents for finding the best timing to invest.
  - [Documentation](https://microsoft.github.io/autogen/)
  - [Tutorial](https://microsoft.github.io/autogen/docs/Examples)
  - [Autogen studio](https://microsoft.github.io/autogen/docs/autogen-studio/getting-started) `cmd> autogenstudio ui --port 8081`
  - [Skills Repository](https://github.com/madtank/autogenstudio-skills)

## User Input and Results

- User Input

```bash
Run complete stock analysis for MSFT from 1995-01-01 to today. 
Generate buy/sell signals using 20 days Moving Average and 200 days Moving Average.
Based on the generated signals, backtest the strategy and provide performance metrics.
```

- Results

```bash
The stock analysis for MSFT from 1995-01-01 to 2024-09-09 has been completed. Here are the performance metrics from the backtest based on the generated buy/sell signals:

- **Cumulative Return:** 4049.51%
- **CAGR (Compound Annual Growth Rate):** 13.30%
- **MDD (Maximum Drawdown):** -70.96%
- **Sharpe Ratio:** 0.04

If you need any further analysis or insights, feel free to ask!

TERMINATE
```

## Configurations and Setup

  ```bash
  poetry install --no-root
  ```
- This application library supports [`ta`](https://github.com/bukosabino/ta), which provides commonly used indicators (pure Python).
- Another backtesting framework will be supported in the future.

## Python Libraries for Quant Trading 

- Zipline: Maintained and updated by the community after Quantopian shut down. [git](https://github.com/stefan-jansen/zipline-reloaded)
- backtrader: Python Backtesting library for trading strategies [git](https://github.com/mementum/backtrader)
- QuantStats: [git](https://github.com/ranaroussi/quantstats)
- TA-Lib Official Site: 200 indicators such as ADX, MACD, RSI, Stochastic, Bollinger Bands etc. Candlestick patterns. Faster (C-based). recognition. [git](https://ta-lib.org/)
  - TA-Lib python wrapper should be downloaded by manual.
  - unofficial TA-Lib wheels for Python on Windows: https://github.com/cgohlke/talib-build
```bash
$ python -m pip install TA_Lib-0.4.32-cp311-cp311-win_amd64.whl
```
- finta: Common financial technical indicators implemented in Pandas. archived repository. [git](https://github.com/peerchemist/finta)
- [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) uses GroupChat for multiple agents
  - GroupManager controls mutiple agents. It can be used to manage multiple agents in a group chat.

