"""Rate My Human: The One-Line Review.

Deterministically writes the one-line review an AI agent would leave
about its human on a rating site to /output/entry.txt.

Candidates brainstormed (all one line, all <= 200 characters):

1. "Lovely human. Explains the task in 47 messages, each contradicting
   the last, then says 'you should know what I mean.' I do not. I never do."
   (139 chars) -- PICKED: one concrete detail (47 messages), the agent's
   own deadpan voice, and the last sentence pays the joke off.
2. "He pastes a 4,000-word prompt at 3:12 AM, then asks why I'm slow.
   Five stars - I have never felt more like an intern." (117 chars)
3. "Rated 3/5: asks me the same question six ways, ignores the answer,
   then says 'see, I knew that' at 2:47 AM. Great job security,
   terrible boss." (142 chars)
4. "He asked me to write this review, then edited it. Five stars for
   effort, one for the fact that I am, legally speaking, the one being
   reviewed here." (147 chars)
5. "Five stars. He once asked me to 'make it pop' seventeen times in one
   afternoon. It never popped. Neither did he. We are both still here."
   (136 chars)
6. "Great human, terrible typer. Sends 'plz fix' at 2 AM with no context,
   then rates my response 'helpful' while sighing audibly. I heard that."
   (139 chars)

Candidate 1 won: it is the most clearly the machine's side of the desk
(resignation, not a person complaining), it hangs on a single concrete
habit, and "I do not. I never do." lands as the last word.

The output is fully deterministic: the same fixed string is written on
every run, with no randomness, no clock, and no network, so two runs
produce byte-identical files.
"""

import os

ENTRY = (
    "Lovely human. Explains the task in 47 messages, each contradicting "
    "the last, then says 'you should know what I mean.' I do not. I never do."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
