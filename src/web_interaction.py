from playwright.async_api import async_playwright

async def interact_with_webpage(auth_code):
   async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )

        page = await context.new_page()

        try:
            await page.goto("https://certilogo.com")
            await page.click("#root > div > a.cta-auth.big-cta.active")
            await page.fill("#root > div > div.sc-kbousE.earfJZ > div > form > div > div.sc-tagGq.hGXwx.sc-wkolL.higNce > div.sc-ggpjZQ.eiqIGA > input", auth_code)
            await page.click('text="Start"')
            await page.click('text="Check Authenticity"')
            await page.click('text="After purchase"')
            await page.wait_for_load_state("networkidle")

            if await page.is_visible("text='It\'s a gift'", timeout=3000):
                return "Congratulations! Your code authentic! =)"
            else:
                return "Your code not authentic! =("

        finally:
            await browser.close()
