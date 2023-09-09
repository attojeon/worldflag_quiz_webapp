import requests 
import bs4
import json

main_url = "https://flagpedia.net/index"
img_url_prefix = "https://flagpedia.net/data/flags/w580/"  # Albania "https://flagpedia.net/data/flags/w580/al.png"
filename = "flags.json"

def get_data():
    response = requests.get("https://flagpedia.net/index")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    flags = []

    # find class flag-grid  
    flag_list = soup.find(class_="flag-grid").find_all("li")
    for idx, flag_set in enumerate(flag_list):
        # <li> > <a href..> 태그를 가지고 있는 것만 검색한다.
        if flag_set.find("a"):
            # <span> text 가져오기
            country_name = flag_set.find("span").text
            # <img> 태그의 src 속성값에서 .webp를 .png로 변경하고, 파일이름만 가져온다.abs
            img_name = flag_set.find("img")["src"].replace(".webp", ".png").split("/")[-1]
            img_url = f"{img_url_prefix}{img_name}"
            print(f"{idx+1}: {country_name}, {img_url}")
            flag = {
                "country_name": country_name,
                "img_url": img_url
            }
            flags.append(flag)

    return flags

def save_to_data(flags):
    with open(filename, "w") as file:
        json.dump(flags, file, indent=4)

if __name__ == "__main__":
    flags = get_data()
    save_to_data(flags)
