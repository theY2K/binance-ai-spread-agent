"""Core market-spread analysis logic.

Binance Agent OS/MCP supplies the live prices. This module deliberately
contains no order-placement code: execution belongs behind the explicit
human-confirmation gate in the agent workflow.
"""

from dataclasses import dataclass


@dataclass
class Spread:
    symbol: str
    spot: float
    futures: float

    @property
    def gap(self) -> float:
        return self.futures - self.spot

    @property
    def gap_pct(self) -> float:
        return (self.gap / self.spot) * 100

    @property
    def direction(self) -> str:
        if self.gap > 0:
            return "above Spot"
        if self.gap < 0:
            return "below Spot"
        return "equal to Spot"


def rank_spreads(prices: list[tuple[str, float, float]]) -> list[Spread]:
    """Return spreads ranked by absolute percentage discrepancy."""
    spreads = [Spread(symbol, spot, futures) for symbol, spot, futures in prices]
    return sorted(spreads, key=lambda x: abs(x.gap_pct), reverse=True)


def format_report(spreads: list[Spread]) -> str:
    lines = ["Asset | Spot | Futures | Gap | Gap % | Direction"]
    lines.append("---|---:|---:|---:|---:|---")
    for s in spreads:
        lines.append(
            f"{s.symbol} | ${s.spot:,.2f} | ${s.futures:,.2f} | "
            f"${s.gap:,.2f} | {s.gap_pct:+.4f}% | Futures {s.direction}"
        )
    if spreads:
        best = spreads[0]
        lines.append("")
        lines.append(
            f"Best opportunity: {best.symbol} at {best.gap_pct:+.4f}%. "
            f"Futures are {best.direction}."
        )
    return "\n".join(lines)


if __name__ == "__main__":
    # Example/test data only. Live values should come from Binance MCP.
    sample = [
        ("BTC", 76707.25, 76670.00),
        ("ETH", 2392.67, 2391.21),
        ("SOL", 98.73, 98.67),
    ]
    print(format_report(rank_spreads(sample)))
