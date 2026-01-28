# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Links
p_list = []
p1 = "https://www.hornbach.se/p/batteridriven-borrskruvdragare-dewalt-dcd791p2-18v-inkl-2x5-0ah-batterier-och-laddare-samt-tstak/6053746/"
p1_price = "/html/body/div[3]/div/main/div[2]/div[1]/section/section/div[2]/div/div/span[2]/span"
p2 = "https://www.bauhaus.se/skruvdragare-dewalt-dcd791p2-qw-18v-2x5-0ah"
p2_price = '//*[@id="product-price-357073"]'
p3 = "https://toolab.se/sv/products/dewalt-dcd791p2-borr-skruvdragare-18v-xr-kolborstfri-2x50ah"
p3_price = '//*[@id="product-price"]'
p4 = "https://www.verktygsproffsen.se/maskiner-elverktyg/elhandverktyg/skruvdragare/dewalt-dcd791p2-skruvdragare-med-2-st-50-ah-batterier-och-laddare-jt11814-2"
p4_price = '/html/body/div[2]/div/main/div/div[2]/div[2]/div/div[1]/div[4]/div/div[1]/span/span/span'
screw_drivers_list = [p1, p2]
screw_drivers_price_list = [p1_price, p2_price]


# Main function
def main():
    screw_list = screw_drivers(p_list)
    print(screw_list)


# Get browser
def screw_drivers(p_list):
    n = 0
    driver = webdriver.Chrome()
    driver.get(p1)
    price_1 = driver.find_element(By.XPATH, p1_price)
    print(price_1.text)
    p_list.append(f"Hornbach: {price_1.text.strip("*")}")
    driver.close()
    driver = webdriver.Chrome()
    driver.get(p2)
    price_2 = driver.find_element(By.XPATH, p2_price)
    print(price_2.text)
    p_list.append(f"Bauhaus: {price_2.text}")
    driver.close()
    driver = webdriver.Chrome()
    driver.get(p3)
    price_3 = driver.find_element(By.XPATH, p3_price)
    print(price_3.text)
    p_list.append(f"Toolab: {price_3.text}")
    driver.close()
    driver = webdriver.Chrome()
    driver.get(p4)
    price_4 = driver.find_element(By.XPATH, p4_price)
    print(price_4.text)
    p_list.append(f"Verktygsproffsen: {price_4.text}")
    driver.close()
    return p_list

# Execute main function
if __name__ == "__main__":
    main()
    
