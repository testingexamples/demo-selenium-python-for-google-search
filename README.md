# Demo Selenium Python for Google Search

A friendly, step-by-step tutorial that demonstrates:

* [Selenium](https://www.selenium.dev/) browser automation testing
* [Python](https://www.python.org/) programming language
* [ChromeDriver](https://developer.chrome.com/docs/chromedriver) extends WebDriver by adding Chromium-specific capabilities
* Locator strategies and assertions for a Google Search results page

This demo is meant to be read top to bottom like a guide: open `src/demo.py`
alongside this README and follow along.

The exact scenario this demo teaches is specified in [spec/index.md](spec/index.md); the code and that spec must always agree.

## ⚠️ Google's Terms of Service — do not run this against live google.com

[Google's Terms of Service](https://www.google.com/policies/terms/)
restrict automated querying of Google Search. This code exists to teach
*patterns* — locator strategies and interaction techniques — not scripts
meant to be run against the live `google.com`.

**Non-negotiable:** never install this demo's dependencies in order to
execute it, never run `python3 src/demo.py`, and never point Selenium at a
real `google.com` results page from this repo. Read the code to learn the
patterns instead.

This is deliberately different from the sibling repo
`demo-selenium-python-for-nhs-wales`, which *is* meant to be installed and
run against its real, live target site. That target's terms permit it; the
live `google.com` does not.

## What this demo teaches

The script (never to be executed against the live site — see above) walks
through three checks a visitor's search might involve:

1. **Visit the Google Search home page** and check the page title is
   `Google`.
2. **Use the search box** — located by `By.NAME, 'q'`, since Google's exact
   markup for the search box has drifted over time (historically an
   `<input>`, currently often a `<textarea>`) but has commonly carried
   `name="q"` regardless — type `testing examples`, press Enter, and check
   the resulting page title contains the query.
3. **Click the first result** — located by `By.CSS_SELECTOR, '#search a'`
   — and check the browser navigated to a hostname other than
   `www.google.com`.

Each step prints what it found, then asserts it matches what we expect,
the same style used across this project family's assertion-based demos.

## Install

**Do not actually run these install steps in order to execute this demo
against live google.com** — see the caution above. They are documented here
so the code is correct and reproducible if you ever adapt this pattern to a
site whose terms permit automated querying.

### Install Python

Install Python from <https://www.python.org/>

Run this to confirm your version:

```sh
python3 --version
```

Output should be at least:

```stdout
Python 3.11.11
```

### Install Selenium

Install Selenium WebDriver:

```sh
pip install selenium
```

### Install chromedriver

Selenium needs a matching `chromedriver` binary on your `PATH` in order to
drive Google Chrome.

If you use macOS brew:

```sh
brew install chromedriver
```

Or download the version that matches your Chrome browser app from
<https://chromedriver.chromium.org/downloads> or, for newer Chrome versions,
<https://googlechromelabs.github.io/chrome-for-testing/>.

### Update

Run:

```sh
pip install --upgrade pip
pip install --upgrade selenium
```

## Run

**Do not run this.** `src/demo.py` is written to be correct and readable,
not to be executed against the live `google.com` — see the caution above.

If it were run, the script would:

1. Launch a local Chrome web browser and go to `https://www.google.com`.
2. Search for `testing examples` and click the first result.
3. Print a checklist of ✅ verifications as it confirms each expectation,
   then print "All checks passed. 🎉" when everything succeeds.

### Troubleshooting “chromedriver” Not Opened

If you get this kind of error message:

```txt
“chromedriver” Not Opened. Apple could not verify “chromedriver”
is free of malware that may harm your Mac or compromise your privacy.
```

Or this kind of error message:

```txt
Apple is not able to verify that it is free from malware that could harm your
Mac or compromise your privacy. Don’t open this unless you are certain it is
from a trustworthy source.
```

Then click "Done".

Try this command line solution:

```sh
xattr -d com.apple.quarantine $(which chromedriver) 2>/dev/null
```

Try adjusting your system settings:

* Apple menu -> Settings -> Security & Privacy -> General

* See the entry that says: "chromedriver" was blocked to protect your Mac.

* Click the button "Allow Anyway".

### Troubleshooting "This version of ChromeDriver …"

If you get this kind of error message:

```txt
SessionNotCreatedException: Message: session not created:
This version of ChromeDriver only supports Chrome version …
```

Then you may need to harmonize your Chrome browser app and your Chrome
webdriver.

If you use macOS brew, then upgrade chromedriver:

```sh
brew upgrade chromedriver
```

To update your Chrome browser app:

* On your computer, open Chrome.

* Find your current Chrome version by typing in the URL bar: `chrome://version/`.

* You should see a web page with many details, and you should see the first
  line with the version number, such as: "Google Chrome 135.0.7049.86
  (Official Build)".

* At top right, tap the "More" icon, which is 3 vertical dots.

* You see the "More" menu. If you see a menu item "Update", then choose it.
  If you don't see a menu item "Update", then you're on the current version.

To update your Chrome webdriver:

* Go to https://chromedriver.chromium.org/downloads

* Download the version that matches your Chrome browser app.

## Tracking

* Package: demo-selenium-python-for-google-search
* Version: 1.0.0
* Created: 2026-09-03T00:00:00Z
* Updated: 2026-09-03T00:00:00Z
* License: GPL-2.0-or-greater or for custom license contact us
* Contact: Joel Parker Henderson (joel@joelparkerhenderson.com)
