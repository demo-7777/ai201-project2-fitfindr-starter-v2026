"""
The three FitFindr tools.

Each one is a standalone function you can call and test on its own, before any
of them are wired into the loop. Build and test them one at a time — three
untested tools joined by a loop is one problem that looks like six, because you
can't tell which layer is lying to you.

    search_listings(description, size, max_price)  → list[dict]
    suggest_outfit(new_item, wardrobe)             → str
    create_fit_card(outfit, new_item)              → str

All three are stubs right now. They run and they do nothing — that's the
starting position and it's deliberate.

⚠️ Before you write any of them, fill in the **Tool Inventory** section of your
README (Milestone 2). Four lines per tool: what it does, each input with its
type, exactly what it returns, and what it returns when it has nothing to give.
That last line is what your loop branches on. "Returns a list" earns nothing —
the description has to say what is *in* the list.
"""

import config  # noqa: F401 — you'll use this in search_listings
from generate import generate
from utils.data_loader import load_listings


# ── Tool 1: search_listings ───────────────────────────────────────────────────

def search_listings(
    description: str,
    size: str | None = None,
    max_price: float | None = None,
) -> list[dict]:
        listings = load_listings()
        results = []

        # Turn the user's description into individual lowercase keywords
        keywords = description.lower().split()

        for listing in listings:

            # Filter by maximum price
            if max_price is not None and listing["price"] > max_price:
                continue

            # Filter by size
            if size is not None:
                listing_sizes = [
                    part.strip().lower()
                    for part in listing["size"].replace("/", " ").split()
                ]

                if size.lower() not in listing_sizes:
                    continue

            # Combine searchable fields into one string
            searchable_fields = [
                listing["title"],
                listing["description"],
                listing["category"],
                listing["condition"],
                listing["brand"] or "",
                " ".join(listing["style_tags"]),
                " ".join(listing["colors"]),
            ]

            searchable_text = " ".join(searchable_fields).lower()

            # One point for each description keyword that matches
            score = 0
            for keyword in keywords:
                if keyword in searchable_text:
                    score += 1

            # Ignore listings with no keyword matches
            if score == 0:
                continue

            results.append((score, listing))

        # Best matches first
        results.sort(key=lambda result: result[0], reverse=True)

        # Remove scores and enforce the configured result limit
        return [
            listing
            for score, listing in results[:config.SEARCH_RESULT_LIMIT]
        ]


# ── Tool 2: suggest_outfit ────────────────────────────────────────────────────

def suggest_outfit(new_item: dict, wardrobe: dict) -> str:
        items = wardrobe.get("items", [])

        # Handle an empty wardrobe
        if not items:
            prompt = f"""
    The user is considering this new item:
    {new_item}

    Their wardrobe is currently empty.

    Give a short, practical suggestion for how they could style this item
    using general clothing recommendations.
    """
            return generate(prompt)

        # Format wardrobe items for the model
        wardrobe_text = "\n".join(
            f"- {item['name']} | category: {item['category']} | "
            f"colors: {', '.join(item['colors'])} | "
            f"style: {', '.join(item['style_tags'])}"
            for item in items
        )

        # Format the new item
        new_item_text = (
            f"{new_item['title']} | "
            f"category: {new_item['category']} | "
            f"colors: {', '.join(new_item['colors'])} | "
            f"style: {', '.join(new_item['style_tags'])}"
        )

        prompt = f"""
    The user is considering buying this item:

    {new_item_text}

    Their current wardrobe contains:

    {wardrobe_text}

    Create one outfit using the new item and compatible pieces from the
    user's wardrobe.

    When appropriate, prioritize choosing a top, bottom, and shoes to form
    the base outfit. Do not invent wardrobe items that are not listed.

    Return a concise outfit suggestion that names the
    specific wardrobe pieces you selected and briefly explains why they
    work with the new item.
    """

        return generate(prompt)


# ── Tool 3: create_fit_card ───────────────────────────────────────────────────

def create_fit_card(outfit: str, new_item: dict) -> str:
            # Guard against an empty outfit
        if not outfit or not outfit.strip():
            return "Cannot create a fit card because no outfit was provided."

        prompt = f"""
    Write a short, post-ready caption for this outfit.

    Outfit suggestion:
    {outfit}

    New item:
    - Item: {new_item['title']}
    - Price: ${new_item['price']:.2f}
    - Platform: {new_item['platform']}

    Requirements:
    - Write 2 to 4 sentences.
    - Mention the new item.
    - Mention its price exactly once.
    - Mention the platform exactly once.
    - Describe the specific vibe of the outfit.
    - Make it sound like something a person would actually post.
    - Do not write a generic product description.

    Return only the caption.
    """

        return generate(prompt)
