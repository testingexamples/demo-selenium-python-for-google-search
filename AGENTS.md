# AGENTS.md

This repo is a small, beginner-friendly walkthrough (`src/demo.py`) that
uses Selenium WebDriver in Python to teach the locator strategies and
assertions needed to check a Google Search results page: the home page
title, the search box, and the first result.

## ⚠️ Non-negotiable: never execute this against live google.com

[Google's Terms of Service](https://www.google.com/policies/terms/)
restrict automated querying of Google Search. This repo's code must always
be **correct and readable**, but it must **never be run**:

* Never run `python3 src/demo.py`.
* Never install this demo's dependencies (`selenium`, `chromedriver`) in
  order to execute it.
* Never point Selenium (from this repo or elsewhere) at a real
  `google.com` results page.
* Do not add CI, a test runner invocation, or any other automation that
  would execute `demo()` against the live site.

This is the opposite policy from the sibling repo
`demo-selenium-python-for-nhs-wales`, which *is* meant to be installed and
run against its real, live target site — that target's terms permit
automated testing; live `google.com` does not. Do not copy that sibling's
"go ahead and run it" framing into this repo.

## Source of truth

`spec/index.md` is the single source of truth for the exact three checks
and selectors this demo teaches. If `src/demo.py` and `spec/index.md` ever
disagree, that is a defect in one of them — fix it before doing anything
else.

## Install and run docs

`README.md` documents Install and Run steps for completeness and
correctness (so the code would work if a reader ever adapted it to a site
whose terms permit this), but its Run section is prescriptive about *not*
running it against google.com. Do not edit that caution out.

## Non-negotiable: don't change the scenario silently

Don't change the target site, the three checks, or the exact expected
strings/selectors (title, `By.NAME, 'q'`, the query text, `By.CSS_SELECTOR,
'#search a'`) without first updating `spec/index.md` to match.

---

CLAUDE.md is a pointer to this file — it is the single source of truth for
agent instructions.
