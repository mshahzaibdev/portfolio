from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        # 1. Index Page
        print("Navigating to index.html")
        page.goto("http://localhost:8080/index.html")
        time.sleep(1)
        page.screenshot(path="screenshot_index_leetcode.png", full_page=True)
        print("Screenshot saved: screenshot_index_leetcode.png")

        # 2. Project 3 Page (Bitcoin Trading)
        print("Navigating to project-3.html")
        page.goto("http://localhost:8080/project-3.html")
        time.sleep(1)
        page.screenshot(path="screenshot_project_3_leetcode.png", full_page=True)
        print("Screenshot saved: screenshot_project_3_leetcode.png")

        browser.close()

if __name__ == "__main__":
    run()
