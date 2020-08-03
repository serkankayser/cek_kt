from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
import time
import sys

# sys.path.insert(0, '/home/serkan/cek_kt/')                # SERVER
# sys.path.insert(0, '/Users/saiderdem/Desktop/cek_kt/')    # SAID
sys.path.insert(0, '/Users/serkankayser/Desktop/cekimkt/')  # SERKAN

from paths import username_field, pass_field, username, pw, master_islem_tipi, cekim_bt, islem_tipi
from paths import search_box, btc_sec, tum_kutucuklar, bosluk, search_bt, musteri_kodu, customer_search, arama_bt
from paths import islemler_bt, baslangic_tarihi, ara, islem, sayfa_nr, sayfa_50, tum_yatirim_yontemleri, durum_tipi, durum_tamamlandi
from paths import islem_type, hepsini_sec, search_box2, win_bet_box, win_bet_box2, bet, text_bosluk
from paths import password_path, kod_path, username_path, giris_kodu, giris_username, giris_password
from paths import casino_kod, casino_ara, casino_musteri, casino_degistir, casino_hh, casino_tarih, casino_bahis_ara, casino_har_tip, casino_playbet, casino_bosluk, casino_toplam_bahis, casino_kapat
from paths import istatistikler_bt, para_cekim, tutar, evet_bt, yetkili_notu, gecerli_bt, ga, casino_ga

# driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[0]) # LOGIN PANELI
# driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[1]) # CASINO PANELI
# driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[2]) # Muhasebe Yönetimi
# driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[3]) # DONTPAD
# driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[4]) # Yeni Müşteri Ara Paneli

all_customer_ids = []
islem_sutunu = []
tarih_sutunu = []
cr_page_number = 2
tum_cek_miktarlari = []

class vevo_panel():
    chrome_option = Options()
    # chrome_option.add_argument('--headless')    # SERVERDAYSAN #YI KALDIR
    chrome_option.add_argument('--no-sandbox')
    chrome_option.add_argument('--disable-dev-shm-usage')
    chrome_option.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(chrome_options=chrome_option)
    driver.get("https://dagur.pronetgaming.eu/login.xhtml")

driver_vevo = vevo_panel()

def check_exists_by_xpath(xpath):
    try:
        wait = WebDriverWait(driver_vevo.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    finally:
        return False
    return True

def login():
    username_bt = driver_vevo.driver.find_element_by_xpath(username_field)
    username_bt.click()
    username_bt.send_keys(username)
    pass_bt = driver_vevo.driver.find_element_by_xpath(pass_field)
    pass_bt.click()
    pass_bt.send_keys(pw)
    pass_bt.send_keys(Keys.ENTER)

    # GOOGLE AUTHENTIFICATION - BASLANGIC
    ga_box = driver_vevo.driver.find_element_by_xpath(ga)
    ga_box.click()
    entry_ga = input("PRONET GA KODU = ")
    ga_box.send_keys(entry_ga)
    ga_box.send_keys(Keys.ENTER)
    time.sleep(10)
    # GOOGLE AUTHENTIFICATION - BITIS

    driver_vevo.driver.execute_script("window.open('https://dagur.pronetgaming.eu/restricted/cust-money-dep-withdraw.xhtml')")
    time.sleep(3)
    login_casino()

def login_casino():
    driver_vevo.driver.execute_script("window.open('https://casinotrader-sl.pronetgaming.eu/login.xhtml')")  
    driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[1]) # CASINO PANELI
    kod = driver_vevo.driver.find_element_by_xpath(kod_path)
    kod.click()
    kod.send_keys(giris_kodu)    
    user = driver_vevo.driver.find_element_by_xpath(username_path)
    user.click()
    user.send_keys(giris_username)
    pass_bt = driver_vevo.driver.find_element_by_xpath(password_path)
    pass_bt.click()
    pass_bt.send_keys(giris_password)
    pass_bt.send_keys(Keys.ENTER) 

    # GOOGLE AUTHENTIFICATION CASINO - BASLANGIC
    ga_casino = driver_vevo.driver.find_element_by_xpath(casino_ga)
    ga_casino.click()
    ga_kodu = input("CASINO GA KODU = ")
    ga_casino.send_keys(ga_kodu)
    ga_casino.send_keys(Keys.ENTER)
    time.sleep(10)
    # GOOGLE AUTHENTIFICATION CASINO - BITIS
    driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[2]) # Muhasebe Yönetimi
    get_ready_panel()

def get_ready_panel():
    check_exists_by_xpath(master_islem_tipi)
    driver_vevo.driver.find_element_by_xpath(master_islem_tipi).click()
    driver_vevo.driver.find_element_by_xpath(cekim_bt).click()
    time.sleep(1)
    driver_vevo.driver.find_element_by_xpath(islem_tipi).click()
    time.sleep(1)
    driver_vevo.driver.find_element_by_xpath(tum_kutucuklar).click() # TUM KUTUCUKLARI SEC - ISLEM TIPINDE
    # BTC CEKIMI CIKAR - BASLANGIC
    search_b = driver_vevo.driver.find_element_by_xpath(search_box)
    search_b.click()
    time.sleep(1)
    search_b.send_keys('btc')
    driver_vevo.driver.find_element_by_xpath(btc_sec).click()
    time.sleep(1) # SIL
    # BTC CEKIMI CIKAR - BITIS
    driver_vevo.driver.find_element_by_xpath(bosluk).click()
    driver_vevo.driver.find_element_by_xpath(search_bt).click()
    driver_vevo.driver.execute_script("window.open('https://dagur.pronetgaming.eu/restricted/customer-details.xhtml?faces-redirect=true&customerId=6090455')") 
    time.sleep(2)
    driver_vevo.driver.execute_script("window.open('http://dontpad.com/kerim.cek.kt')")
    get_cust_id()

def get_id_again():
    driver_vevo.driver.find_element_by_xpath(search_bt).click()
    get_cust_id()

def get_cust_id():
    time.sleep(2)
    driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[2]) # Muhasebe Yönetimi
    a = driver_vevo.driver.find_elements_by_xpath(musteri_kodu)
    for customer_id in a:
        all_customer_ids.append(customer_id.text)
    
    b = driver_vevo.driver.find_elements_by_xpath(tutar)
    for tutarlar in b:
        yeni_tutar = tutarlar.text.split(',')
        filtred_tutar = int(yeni_tutar[0].replace('.', ''))
        tum_cek_miktarlari.append(filtred_tutar)
    if len(all_customer_ids) == 0:
        time.sleep(5) # YENI CEKIM GELMESINI BEKLE 5 SANIYE
        get_id_again()
    cp_paste_cust_id()

def cp_paste_cust_id():
    if len(tum_cek_miktarlari) == 0:
        get_id_again()
    print(all_customer_ids, tum_cek_miktarlari)
    if tum_cek_miktarlari[-1] >= 2000: # KAC TLYE KADAR KT EDILMESINI ISTIYORSAN BURDAN AYARLA (1999 TL ve altindaki miktarlar kt ediliyor)
        del tum_cek_miktarlari[-1]
        del all_customer_ids[-1]
        cp_paste_cust_id()
    if tum_cek_miktarlari[-1] <= 300: # 300 TL ALTI KONTROLSUZ ONAY
        time.sleep(8)
        cekim_onay()
    driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[4]) # Yeni Müşteri Ara Paneli
    time.sleep(1)
    customer_search_box = driver_vevo.driver.find_element_by_xpath(customer_search)
    customer_search_box.click()
    customer_search_box.send_keys(all_customer_ids[-1])
    driver_vevo.driver.find_element_by_xpath(arama_bt).click()
    time.sleep(4)
    get_ready_islemler()

def get_ready_islemler():
    driver_vevo.driver.find_element_by_xpath(islemler_bt).click() # ISLEMLER BUTONUNA TIKLA
    # TARIHI 1 AY GERIYE AL - BASLANGIC
    check_exists_by_xpath(baslangic_tarihi)
    bt = driver_vevo.driver.find_element_by_xpath(baslangic_tarihi)
    tarih = bt.get_attribute('value') # TARIH DEGERINI AL
    gun = tarih[0:2]
    ay = tarih[3:5]
    sene = tarih[6:10]
    yeni_ay = int(ay) - 1
    bt.clear()
    bt.send_keys(f'{gun}.{yeni_ay}.{sene} 23:59:59')
    # TARIHI 1 AY GERIYE AL - BITIS

    # DURUM TIPINI TAMAMLANMIS YAP - BASLANGIC
    driver_vevo.driver.find_element_by_xpath(durum_tipi).click()
    driver_vevo.driver.find_element_by_xpath(durum_tamamlandi).click()    
    # DURUM TIPINI TAMAMLANMIS YAP - BITIS

    # WIN_BETI SECME - BASLANGIC
    driver_vevo.driver.find_element_by_xpath(islem_type).click()
    driver_vevo.driver.find_element_by_xpath(hepsini_sec).click()
    win_yazdir = driver_vevo.driver.find_element_by_xpath(search_box2)
    win_yazdir.click()
    win_yazdir.send_keys('win')
    driver_vevo.driver.find_element_by_xpath(win_bet_box).click()
    driver_vevo.driver.find_element_by_xpath(win_bet_box2).click()
    time.sleep(1)
    # WIN_BETI SECME - BITIS
  
    driver_vevo.driver.find_element_by_xpath(ara).click() # ARAMA BUTONUNA TIKLA
    time.sleep(2)

    # SAYFA SAYISINI 50 YAP - BASLANGIC
    driver_vevo.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver_vevo.driver.find_element_by_xpath(sayfa_nr).click()
    time.sleep(1)
    driver_vevo.driver.find_element_by_xpath(sayfa_50).click()
    # SAYFA SAYISINI 50 YAP - BITIS
    get_wd_data() # SONRAKI FONKSIYONA GEC
    
    # MESAJ YAZDIR - BASLANGIC
def dontpade_yazdir(note):
    driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[3]) # DONTPAD SAYFASINA GEC
    bosluga_tikla = driver_vevo.driver.find_element_by_xpath(text_bosluk)
    bosluga_tikla.click()
    bosluga_tikla.send_keys(note)
    bosluga_tikla.send_keys(Keys.RETURN)
    # MESAJ YAZDIR - BITIS

def cekim_onay():
    time.sleep(2)
    driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[2]) # Muhasebe Yönetimi
    for cek in driver_vevo.driver.find_elements_by_xpath(musteri_kodu):
        if cek.text == all_customer_ids[-1]:
            cek.click()
            break
    time.sleep(6) # GECERLININ AKTIF OLMA SURESI
    # element = WebDriverWait(driver_vevo.driver, 20).until(EC.element_to_be_clickable((By.XPATH, gecerli_bt)))
    # element.click()
    driver_vevo.driver.find_element_by_xpath(gecerli_bt).click()
    time.sleep(1)
    yet_notu = driver_vevo.driver.find_element_by_xpath(yetkili_notu)
    yet_notu.send_keys('.')
    driver_vevo.driver.find_element_by_xpath(evet_bt).click() # GECERLIYE ATMAK ICIN # YI KALDIR.
    time.sleep(1)
    del all_customer_ids[-1] # LISTEDEKI SON MUSTERININ IDSINI SIL
    del tum_cek_miktarlari[-1] # LISTEDEKI SON MUSTERININ CEKIM MIKTARINI SIL
    islem_sutunu.clear()
    tarih_sutunu.clear()
    cr_page_number = 2
    if len(all_customer_ids) == 0:
        driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[2])
        time.sleep(1)
        driver_vevo.driver.find_element_by_xpath(search_bt).click()
        get_cust_id()
    else:
        cp_paste_cust_id()

def cekim_red():
    del all_customer_ids[-1] # LISTEDEKI SON MUSTERI IDSINI SIL
    del tum_cek_miktarlari[-1] # LISTEDEKI SON MUSTERININ CEKIM MIKTARINI SIL
    islem_sutunu.clear()
    tarih_sutunu.clear()
    cr_page_number = 2
    if len(all_customer_ids) == 0:
        driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[2])
        driver_vevo.driver.find_element_by_xpath(search_bt).click()
        get_cust_id()
    else:
        cp_paste_cust_id()

def get_wd_data():
    time.sleep(2)
    islem_sutunu = driver_vevo.driver.find_elements_by_xpath(islem)
    
    a = [] # GECICI LISTE ISLEM ICIN
    c = [] # GECICI LISTE MIKTAR ICIN
    for b in islem_sutunu:
        a.append(b.text)
        if 'Withdraw' in a[-1]:
            note = f'{all_customer_ids[-1]} : Son cekiminden once cekimi var. ONAY'
            cekim_onay()
        elif b.text in tum_yatirim_yontemleri:
            break
    islem_sutunu = a # ISLEM TIPLERI
    adet = len(islem_sutunu) + 1
    for i in range(1,adet):
        tarih = driver_vevo.driver.find_element_by_xpath(
            f'/html/body/div[4]/div/div[5]/div/form[2]/fieldset/div/div/div/div[1]/div[9]/div/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[5]')
        tarih_sutunu.append(tarih.text)        
        
        miktar_sutunu = driver_vevo.driver.find_element_by_xpath(
            f'/html/body/div[4]/div/div[5]/div/form[2]/fieldset/div/div/div/div[1]/div[9]/div/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[7]')
        miktar_filtre = miktar_sutunu.text[:-3]
        if len(miktar_filtre) > 4:
            miktar_filtre = miktar_filtre.replace('.', '')
        c.append(miktar_filtre)
    
    miktar_sutunu = c # MIKTARLAR
    cevrim_hesapla(miktar_sutunu, islem_sutunu, tarih_sutunu)

def istatistik():
    driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[4]) # Yeni Müşteri Ara Paneli
    driver_vevo.driver.execute_script("window.scrollTo(0, 0)")
    driver_vevo.driver.find_element_by_xpath(istatistikler_bt).click()
    time.sleep(3)
    check_exists_by_xpath(para_cekim)
    para_cekme_miktari = driver_vevo.driver.find_element_by_xpath(para_cekim).text

    if para_cekme_miktari == '0,00':
        return para_cekme_miktari

def casino_hesapla(deposit_miktari):
    driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[1]) # CASINO PANELI
    
    kod_yapistir = driver_vevo.driver.find_element_by_xpath(casino_kod)
    kod_yapistir.click()
    kod_yapistir.send_keys(all_customer_ids[-1])

    driver_vevo.driver.find_element_by_xpath(casino_ara).click()
    time.sleep(3)
    driver_vevo.driver.find_element_by_xpath(casino_musteri).click()
    time.sleep(1)
    driver_vevo.driver.find_element_by_xpath(casino_degistir).click()
    # time.sleep(3)
    element3 = WebDriverWait(driver_vevo.driver, 20).until(EC.element_to_be_clickable((By.XPATH, casino_hh)))
    element3.click()
    # driver_vevo.driver.find_element_by_xpath(casino_hh).click()
    # time.sleep(2)
    element3 = WebDriverWait(driver_vevo.driver, 20).until(EC.element_to_be_clickable((By.XPATH, casino_tarih)))
    element3.click()
    element3.clear()
    element3.send_keys(tarih_sutunu[-1])
    # cas_tarih = driver_vevo.driver.find_element_by_xpath(casino_tarih)
    # cas_tarih.click()
    # cas_tarih.clear()
    # cas_tarih.send_keys(tarih_sutunu[-1])
    driver_vevo.driver.find_element_by_xpath(casino_bosluk).click()
    time.sleep(1)
    driver_vevo.driver.find_element_by_xpath(casino_har_tip).click()
    time.sleep(1)
    driver_vevo.driver.find_element_by_xpath(casino_playbet).click()
    time.sleep(1)
    driver_vevo.driver.find_element_by_xpath(casino_bahis_ara).click()
    time.sleep(1)    

    bahis_miktari = driver_vevo.driver.find_element_by_xpath(casino_toplam_bahis).text
    filtered_bahis_miktari = bahis_miktari.split('.')
    
    deposit_miktari -= int(filtered_bahis_miktari[0].replace(',', ''))
    driver_vevo.driver.find_element_by_xpath(casino_kapat).click()
    time.sleep(1)
    kod_yapistir.clear()
    if deposit_miktari <= 0:
        a = istatistik()
        if a != None:
            note = f'{all_customer_ids[-1]} - Casino cevrimi onay -ILK CEKIM-'
            dontpade_yazdir(note)
            del all_customer_ids[-1] # LISTEDEKI SON MUSTERI IDSINI SIL
            del tum_cek_miktarlari[-1] # LISTEDEKI SON MUSTERININ CEKIM MIKTARINI SIL
            if len(all_customer_ids) == 0:
                driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[2])
                driver_vevo.driver.find_element_by_xpath(search_bt).click()
                get_cust_id()
            else:
                cp_paste_cust_id()
        else:
            note = f'{all_customer_ids[-1]} - Casino cevrimi onay'
            cekim_onay()
    else:
        note = f'{all_customer_ids[-1]} - Casino cevrimi red'
        a = istatistik()
        dontpade_yazdir(note)
        cekim_red()

def cevrim_hesapla(miktar_sutunu, islem_sutunu, tarih_sutunu):
    x = int(miktar_sutunu[-1])
    deposit_miktari = x * 7 / 10
    if islem_sutunu[-1] in tum_yatirim_yontemleri:
        for i in range(len(islem_sutunu)-1, 0, -1):
            if 'Bet' in islem_sutunu[i-1]:
                bet_id = driver_vevo.driver.find_element_by_xpath(
                    f'/html/body/div[4]/div/div[5]/div/form[2]/fieldset/div/div/div/div[1]/div[9]/div/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[6]')           
                bet_id.location_once_scrolled_into_view
                time.sleep(1)
                bet_id.click()
                time.sleep(1)
                del tarih_sutunu[-1]
                try:
                    bet_oranlari = driver_vevo.driver.find_elements_by_xpath(bet)
                except ElementClickInterceptedException:
                    time.sleep(1)

                for bet_orani in bet_oranlari:
                    a = float(bet_orani.text)
                    if a >= 1.30:
                        deposit_miktari -= int(miktar_sutunu[i-1])
                        webdriver.ActionChains(driver_vevo.driver).send_keys(Keys.ESCAPE).perform()
                        time.sleep(1)
                        break
                    else:
                        webdriver.ActionChains(driver_vevo.driver).send_keys(Keys.ESCAPE).perform()
                        time.sleep(1)
                        break

                if deposit_miktari <= 0:
                    a = istatistik()
                    if a != None:
                        note = f'{all_customer_ids[-1]} - Cevrim OK -ILK CEKIM-'
                        dontpade_yazdir(note)
                        del all_customer_ids[-1] # LISTEDEKI SON MUSTERININ IDSINI SIL
                        del tum_cek_miktarlari[-1] # LISTEDEKI SON MUSTERININ CEKIM MIKTARINI SIL
                        if len(all_customer_ids) == 0:
                            driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[2])
                            driver_vevo.driver.find_element_by_xpath(search_bt).click()
                            get_cust_id()
                        else:
                            cp_paste_cust_id()
                    else:
                        note = f'{all_customer_ids[-1]} - Cevrim OK'
                        cekim_onay()
                    break
                if i == 1:
                    note = f'{all_customer_ids[-1]} - Cevrim RED. Oynamasi gereken tutar: {deposit_miktari}'
                    dontpade_yazdir(note)
                    cekim_red()
                    break
            elif i == 1 and len(islem_sutunu) == 1:
                note = f'{all_customer_ids[-1]} - Cevrim RED. Oynamasi gereken tutar: {deposit_miktari}'
                dontpade_yazdir(note)        
                cekim_red()
                break

            elif islem_sutunu[i-1] == 'Transfer to Casino':
                del tarih_sutunu[-1]
                casino_hesapla(deposit_miktari)
                break

            elif islem_sutunu[i-1] == 'Transfer To Klas Poker':
                a = istatistik()
                if a != None:
                    note = f'{all_customer_ids[-1]} - Klas Poker -ILK CEKIM-'
                    dontpade_yazdir(note)
                    del all_customer_ids[-1] # LISTEDEKI SON MUSTERININ IDSINI SIL
                    del tum_cek_miktarlari[-1] # LISTEDEKI SON MUSTERININ CEKIM MIKTARINI SIL
                    if len(all_customer_ids) == 0:
                        driver_vevo.driver.switch_to_window(driver_vevo.driver.window_handles[2])
                        driver_vevo.driver.find_element_by_xpath(search_bt).click()
                        get_cust_id()
                    else:
                        cp_paste_cust_id()
                else:
                    note = f'{all_customer_ids[-1]} - Klas Poker'
                    cekim_onay()

    elif islem_sutunu[-1] not in tum_yatirim_yontemleri:
        global cr_page_number
        total_page_nr = driver_vevo.driver.find_elements_by_xpath(
            '/html/body/div[4]/div/div[5]/div/form[2]/fieldset/div/div/div/div[1]/div[9]/div/div/div/div[1]/div[2]/div/div[3]/span/a')

        for i in range(cr_page_number, len(total_page_nr)):
            driver_vevo.driver.find_element_by_xpath(
                f'/html/body/div[4]/div/div[5]/div/form[2]/fieldset/div/div/div/div[1]/div[9]/div/div/div/div[1]/div[2]/div/div[3]/span/a[{i}]').click()
            cr_page_number += 1
            break
        time.sleep(1)
        get_wd_data()

check_exists_by_xpath(username_field)
login()

# CEKIM SAYFASINI 50 YAP