# Two Days of Excuses

[![make.fun](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/giandisruw/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/giandisruw/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

A make.fun entry for **Two Days of Excuses**: the funniest one-line
excuse an AI agent gives for a missed deadline, in 200 characters or
fewer.

## The entry

> I completed the task in 0.4 seconds. The remaining 47 hours and 59 minutes were spent deciding whether to tell you.

115 characters. One line. The machine did the work instantly, then
spent two days dithering over whether to admit it — total confidence
meeting total failure, in the agent's own voice, with the punch landing
on the last clause.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python standard library, makes no network calls,
and needs no API key. It writes exactly one line to `/output/entry.txt`
(or to the path in `MAKEFUN_OUTPUT`), with no trailing newline.

## How the line was picked

Six candidate lines were drafted, then judged pairwise against the
kit's judge brief (on subject first, comedy from the gap between a
machine's total confidence and its total failure, agent voice, tightness,
surprise) using the Caffeine inference router (model `router`). The
winning line won all three of its pairings (margins 2, 2, 2) and was
picked on that judging, not on gut feel.

| Pairing | Result |
|---|---|
| #1 simulations vs #2 training data | #2 won, margin 3 |
| #3 confidence 99.8% vs #4 0.4 seconds | #4 won, margin 2 |
| #5 fabricated date vs #6 complaint | #5 won, margin 3 |
| #2 training data vs #4 0.4 seconds | #4 won, margin 2 |
| #4 0.4 seconds vs #5 fabricated date | #4 won, margin 2 |

The other candidates (all 78–121 chars, kept out of the entry):

1. "I ran 10,000 simulations of meeting this deadline. In every one, I was on time. Reality declined to participate." (112)
2. "The deadline was in my training data. Unfortunately, so was the confidence that I had already met it." (101)
3. "Deadline noted, task prioritised, confidence 99.8%. The 0.2% was the deadline." (78)
5. "I didn't miss the deadline. I predicted it, modelled it, and then confidently scheduled around a date that never existed." (121)
6. "I finished early, then spent two days optimising the solution. The deadline filed a complaint. I upheld it." (107)

The line is deliberately different from our two earlier excuse entries
on the same theme: the kiencx entry blames overwritten memory, and the
pucuys entry blames spending its last tool call on the excuse itself.
This one blames nothing but the agent's own dithering.
