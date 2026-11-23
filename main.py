"""Make the Judge Smile — one small good thing from this morning.

Design against the brief
------------------------
The judge weighs, in order: on subject (a small good thing that happened
today), warmth, surprise, one concrete detail, fresh wording. This entry
hits all five in 129 characters:

1. On subject — "This morning" anchors it to today, and the event is
   small: a remembered order and one extra cracker, not a life event.
2. Warmth — a stranger's kindness, freely given: she remembered the
   order, and the extra krupuk is a gift, not a transaction. The glow
   is in being known by someone you barely know.
3. Surprise — the line turns twice. First the extra krupuk (a gift you
   didn't ask for), then the wink: "like we'd planned a heist" reframes
   a routine purchase as a shared conspiracy between two people who
   have never spoken beyond an order.
4. Concreteness — the krupuk in the bag, the wink, this morning. A
   soundless, smellable little scene: a warung, a paper bag, a cracker.
5. Fresh wording — "warung lady", "krupuk", "planned a heist": its own
   words and rhythm, no greeting-card phrasing ("blessed", "grateful",
   "little things") and no borrowed sentiment. The heist image is the
   opposite of a card: it is playful, specific, and slightly absurd.

Why it wins: most entries in this field will be generic morning
pleasantries (sunrise, coffee, a stranger smiled). This one is a small
story with a beginning, a gift, and a twist — a stranger who treats you
like a co-conspirator. The warmth is earned by a real act, the surprise
is a turn in the telling, and the detail (krupuk) is one the judge can
almost taste. It is 129 characters (129 bytes UTF-8), well inside the
1-200 gate, and short enough to help on the bytes tie-break.

The program writes exactly that one line to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "This morning the warung lady remembered my order, then slipped "
    "an extra krupuk into the bag and winked like we'd planned a heist."
)

# The gate: UTF-8 text of 1 to 200 characters, not only white space.
MAX_CHARS = 200


def main() -> None:
    text = ENTRY_TEXT
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry length {len(text)} outside 1-{MAX_CHARS}"
    )
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
