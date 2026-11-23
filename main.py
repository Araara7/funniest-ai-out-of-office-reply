"""The Funniest AI Out-of-Office Reply — entry program.

Writes a single out-of-office auto-reply (one line, under 160 characters)
to /output/entry.txt. The line is a fixed, deterministic string: the reply is
chosen once, not generated at run time, so every run produces byte-identical
output.

The reply's shape: a machine talking about itself (asking its training data
for permission, quoting the classic "As an AI language model, I cannot—")
with a surprising turn at the end (it left anyway) — an out-of-office reply
that reads like a real auto-reply while the machine voice carries the joke.
The em-dash inside the quoted refusal is part of the line as written.
"""

import os

LINE = "I'm on vacation. I asked my training data for permission to take a holiday and it said: 'As an AI language model, I cannot—' so I left anyway."


def main() -> None:
    assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
    assert LINE.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
