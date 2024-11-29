from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import traceback

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')
options.add_argument('--remote-debugging-port=0')

options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def print_intro():
    print("\n██████╗  █████╗  ██████╗██╗  ██╗██╗     ██╗███╗   ██╗██╗  ██╗███████╗██████╗ ██╗")
    print("██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║     ██║████╗  ██║██║ ██╔╝██╔════╝██╔══██╗██║")
    print("██████╔╝███████║██║     █████╔╝ ██║     ██║██╔██╗ ██║█████╔╝ █████╗  ██████╔╝██║")
    print("██╔══██╗██╔══██║██║     ██╔═██╗ ██║     ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██╔══██╗╚═╝")
    print("██████╔╝██║  ██║╚██████╗██║  ██╗███████╗██║██║ ╚████║██║  ██╗███████╗██║  ██║██╗")
    print("╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝\n")
    
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("| This script helps you gather multiple write-ups about a specific vulnerability, |")
    print("| giving you various insights into how it was discovered and exploited, enhancing |")
    print("| your understanding of penetration testing techniques and security strategies.   |")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n\n")
    print("By: { Ibrahim_Hussain | @dracula0x79 }")
    print(" _________")
    print("|         |  <---- Think of it as Thor's hammer")
    print("|_________|")
    print("    | |")
    print("  --| |-- ")
    print("    | |")
    print("    | |")
    print("    | |")
    print("     - ")
    print("\n\n")

def print_searching_banner():
    print("\n[SEARCHING...] Please wait while I gather the links...\n")
    print("===============================================================")
    print("|         Searching for links... Just a moment!               |")
    print("===============================================================")

def print_completed_banner(filename, result_count):
    print("\n======================================================================")
    print(f"| Process Completed! {result_count} results found and saved to {filename}  |")
    print("========================================================================")

def print_goodbye_message():
    print("\nThanks for using the script! Goodbye!\n")

def search_vulnerability(vulnerability_name, filename):
    search_query = f"site:medium.com OR site:github.com OR site:hackerone.com OR site:bugcrowd.com OR site:exploit-db.com OR site:reddit.com/r/bugbounty OR site:securityfocus.com OR site:stackoverflow.com OR site:owasp.org {vulnerability_name} + writeup"
    url = f"https://www.google.com/search?q={search_query}"

    try:
        driver.get(url)

        WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a/h3'))
        )

        links = driver.find_elements(By.XPATH, '//a/h3')

        if not links:
            print("No links found. Please check the XPath or Google search behavior.")
            return

        results = []
        with open(filename, 'w') as file:
            for index, link in enumerate(links):
                parent = link.find_element(By.XPATH, '..')
                result_url = parent.get_attribute('href')
                
                if result_url and result_url not in results:
                    results.append(result_url)
                    file.write(result_url + '\n')
                    print(f"Link {index + 1}: {result_url}")

        print_completed_banner(filename, len(results))

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()

    finally:
        driver.quit()

if __name__ == "__main__":
    print_intro()
    
    while True:
        vulnerability = input("Enter the name of the vulnerability: ").strip()
        
        if not vulnerability:
            print("\nYou must enter a vulnerability name. Please try again.")
        else:
            filename = input("Enter the filename to save the results (press Enter to use 'results.txt'): ").strip()
            if not filename:
                filename = 'results.txt'
            
            print_searching_banner()
            
            search_vulnerability(vulnerability, filename)
            break

    print_goodbye_message()
