import os
from datetime import datetime


def capture_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = os.path.join(
        "screenshots",
        f"{name}_{timestamp}.png"
    )

    driver.save_screenshot(path)

    return path