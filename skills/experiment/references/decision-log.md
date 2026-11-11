# Attempt log format

`docs/experiments/<topic>/decision.tsv`, tab-separated. The first line is exactly this header.

```
id	hypothesis	change	before	after	delta	tests	verdict	note
1	Adding fees hurts high-turnover strategies	cost=0.1%	1.42	1.10	-0.32	pass	reverted	Sharpe, 2020-2024 out of sample
```

- Use the same unit for before, after, and delta (the one in the metric definition).
- verdict is `kept` or `reverted`.
- Put noise size and evaluation window in note.
