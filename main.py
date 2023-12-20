import sys
import requests

def print_meanings():
    headers = {
        "User-Agent": "",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-GPC": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }

    response = requests.get(url, params=params, headers=headers)

    data = response.json()

    # Anlamları çıkart ve yazdır
    if isinstance(data, list) and data:
        first_element = data[0]
        if "anlamlarListe" in first_element:
            meanings = first_element["anlamlarListe"]
            for meaning in meanings:
                if "anlam" in meaning:
                    ozellikler = meaning.get("ozelliklerListe", [])
                    if ozellikler:
                        first_ozellik = ozellikler[0]
                        tam_adi = first_ozellik.get("tam_adi", "")
                        print("\n" + "-" * 50)
                        print("Meaning:", tam_adi)
                    print("-" * 50)
                    print(meaning["anlam"])
    else:
        print("No meanings found.")

url = "https://sozluk.gov.tr/gts"

if len(sys.argv) >= 2:
    search_word = sys.argv[1]
    params = {"ara": search_word}
    print_meanings()
    sys.exit(1)
else:
    while True:
        search_word = input("\nworld? ")
        params = {"ara": search_word}
        print_meanings()
