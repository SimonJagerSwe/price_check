# Imports
from selenium import webdriver


# Links
p1 = "https://www.hornbach.se/p/batteridriven-borrskruvdragare-dewalt-dcd791p2-18v-inkl-2x5-0ah-batterier-och-laddare-samt-tstak/6053746/"

# Main function
def main():
    launch_browser()


# Get browser
def launch_browser():
    driver = webdriver.Firefox()
    driver.get(p1)
    # driver.implicitly_wait(10)
    # driver.close()

# Execute main function
if __name__ == "__main__":
    main()
    
