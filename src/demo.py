#!/usr/bin/env python3

"""
Demo of Selenium WebDriver browser automation with Python, teaching the
locator strategies and interaction patterns for a Google Search results
page.

IMPORTANT — DO NOT RUN THIS AGAINST LIVE google.com:
Google's Terms of Service restrict automated querying of Google Search.
This code exists to teach syntax and interaction *patterns* — it is not
meant to be executed against the live google.com. Do not run this script,
do not install its dependencies in order to run it, and do not point it at
a real Google Search results page. See README.md and AGENTS.md for the
full caution.

Please see the file README.md for more information.

## Tracking

  * Package: demo-selenium-python-for-google-search
  * Version: 1.0.0
  * Created: 2026-09-03T00:00:00Z
  * Updated: 2026-09-03T00:00:00Z
  * License: GPL-2.0-or-greater or for custom license contact us
  * Contact: Joel Parker Henderson (joel@joelparkerhenderson.com)
"""

import sys
from urllib.parse import urlparse

# Import Selenium WebDriver parts.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import chromedriver options that you can set as you wish.
from selenium.webdriver.chrome.options import Options


def demo() -> None:
    """Teach the locator strategies and assertions for a Google Search
    walkthrough. Do not call this against the live google.com — see the
    module docstring and README.md."""

    options = Options()
    options.add_argument('--verbose')  # Enable verbose logging.
    options.add_argument('--disable-notifications')  # Disable notifications such as popups.
    options.add_experimental_option(
        "prefs",
        {"profile.default_content_setting_values.cookies": 2},  # Reject cookies.
    )

    # Initialize the driver. Choose other browsers as you wish.
    driver = webdriver.Chrome(options=options)

    try:

        ###
        # Step 1: Load the Google Search home page, then verify the page
        # title is what we expect.
        ###

        driver.get('https://www.google.com')

        title = driver.title
        print(f'Page title: "{title}"')
        assert title == 'Google', \
            f'Expected page title to be "Google", got "{title}"'
        print('✅ Page title is correct.')

        ###
        # Step 2: Use the search box, then verify the results page title
        # contains our query.
        #
        # Note on markup drift: Google's exact markup for the search box
        # has drifted over time, and will likely keep drifting. It has
        # historically been an <input> and is currently often a
        # <textarea> — but both have commonly carried name="q", so we
        # locate it by name rather than by tag or type.
        ###

        query = 'testing examples'
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(query + Keys.RETURN)

        result_title = driver.title
        print(f'Result page title: "{result_title}"')
        assert query in result_title, \
            f'Expected result page title to contain "{query}", got "{result_title}"'
        print('✅ Result page title contains the search query.')

        ###
        # Step 3: Click the first result, then verify we navigated away
        # from www.google.com to some other hostname.
        ###

        driver.find_element(By.CSS_SELECTOR, '#search a').click()

        hostname = urlparse(driver.current_url).hostname
        print(f'Result hostname: "{hostname}"')
        assert hostname != 'www.google.com', \
            f'Expected hostname to change away from www.google.com, got "{hostname}"'
        print('✅ Navigated away from www.google.com.')

        print('\nAll checks passed. 🎉')

    finally:
        driver.quit()


def main() -> None:
    """Main entry point with error handling.

    NON-NEGOTIABLE: never call demo() against the live google.com. See the
    module docstring, README.md, and AGENTS.md."""
    try:
        demo()
    except Exception as err:
        print(f'Fatal error: {err}', file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
