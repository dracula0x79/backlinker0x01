# backlinker0x01                                                                                
This script gathers multiple write-ups about a specific vulnerability, offering insights into its discovery and exploitation. It helps enhance your understanding of penetration testing and security strategies through real-world examples and various exploitation techniques.

![image](https://github.com/user-attachments/assets/842a3479-5c13-4f5c-aa6d-56cfddafade1)


## Requirements

Before running the script, ensure that you have the following:

1. **Python 3.x** – The script is written in Python, so you need Python 3 installed.
2. **Selenium** – A web scraping library to interact with web pages.
   - Install with: 
     ```bash
     pip install selenium
     ```
3. **WebDriver Manager** – Used to automatically manage the ChromeDriver installation.
   - Install with:
     ```bash
     pip install webdriver-manager
     ```
4. **Google Chrome** – The script uses Chrome for web scraping. Ensure that Google Chrome is installed on your system. You may need to update the `options.binary_location` in the script to point to your Chrome installation path:
   - Default path for Windows: `C:\Program Files\Google\Chrome\Application\chrome.exe`
   - On Linux, the `binary_location` is usually not required if Chrome is installed via the package manager.
5. **ChromeDriver** – The WebDriver used by Selenium for automating Chrome. The script automatically installs the correct version using `webdriver-manager`.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dracula0x79/backlinker0x01.git
   cd backlinker0x01
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**
   ```bash
   python backlinker.py
   ```

4. The script will prompt you to:
   - Enter the name of the vulnerability you want to search for.
   - Enter the filename where you want to save the search results (optional, default is `results.txt`).

   The script will search for write-ups related to the specified vulnerability and save the gathered links in the chosen file.

## Features

- **Headless Mode**: The script runs in headless mode (no GUI) for faster operation, especially useful for environments like WSL or Docker.
- **Automated ChromeDriver Setup**: Uses `webdriver-manager` to automatically install and configure the ChromeDriver.
- **Customizable Output**: Save the results to a custom filename or use the default `results.txt`.

## Compatibility

- **Windows**: Fully compatible with Windows systems. Ensure Chrome is installed in the default location or update the path if needed.
- **Linux**: Fully compatible with Linux systems. Make sure Google Chrome is installed, and the `binary_location` variable may not need to be set.

## Example

Enter the name of the vulnerability: XSS
![image](https://github.com/user-attachments/assets/1f6b251c-508f-4311-a913-61e555ebc5b1)

Enter the filename to save the results: xss_writeups.txt
[SEARCHING...] Please wait while I gather the links...
Process Completed! 10 results found and saved to `xss_writeups.txt`
![image](https://github.com/user-attachments/assets/9eca4e1d-25e0-4cb4-8899-5aef1f277108)

In the `xss_writeups.txt` file, you will find links to write-ups about the vulnerability collected from various sources. You can open these links at any time and read them for more detailed information on the vulnerability and its exploitation.
![image](https://github.com/user-attachments/assets/ad2e1aeb-8c4b-4036-9c9b-71a8c261e98d)




