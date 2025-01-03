# backlinker0x01                                                                                
This script gathers multiple write-ups/reports about a specific vulnerability, offering insights into its discovery and exploitation. It helps enhance your understanding of penetration testing and security strategies through real-world examples and various exploitation techniques.

![image](https://github.com/user-attachments/assets/842a3479-5c13-4f5c-aa6d-56cfddafade1)

### Steps to Install the Tool on **Windows**

**Note**: This tool is designed to work on **Windows** systems. Please ensure you are using a Windows device before proceeding with the following steps.

---

### Prerequisites:

1. **Python 3.x**: You need Python 3 installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/downloads/).  
2. **Google Chrome**: Ensure that Google Chrome is installed on your machine.  
3. **ChromeDriver**: Selenium uses **ChromeDriver** to control Google Chrome. The script will automatically download the appropriate version using `webdriver-manager`.  
4. **Libraries**:  
   - **Selenium** and **webdriver-manager**: Required for web automation tasks.  
   - **fpdf**: Used for generating PDF files programmatically.  

   These libraries are listed in the `requirements.txt` file and can be installed in one step.

---

### Steps:

#### 1. Install Python:
- **Download Python**: If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).  
- **Verify Installation**:
    - Open **Command Prompt** or **Terminal**.
    - Run the following command to check if Python is installed:
      ```bash
      python --version
      ```

#### 2. Install Dependencies:
- Open **Command Prompt** or **Terminal**, navigate to the project directory, and install all required libraries using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

    This command will automatically install:
    - **Selenium**
    - **webdriver-manager**
    - **fpdf**

#### 3. Clone the Repository:
- Open **Command Prompt** or **Terminal** and navigate to the directory where you want to clone the repository. Then run the following command:
    ```bash
    git clone https://github.com/dracula0x79/backlinker0x01.git
    ```

    If you don’t have **Git** installed, download it from [git-scm.com](https://git-scm.com/).

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

⚠ Note: The tool might take some time to run initially because it needs to load the required libraries.

#### 6. Script Execution:
- The script will prompt you for:
  1. The name of the vulnerability you want to search for.
  2. The filename to save the results (default is `results.pdf`).
  
The script will then search for write-ups related to the vulnerability and save the links to the specified file.

### Troubleshooting:
- If you encounter the error: **"An error occurred: Message"** it usually indicates a problem with the WebDriver or the Chrome installation. Ensure that **Google Chrome** is correctly installed and that **ChromeDriver** is compatible with the version of Chrome on your system.


## Example

Enter the name of the vulnerability: xss
![image](https://github.com/user-attachments/assets/1f6b251c-508f-4311-a913-61e555ebc5b1)

Enter the filename to save the results: xss.pdf
[SEARCHING...] Please wait while I gather the links...
Process Completed! 10 results found and saved to `xss.pdf`
![image](https://github.com/user-attachments/assets/cc371f7e-4ffd-46e5-afda-0d2af97b22b6)

In the `xss.pdf` file, you will find links to write-ups about the vulnerability collected from various sources. You can open these links at any time and read them for more detailed information on the vulnerability and its exploitation.
![image](https://github.com/user-attachments/assets/e3ffe8a6-db50-4d8d-a94a-111cc0ecfef0)




