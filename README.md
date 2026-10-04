# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every
> command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> All three tools are stubs, so that last command will do nothing useful yet.
> That's the starting position.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.
     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Three or four sentences: what a user asks for, and what they get back. -->

The user asks for suggestions on a new item based on their desired description, price range, and size. The program searches the available listings and selects the best matching item. It then uses the user's current wardrobe to suggest an outfit that includes the new item. Finally, it returns a short caption describing the outfit and its appeal.

---

## Tool Inventory

<!-- Four lines per tool. This is worth 2 points and it's the single most
     common place students lose them.

     "Returns a list" earns NOTHING. The description has to say what is IN
     the list.

     The empty case isn't optional either — it's the thing your loop branches
     on, and if you don't decide it here you'll discover it as a crash in
     Milestone 5. -->

### `search_listings`

- **What it does:** Searches the items in `listings.json` for listings matching the user's requested description, size, and maximum price.
- **Inputs:** `description` (string), `size` (string), `max_price` (float).
- **Returns:** A list of matching listing dictionaries containing fields such as `id`, `title`, `description`, `category`, `style_tags`, `size`, `condition`, `price`, `colors`, `brand`, and `platform`.
- **When it has nothing:** Returns an empty list `[]` when no listings match the search.

### `suggest_outfit`

- **What it does:** Uses the new listing item and the user's wardrobe to suggest an outfit combination.
- **Inputs:** `new_item` (dict), `wardrobe` (dict containing a list of item dictionaries).
- **Returns:** A string containing the `new_item` and selected compatible items from the user's wardrobe.
- **When it has nothing:** If the wardrobe contains no items, returns a string containing general outfit advice for styling the new item.

### `create_fit_card`

- **What it does:** Writes a short caption describing the appeal of an outfit after the addition of the new item.
- **Inputs:** `outfit` (string), `new_item` (dict).
- **Returns:** A string containing a short caption describing the outfit and how the new item complements it.
- **When it has nothing:** Returns a string with a message explaining that no outfit was provided.

---

## Planning Loop

<!-- Your branch rule, stated as a rule — the condition AND both paths — plus
     the file and function that holds it.

     Like this:
       "If search_listings returns an empty list, put a message in the session
        and stop. Otherwise take the first result and go to suggest_outfit."
        — agent.py::run_agent

     The grader checks your code against what you claim here, so the file and
     function have to be real. -->

**Branch rule:** If `search_listings` returns an empty list, put a message in the session and stop. Otherwise, take the first result and continue to `suggest_outfit`.

**Where it lives:** `agent.py::run_agent`

**How the query is parsed:** Using regex, the size and max_price are extracted from the user's query, and the remaining text is cleaned into the description.<!-- regex, string splitting, or asking the model — say which -->

**What moves through the session:** The parsed query is stored in parsed and passed to search_listings. Its results are stored in search_results, the best result becomes selected_item, the generated outfit is stored in outfit_suggestion, and the final caption is stored in fit_card.<!-- which fields, in what order -->

---

## Sample Run

<!-- Two things go here.

     1. One FULL query and its output, pasted as text.
     2. Your three per-tool terminal tests — the command and what it printed. -->

**One full query**

```
$ python agent.py

=== A query the data can match ===
found: Y2K Baby Tee — Butterfly Print — $18.0 on depop

outfit:
Top: Y2K Baby Tee — Butterfly Print (New Item)
Bottoms: Baggy straight-leg jeans, dark wash
Shoes: Chunky white sneakers
Outerwear: Vintage black denim jacket
Accessories: Black crossbody bag

Why it works:
This outfit plays with a classic Y2K silhouette by pairing the fitted, graphic baby tee with baggy straight-leg jeans for a balanced proportion. The chunky white sneakers tie into the playful, nostalgic aesthetic, while the vintage black denim jacket and black crossbody bag add a cool, effortless finish without distracting from the tee's butterfly print.

fit card:
Channeling major 2000s energy with this fitted butterfly baby tee paired with dark baggy denim and chunky sneakers. Topped off with a vintage black jacket, this fit is serving ultimate effortless off-duty vibes. Snag the Y2K Butterfly Baby Tee over on my Depop for just $18.00 before it’s gone!

```

**The three tools, tested one at a time**

```text
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"

[{'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.', 'category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_017', 'title': 'Mesh Long-Sleeve Top — Black', 'description': 'Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.', 'category': 'tops', 'style_tags': ['y2k', 'grunge', 'goth', 'layering'], 'size': 'S/M', 'condition': 'excellent', 'price': 15.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_011', 'title': 'Low-Rise Cargo Pants — Khaki', 'description': 'Y2K era low-rise cargo pants. Lots of pockets. Khaki color, slightly distressed at the hems. Great for layering with a long tee.', 'category': 'bottoms', 'style_tags': ['y2k', 'cargo', '2000s', 'streetwear'], 'size': 'W29', 'condition': 'fair', 'price': 27.0, 'colors': ['khaki', 'tan'], 'brand': None, 'platform': 'poshmark'}, {'id': 'lst_012', 'title': 'Oversized Crewneck Sweatshirt — Vintage Navy', 'description': 'Perfectly faded navy crewneck. Genuinely vintage — not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.', 'category': 'tops', 'style_tags': ['vintage', 'basics', 'oversized', 'classic'], 'size': 'XL (fits oversized)', 'condition': 'good', 'price': 20.0, 'colors': ['navy'], 'brand': None, 'platform': 'thredUp'}, {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie — Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'}]
```

```text
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"

**Outfit Suggestion:**

* **New Item:** Vintage Levi's 501 Jeans (Medium Wash)
* **Top:** White ribbed tank top
* **Outerwear:** Vintage black denim jacket
* **Shoes:** Chunky white sneakers
* **Accessories:** Black crossbody bag

**Why it works:**
The medium-wash vintage Levi's provide a classic, relaxed base that pairs effortlessly with the fitted white tank top for a timeless casual look. Layering the vintage black denim jacket adds a cool, cohesive texture that complements the retro vibe of the jeans, while the chunky white sneakers and black crossbody bag tie the streetwear elements of the outfit together.
```

```text
$ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"

Nothing beats the timeless combo of your favorite white sneakers and the ultimate off-duty uniform. These Vintage Levi's 501 Jeans in medium wash nail that effortless, perfectly broken-in 90s aesthetic. Grab them on depop for just $38.00 before I change my mind and keep them.
```

---

## How I Used AI

<!-- Two specific moments. What you asked, what came back, what you changed.

     "I used Claude to help me code" is not enough.

     "I gave Claude my search_listings spec. It returned None on no match
     instead of an empty list, so I changed it" is the level we want. -->

**Moment 1**

- *What I asked for:* I gave AI my rough algorithm for search_listings and asked it to help implement the function based on the requirements in tools.py.
- *What came back:* It produced code that loads the listings, filters by price and size, scores listings using keyword matches, sorts them by score, and returns the results.
- *What I changed:* I tested the function myself using both a matching query and a query designed to return nothing. I verified that matching searches returned listing dictionaries and that no matches returned [].

**Moment 2**

- *What I asked for:* I gave AI my planned flow for run_agent and asked for help implementing the planning loop and session state.
- *What came back:* It produced a loop that parses the query, calls search_listings, stores the selected item in the session, calls suggest_outfit, and then calls create_fit_card. It also included the branch that stops when the search returns an empty list.
- *What I changed:* I added and tested the iteration checks using trace.check_iterations(). I ran both example paths and verified that the successful path reached all three tools while the no-results path stopped after the search and left fit_card as None.

<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.

     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. Matching query completes | 4/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2. Impossible query stops early | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3. Selected listing passed to outfit tool | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4. Fit card stays consistent with item | 4/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 5. Maximum price respected | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |

**Real output from one try**, pasted as text, naming the file and function
that produced it:

```

**Criterion 1 — Matching query completes all three tools**  
Tested: `agent.py::run_agent`

```text
selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
search_results: 10

[1] search_listings (via MCP)
[2] suggest_outfit
[3] create_fit_card

Fit card:
Channeling major early 2000s energy with this effortless streetwear fit, pairing baggy dark wash denim with chunky kicks. The star of the look is this brand new Y2K butterfly baby tee, which is giving all the nostalgic vibes. Snag this cute new piece on Depop for just $18.00 before it’s gone!
```

**Criterion 2 — Impossible query stops early**  
Tested: `agent.py::run_agent`

```text
stopped early: yes — No matching listings were found. Try changing the description, size, or increasing the maximum price.
selected_item: (none)
search_results: 0

[1] search_listings (via MCP)
      out: [] (empty)
```

**Criterion 3 — Selected listing passed to outfit tool**  
Tested: `agent.py::run_agent`

```text
selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)

[1] search_listings (via MCP)
      out: 10 items: Y2K Baby Tee — Butterfly Print, ...

[2] suggest_outfit
      in: dict with keys: new_item, wardrobe

Outfit Suggestion:
Top: Y2K Baby Tee — Butterfly Print (New item)
```

**Criterion 4 — Fit card stays consistent with item**  
Tested: `tools.py::create_fit_card`

```text
selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)

Fit card:
Embracing full early-2000s streetwear energy with this baggy denim and cropped hoodie combo. The star of the fit is this new Y2K butterfly print baby tee, which brings total retro nostalgia. Grab it on my depop now for just $18.00 before it’s gone!
```

**Criterion 5 — Maximum price respected**  
Tested: `tools.py::search_listings`

```text
Query: vintage graphic tee under $20
selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
search_results: 8
```
```

---

## Verdicts and Diagnoses

<!-- MET or MISSED per criterion against LAST UNIT's target, plus a sentence on
     how you decided.

     Then, for every miss: which of the four places it happened — a tool, the
     loop's branch, the session, or the model's output — AND the mechanism.

     Not a diagnosis:  "The fit card was bad."
     A diagnosis:      "The fit card criterion missed on 2 of 5 items. Both had
                        an empty brand field. My prompt puts the brand in the
                        first sentence, so the card opened with a blank and read
                        like a fragment. The tool worked; the prompt assumed a
                        field that isn't always there."

     Look for a pattern. Three misses on the same tool is one problem, not
     three. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**



---

## Loop Trace

```text
[1] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Y2K Baby Tee — Butterfly Print, Graphic Tee — 2003 Tour Bootleg Style, Vintage Band Tee — Faded Grey … +7 more
[2] suggest_outfit
      in:  dict with keys: new_item, wardrobe
      out: **Outfit Suggestion:**  * **Top:** Y2K Baby Tee — Butterfly Print (New Item) * **Bottoms:** Baggy straight-leg…
[3] create_fit_card
      in:  dict with keys: outfit, new_item
      out: Channeling major 2000s energy with this fitted butterfly baby tee paired with dark baggy denim and chunky snea…
```
<!-- One full run, printed step by step, with the MCP call visible in it.

     `python app.py ask '...' --trace` once you've added the trace.step()
     calls in Milestone 2.

     Worth pasting BOTH the happy path and the empty-search path. The empty
     one should be visibly shorter, because it stops. If your two traces are
     the same length, your branch isn't working — and this is the fastest way
     anyone will ever find that out. -->

**Happy path**

```

```

**Empty search**

```

```

**On the MCP move:** <!-- what changed in your code, and whether anything
behaved differently afterwards. If the rewire didn't work, say exactly where it
broke — the error text and the last thing that worked. That earns the point in
full. -->



---

## The Improvement

<!-- What you changed, why your diagnosis pointed at it, and the after-run in
     the same table format. One change, measured properly.

     `python run_eval.py --label after` -->

**What I changed:**

**Which failure it was meant to fix:**

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |  |  |
| 2.  |  |  |  |  |  |  |  |
| 3.  |  |  |  |  |  |  |  |
| 4.  |  |  |  |  |  |  |  |
| 5.  |  |  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it made things worse, say that. Honestly reported, that earns full
     credit and is more interesting than one that worked. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped where
     you did. "I ran out of time" is fine if it's true. Pretending nothing is
     left is not. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
