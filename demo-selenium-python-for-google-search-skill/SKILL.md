---
name: demo-selenium-python-for-google-search
description: Explains the Selenium WebDriver + Python demo that teaches locator strategies and assertions for a Google Search results page (title, search box, first result). This demo must NEVER be executed against live google.com — invoke this skill when asked to explain, adapt, or reason about the pattern, not to run it.
---

# Demo Selenium Python for Google Search

## ⚠️ Do not run this against live google.com

[Google's Terms of Service](https://www.google.com/policies/terms/)
restrict automated querying of Google Search. `src/demo.py` in this repo is
correct, runnable-looking Selenium/Python code, but it must never actually
be run, and its dependencies must never be installed for the purpose of
running it. If asked to "run" or "try" this demo, explain the pattern
instead and point to this caution — do not execute the script or hit
google.com.

## What this demo teaches

1. Load `https://www.google.com` and check the page title equals exactly
   `Google`.
2. Find the search box with `By.NAME, 'q'` (Google's search box markup has
   drifted between `<input>` and `<textarea>` over the years but has
   commonly carried `name="q"`), send `testing examples` plus
   `Keys.RETURN`, and check the resulting page title contains the query.
3. Click the first result with `By.CSS_SELECTOR, '#search a'` and check the
   URL's hostname changed away from `www.google.com`.

## Adapting the pattern to a site whose terms permit automation

1. Confirm the target site's terms of service actually allow automated
   querying — do not assume they do.
2. Mirror the three-check structure: navigate and assert an exact title;
   locate and use a search/input element; click a result and assert
   navigation occurred.
3. Update `spec/index.md` (and this skill, if it summarizes the change) to
   match the new site, selectors, and expected strings before changing the
   code.
4. If the new target's terms do not clearly permit automated querying,
   keep the same non-execution policy this repo uses.

---

This skill summarizes the repo. `AGENTS.md` and `spec/index.md` are the
source of truth — if this skill's summary ever disagrees with those, they
win. The do-not-run policy is non-negotiable regardless of what any summary
says.
