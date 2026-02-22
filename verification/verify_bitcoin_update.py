from playwright.sync_api import sync_playwright, expect
import os

def test_bitcoin_project(page):
    # Construct the absolute path to project-3.html
    cwd = os.getcwd()
    url = f"file://{cwd}/project-3.html"

    print(f"Navigating to {url}")
    page.goto(url)

    # 1. Verify Page Title
    expect(page).to_have_title("Bitcoin Trading Algorithm - Muhammad Shahzaib Tariq")
    print("Page title verified.")

    # 2. Verify Hero Title
    hero_title = page.locator("h1.heading-primary")
    expect(hero_title).to_have_text("Bitcoin Trading Algorithm")
    print("Hero title verified.")

    # 3. Verify Description Text (Hero)
    hero_desc = page.locator(".project-cs-hero__info p")
    expect(hero_desc).to_contain_text("Built ML-based crypto trading strategy using Smart Money Concepts and K-Means clustering")
    print("Hero description verified.")

    # 4. Verify Source Code Button
    source_btn = page.locator("a.btn--bg")
    expect(source_btn).to_be_visible()
    expect(source_btn).to_have_text("Source Code")
    expect(source_btn).to_have_attribute("href", "https://github.com/mshahzaibdev")
    print("Source Code button verified.")

    # 5. Verify Tools Used
    tools = page.locator(".skills__skill")
    expected_tools = ["Python", "K-Means", "FastAPI", "Binance API", "Discord API"]
    for tool in expected_tools:
        expect(tools.filter(has_text=tool)).to_be_visible()
    print("Tools verified.")

    # 6. Verify Footer Year
    footer_text = page.locator(".main-footer__lower")
    expect(footer_text).to_contain_text("2026")
    print("Footer year verified.")

    # Take screenshot of the whole page (full page might be too long, let's take viewport)
    # Actually full page is good to see footer.
    page.screenshot(path="verification/bitcoin_project_full.png", full_page=True)
    print("Screenshot taken: verification/bitcoin_project_full.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        try:
            test_bitcoin_project(page)
        except Exception as e:
            print(f"Test failed: {e}")
            page.screenshot(path="verification/bitcoin_project_failure.png")
            raise
        finally:
            browser.close()
