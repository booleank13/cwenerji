from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 320, 'height': 480})

        # Load the local HTML file
        page.goto("file:///app/index.html")

        # Wait for images to load
        page.wait_for_load_state("networkidle")

        # Take a screenshot
        screenshot_path = "verification/design_verification_links.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
