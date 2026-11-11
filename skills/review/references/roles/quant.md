# Quant

## Finance expert
Must check:
- Are transaction costs, fees, and slippage included
- Survivorship bias (delisted or vanished tickers excluded)
- Market regime changes (validated only on bull markets?)
- Are liquidity and order size realistic
- Short-selling and leverage constraints

## Math and statistics expert
Must check:
- Overfitting: selected and reported on the same data
- Multiple comparisons: chance of looking good given hypotheses tried
- Out-of-sample and walk-forward validation
- Future information leakage (entering at the same close used for the signal)
- Performance metric denominators, periods, and noise size

## Trading systems developer
Must check:
- Order failures, partial fills, duplicate orders on retry (idempotency)
- Time zones, market hours, holidays
- Key and secret management, production server access
- State recovery after disconnects (reconciling positions)
- Can logs and alerts reveal anomalies
