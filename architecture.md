# Architecture

```text
User
  |
  v
AI Agent / Agent OS
  |
  +--> Binance MCP: Spot prices
  |
  +--> Binance MCP: USDT-M Futures prices
  |
  v
Spread Analyzer
  |
  +--> rank discrepancies
  +--> explain direction
  |
  v
Human Confirmation Gate
  |
  +--> NO -> stop
  |
  +--> YES
        |
        v
   Binance MCP Trading
        |
        v
   Order Verification
```

The important design property is the confirmation gate: analysis can be automatic, but execution requires an explicit user approval.
