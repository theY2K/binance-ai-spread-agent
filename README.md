# Binance AI Spread Agent

An AI-powered Binance Agent OS workflow that scans Spot vs USDT-M Futures prices, ranks discrepancies, explains the largest spread, and requires explicit user confirmation before executing a trade through Binance MCP.

## Workflow

1. Scan BTC, ETH and SOL.
2. Read current Spot and USDT-M Futures prices through Binance MCP.
3. Calculate absolute gap and percentage gap:
   `gap = futures - spot`
   `gap_pct = (futures - spot) / spot * 100`
4. Rank opportunities by absolute percentage discrepancy.
5. Explain whether Futures are above or below Spot.
6. **STOP and request confirmation.**
7. Only after explicit confirmation, execute the configured trade through Binance MCP.
8. Verify the order status and report the result.

## Safety design

- No trade is placed during the scan.
- Explicit confirmation is required before execution.
- Use a dedicated Binance Agent OS sub-account with limited permissions/funding.
- Never place withdrawals or expose API secrets.

## Demo prompt

> Scan the market, identify the largest futures/spot discrepancy, explain the opportunity, and—only after my confirmation—execute the trade through Binance MCP.

## Example analysis

The agent may return:

- ETH: Spot $2,392.67 / Futures $2,391.21 / Gap -$1.46 / -0.0610%
- SOL: Spot $98.73 / Futures $98.67 / Gap -$0.06 / -0.0608%
- BTC: Spot $76,707.25 / Futures $76,670.00 / Gap -$37.25 / -0.0486%

Then it identifies ETH as the largest percentage discrepancy and pauses for confirmation.

> This project demonstrates an agentic workflow, not a guaranteed arbitrage strategy. Fees, funding, slippage, execution latency and market movement can eliminate a spread.
