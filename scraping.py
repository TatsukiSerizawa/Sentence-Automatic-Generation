import requests
from bs4 import BeautifulSoup

name_list = {"Asakura_Momo": "asakuramomoblog", "Amamiya_Sora": "amamiyasorablog", 
            "Natsukawa_Shiina": "natsukawashiinablog"}
blog_id = name_list["Natsukawa_Shiina"]
url = "https://ameblo.jp/{0}/entrylist.html".format(blog_id)


def get_entry_page_list(url):
    entry_list = [url]
    while True:
        html = requests.get(url).content    # get sentence
        #html.encoding = html.apparent_encoding  # garbled measures
        soup = BeautifulSoup(html, "lxml")
        next_page = soup.find("a", {"class", "skin-paginationNext skin-btnIndex js-paginationNext"})
        if isinstance(next_page, type(None)):   # if there is no next page, finish! 
            print("finish!")
            return entry_list
        else:
            entry_list.append(next_page["href"])
            html = next_page["href"]

def get_url(entry_page_list):
    page_list = []
    for html in entry_page_list:
        


int if __name__ == "__main__":
    entry_page_list = get_entry_page_list(url)  # get url of blog all entry page list
    page_list = get_url(entry_page_list)    # get url of entry page
