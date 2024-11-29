# backlinker0x01                                                                                
This script gathers multiple write-ups about a specific vulnerability, offering insights into its discovery and exploitation. It helps enhance your understanding of penetration testing and security strategies through real-world examples and various exploitation techniques.

![image](https://github.com/user-attachments/assets/842a3479-5c13-4f5c-aa6d-56cfddafade1)

### Steps to Install the Tool on **Windows**

**Note**: This tool is designed to work on **Windows** systems. Please ensure you are using a Windows device before proceeding with the following steps.

### Prerequisites:
1. **Python 3.x**: You need Python 3 installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/downloads/).
2. **Google Chrome**: Ensure that Google Chrome is installed on your machine.
3. **ChromeDriver**: Selenium uses **ChromeDriver** to control Google Chrome, and the script will automatically download the appropriate version using `webdriver-manager`.
4. **Selenium** and **webdriver-manager**: These libraries will be installed via `pip`.

### Steps:

#### 1. Install Python:
- **Download Python**: If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
- **Verify Installation**:
    - Open **Command Prompt**.
    - Run the following command to check if Python is installed:
      ```bash
      python --version
      ```

#### 2. Install Dependencies:
- Open **Command Prompt** and install **Selenium** and **webdriver-manager** by running the following commands:

    ```bash
    pip install selenium webdriver-manager
    ```

    If you need to install any other libraries or if you want to update existing ones, you can use the `requirements.txt` file that includes all the necessary libraries for the script.

#### 3. Clone the Repository:
- Open **Command Prompt** and navigate to the directory where you want to clone the repository. Then run the following command:
  
    ```bash
    git clone https://github.com/dracula0x79/backlinker0x01.git
    ```

    If you don’t have **git** installed, you can download and install it from [git-scm.com](https://git-scm.com/).

#### 4. Navigate to the Project Directory:
After cloning the repository, navigate to the project folder:

```bash
cd backlinker0x01
```

#### 5. Run the Script:
Now, you are ready to run the script. Open **Command Prompt** inside the project directory and run:

```bash
python backlinker.py
```

#### 6. Script Execution:
- The script will prompt you for:
  1. The name of the vulnerability you want to search for.
  2. The filename to save the results (default is `results.txt`).
  
The script will then search for write-ups related to the vulnerability and save the links to the specified file.

### Troubleshooting:
- If you encounter the error: **"An error occurred: Message:"** it usually indicates a problem with the WebDriver or the Chrome installation. Ensure that **Google Chrome** is correctly installed and that **ChromeDriver** is compatible with the version of Chrome on your system.


## Example

Enter the name of the vulnerability: XSS
![image](https://github.com/user-attachments/assets/1f6b251c-508f-4311-a913-61e555ebc5b1)

Enter the filename to save the results: xss_writeups.txt
[SEARCHING...] Please wait while I gather the links...
Process Completed! 10 results found and saved to `xss_writeups.txt`
![image](https://github.com/user-attachments/assets/9eca4e1d-25e0-4cb4-8899-5aef1f277108)

In the `xss_writeups.txt` file, you will find links to write-ups about the vulnerability collected from various sources. You can open these links at any time and read them for more detailed information on the vulnerability and its exploitation.
![image](https://github.com/user-attachments/assets/ad2e1aeb-8c4b-4036-9c9b-71a8c261e98d)




