import urllib.request
from bs4 import BeautifulSoup
import re


# endpoint
class Endpoint:
    def __init__(self, fqdn, protocol):
        self.__fqdn = fqdn
        self.__protocol = protocol

    def get_fqdn(self):
        return self.__fqdn

    def get_protocol(self):
        return self.__protocol

# http response data
class WebResponseData:
    def __init__(self, fqdn, protocol):
        self.__endpoint = Endpoint(fqdn, protocol)
        self.__response_data = None

    def get_endpoint(self):
        return self.__endpoint

    def get_response_data(self):
        return self.__response_data

    def set_response_data(self, path):
        url = self.__endpoint.get_protocol() + "://" + self.__endpoint.get_fqdn() + "/" + path
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as res:
                html_body = res.read().decode('utf-8')
                self.__response_data = html_body

        except Exception as e:
            print(e)

# Brand name obtained by scraping
class BrandName:
    def __init__(self, fqdn, protocol):
        self.__web_response_data = WebResponseData(fqdn, protocol)
        self.__brand_name = None

    def get_web_response_data(self):
        return self.__web_response_data

    def get_brand_name(self):
        return self.__brand_name

    def set_brand_name(self, path):
        self.__web_response_data.set_response_data(path)
        self.__brand_name = self.__scrape()

    def __scrape(self):
        b_list = []
        try:
            if self.__web_response_data.get_response_data() is not None:
                obj = BeautifulSoup(self.__web_response_data.get_response_data(), "html.parser")
                main_contents = obj.find("section", class_ = "container__mainContents")
                brands_wrapper = main_contents.find("section", class_ = re.compile("^Instruments__instrumentsWrapper"))
                brands = brands_wrapper.find("div", class_ = re.compile("^Instruments__forUpdate"))
                brands_tables_tbody = brands.find("table").find("tbody")
                for tr in brands_tables_tbody.find_all("tr"):
                    b_list.append(tr.find("button").string)

        except Exception as e:
            print(e)

        return b_list
