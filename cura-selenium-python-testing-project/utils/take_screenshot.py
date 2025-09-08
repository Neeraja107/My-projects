import os
from datetime import datetime

class Screenshot:
    def take_screenshot(self,save_path="screenshots",filename_prefix = "screenshot"):
        os.makedirs(save_path, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename=f"{filename_prefix}_{timestamp}.png"
        file_path = os.path.join(save_path,filename)

        self.driver.save_screenshot(file_path)
        print(f"saacreenshot saved at: {file_path}")
        return file_path