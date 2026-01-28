# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By


# Links
p_list = []
p_names = ["Hornbach", "Bauhaus", "Toolab", "Verktygsproffsen"]
p1 = "https://www.hornbach.se/p/batteridriven-borrskruvdragare-dewalt-dcd791p2-18v-inkl-2x5-0ah-batterier-och-laddare-samt-tstak/6053746/"
p1_price = "/html/body/div[3]/div/main/div[2]/div[1]/section/section/div[2]/div/div/span[2]/span"
p2 = "https://www.bauhaus.se/skruvdragare-dewalt-dcd791p2-qw-18v-2x5-0ah"
p2_price = '//*[@id="product-price-357073"]'
p3 = "https://toolab.se/sv/products/dewalt-dcd791p2-borr-skruvdragare-18v-xr-kolborstfri-2x50ah"
p3_price = '//*[@id="product-price"]'
p4 = "https://www.verktygsproffsen.se/maskiner-elverktyg/elhandverktyg/skruvdragare/dewalt-dcd791p2-skruvdragare-med-2-st-50-ah-batterier-och-laddare-jt11814-2"
p4_price = '/html/body/div[2]/div/main/div/div[2]/div[2]/div/div[1]/div[4]/div/div[1]/span/span/span'
screw_drivers_dict = {
    p1 : p1_price,
    p2 : p2_price,
    p3 : p3_price,
    p4 : p4_price
}


# Main function
def main():
    prices = driver_dict(screw_drivers_dict, p_list, p_names)
    print(f"Skruvdragare:\n{prices}")


# Create list of places and prices with dictionary comprehension
def driver_dict(dict, p_list, p_names):  
    n = 0  
    for key, value in dict.items():
        driver = webdriver.Chrome()
        driver.get(key)
        price = driver.find_element(By.XPATH, value)
        p_list.append(f"{p_names[n]}: {price.text}")
        n += 1
    
    return p_list

# Execute main function
if __name__ == "__main__":
    main()
    
