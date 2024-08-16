from playwright.sync_api import sync_playwright

def interact_with_webpage(auth_code):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto("https://certilogo.com")
            page.click("#root > div > a.cta-auth.big-cta.active")
            page.fill("#root > div > div.sc-kbousE.earfJZ > div > form > div > div.sc-tagGq.hGXwx.sc-wkolL.higNce > div.sc-ggpjZQ.eiqIGA > input", auth_code)
            page.click('text="Start"')
            page.click('text="Check Authenticity"')
            page.click('text="After purchase"')
            page.wait_for_load_state("networkidle")

            if page.is_visible("[id='6216181673f60c001f804ac2']", timeout=6000):
                print("Authentic!")
            else:
                print("Not Authentic!")

        finally:
            browser.close()

if __name__ == "__main__":
    auth_code = input("Please enter the authentication code: ")
    interact_with_webpage(auth_code)