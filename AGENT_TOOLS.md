# Binance MCP Tool Mapping

The agent uses Binance Agent OS/MCP for live exchange actions.

## Market data
- Spot: `spot.tickerPrice`
- USDT-M Futures: `futures_usds.symbolPriceTicker`

## Trading
The agent may use the appropriate Binance MCP order tool only **after explicit user confirmation**.

## Required execution rule

The agent must not place an order during the scan or recommendation phase.

Required sequence:

`scan -> analyze -> recommend -> confirm -> execute -> verify`

Never expose API keys, secrets, passwords, or seed phrases in the repository or demo.
