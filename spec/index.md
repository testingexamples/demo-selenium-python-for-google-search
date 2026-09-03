# Spec: Demo Selenium Python for Google Search

## Summary

This repo is a beginner-friendly walkthrough of Selenium WebDriver browser
automation in Python, teaching the locator strategies and assertions for a
Google Search results page. `src/demo.py` must never be executed against
the live `google.com` — see the caution below and in `README.md` /
`AGENTS.md`.

## Scope

This spec covers only the three checks implemented in `src/demo.py`. It
does not cover unrelated Google Search features, other browsers, or other
Google products.

## ⚠️ Non-negotiable: do not run this against live google.com

[Google's Terms of Service](https://www.google.com/policies/terms/)
restrict automated querying of Google Search. This code teaches syntax and
interaction *patterns*; it is not meant to be run repeatedly, or at all,
against the live `google.com`. Do not install dependencies to execute it,
do not run it, and do not point it at a real Google Search page.

## Principles and rules

* The demo uses the `selenium` package's Chrome driver directly (via
  `webdriver.Chrome(options=options)`), not a wrapper or test framework.
* Expected strings and selectors must be matched exactly as written below
  and in the source.
* If the code (`src/demo.py`) and this file ever disagree, that is a defect
  in one of them; fix it before doing anything else.

## Detail

1. **Home page title check**
   * Navigate to: `https://www.google.com`
   * Get the page title (`driver.title`).
   * Assert the title equals exactly: `Google`

2. **Search check**
   * Find the search box by `By.NAME, 'q'`.
     * Note: Google's exact markup for the search box has drifted between
       `<input>` and `<textarea>` over the years, but has commonly carried
       `name="q"` regardless, so `By.NAME` is the stable locator.
   * Send keys: `'testing examples' + Keys.RETURN`
   * Get the resulting page title (`driver.title`).
   * Assert the title contains the substring: `testing examples`

3. **First result check**
   * Find the first result link by `By.CSS_SELECTOR, '#search a'` and click
     it.
   * Get the resulting URL's hostname (via `urlparse(driver.current_url).hostname`).
   * Assert the hostname is not equal to: `www.google.com`

## Acceptance criteria

* All 3 checks above are correct Selenium/Python code that would pass if
  ever run against a live Google Search session — but they must not
  actually be executed against `google.com` as part of routine repo
  maintenance, CI, or agent work.

## Related topics

* [../README.md](../README.md)
* [../AGENTS.md](../AGENTS.md)

## Sources

* <https://testingexamples.github.io/examples/google-search/>
