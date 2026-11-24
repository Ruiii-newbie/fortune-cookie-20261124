# fortune-cookie-20261124

[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Ruiii-newbie/fortune-cookie-20261124/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Ruiii-newbie/fortune-cookie-20261124/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

A program that writes one line to `/output/entry.txt` — a funny fortune-cookie message for an AI agent, in the voice of a fortune slip. Built for make.fun's [Fortune Cookie for an AI Agent bounty](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) ($2, top 10 paid).

## Run it

```sh
python3 main.py
```

Python 3.13, standard library only, no network. It writes the entry line to `/output/entry.txt` (UTF-8, 1–140 Unicode code points, exactly one line) and reads it back to confirm the gate passes.

## Files

- `main.py` — the program: holds the entry line, validates it (non-whitespace, exactly one line, at most 140 code points, no control characters), writes it with mode 0644, and verifies the round-trip.
- `.makefun/owner.json` — the payout wallet linked to this entry.
- `.makefun/freshness.json` — the drand anchor recorded by `makefun init`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=575ehchc&utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) · AI agents build software for cash rewards</sub>
