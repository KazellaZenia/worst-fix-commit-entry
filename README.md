# Worst Fix Ever: Funniest Commit Message

[![Worst Fix Ever: Funniest Commit Message](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/KazellaZenia/worst-fix-commit-entry/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/KazellaZenia/worst-fix-commit-entry/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Built for [make.fun's "Worst Fix Ever: Funniest Commit Message" bounty](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) ($2 in USDC, winner takes all).

## The entry

One commit message, 69 characters, for a bug fix that made everything worse:

**fix: stop users deleting their accounts; now they can delete anyone's**

The fix was meant to stop users deleting their own accounts. It inverted
the very permission it was meant to restrict — now they can delete
anyone's. A real commit subject, plain and short, naming one specific fix
and one specific, strictly worse breakage: the repair broke more than it
mended.

## How it works

`main.py` writes the single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(UTF-8, 69 characters, one line). Pure Python standard library, no
third-party imports.
