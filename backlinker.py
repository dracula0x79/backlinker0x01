from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Chrome WebDriver with WebDriverManager
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # Important for WSL and Docker
options.add_argument('--disable-dev-shm-usage')  # Fixes potential shared memory issues
options.add_argument('--headless')  # Run in headless mode (without GUI)

# Disable logging to hide unnecessary output (DevTools, TensorFlow, etc.)
options.add_argument('--disable-logging')  # Disable logging
options.add_argument('--log-level=3')  # Set log level to 'ERROR' only, hide info and warnings
options.add_argument('--remote-debugging-port=0')  # Disable remote debugging

# Add the binary location for Google Chrome (update the path if necessary)
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Use WebDriverManager to install the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Continue with the rest of the script...

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

def print_usage():
    print("\n\nUsage Instructions:")
    print("1. Enter the name of the vulnerability you want to search for.")
    print("2. Enter the filename where you want to save the results (optional, default is 'results.txt').")
    print("3. The script will search and save the results to the file.\n")

def print_searching_banner():
    print("\n[SEARCHING...] Please wait while I gather the links...\n")
    print("===============================================================")
    print("|         Searching for links... Just a moment!               |")
    print("===============================================================")

def print_completed_banner(filename, result_count):
    print("\n===============================================================")
    print(f"| Process Completed! {result_count} results found and saved to {filename} |")
    print("===============================================================")

def print_goodbye_message():
    print("\nThanks for using the script! Goodbye!\n")

def search_vulnerability(vulnerability_name, filename):
    # Define your search URL with Google Dorking
    search_query = f"site:medium.com OR site:github.com OR site:hackerone.com OR site:bugcrowd.com OR site:exploit-db.com OR site:reddit.com/r/bugbounty OR site:securityfocus.com OR site:stackoverflow.com OR site:owasp.org {vulnerability_name} + writeup"
    url = f"https://www.google.com/search?q={search_query}"

    try:
        # Open the search URL
        driver.get(url)

        # Wait for search results to load more efficiently
        WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a/h3'))
        )

        # Find the search results
        links = driver.find_elements(By.XPATH, '//a/h3')

        if not links:
            print("No links found. Please check the XPath or Google search behavior.")
            return

        # Extract URLs and save them to the specified text file
        results = []
        with open(filename, 'w') as file:
            for index, link in enumerate(links):
                parent = link.find_element(By.XPATH, '..')  # Get the parent <a> tag
                result_url = parent.get_attribute('href')
                
                if result_url and result_url not in results:  # Ensure the URL is not empty or duplicate
                    results.append(result_url)
                    file.write(result_url + '\n')
                    print(f"Link {index + 1}: {result_url}")  # Print each link in real-time

        print_completed_banner(filename, len(results))

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    print_intro()  # Call the function to print the intro
    
    while True:
        # Get user input for vulnerability and filename
        vulnerability = input("Enter the name of the vulnerability: ").strip()
        
        # If the user inputs nothing, prompt again until they enter a valid value
        if not vulnerability:
            print("\nYou must enter a vulnerability name. Please try again.")
        else:
            # Ask user for the file name (if not entered, use 'results.txt')
            filename = input("Enter the filename to save the results (press Enter to use 'results.txt'): ").strip()
            if not filename:
                filename = 'results.txt'
            
            print_searching_banner()  # Show the banner for searching
            
            # Search and save results
            search_vulnerability(vulnerability, filename)
            break  # Exit the loop if everything goes well

    # Show the goodbye message at the end
    print_goodbye_message()
