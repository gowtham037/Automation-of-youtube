import logging
from appium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("🚀 Starting test...")
        
        # Chrome configuration
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = "/usr/bin/chromium-browser"

        # Set REQUIRED capabilities as options
        chrome_options.set_capability("platformName", "linux")
        chrome_options.set_capability("browserName", "chrome")
        chrome_options.set_capability("appium:automationName", "chromium")

        logger.info("🔌 Initializing WebDriver...")
        driver = webdriver.Remote(
            command_executor='http://localhost:4723',
            options=chrome_options  # Using ONLY options
        )

        logger.info("🌐 Navigating to YouTube...")
        driver.get("https://www.youtube.com")
        sleep(3)

        screenshot_path = "/tmp/youtube_success.png"
        driver.save_screenshot(screenshot_path)
        logger.info(f"📸 Screenshot saved to {screenshot_path}")

    except Exception as e:
        logger.error(f"❌ Test failed: {str(e)}")
        raise
    finally:
        if 'driver' in locals():
            driver.quit()
        logger.info("✅ Test completed")

if __name__ == "__main__":
    main()
