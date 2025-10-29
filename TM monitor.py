import requests
import time

class monitor_price():
    def __init__(self):
        self.min = float("inf")
        self.is_new_min = False
        self.event_id = "00006192CB7039A7"
        self.proxy_index = 0
        self.url = f"https://offeradapter.ticketmaster.com/api/ismds/event/{self.event_id}/facets?apikey=b462oi7fic6pehcdkzony5bxhe&apisecret=pquzpfrfz7zd2ylvtz3w5dtyse&by=inventorytypes%20offer&q=available&show=listpricerange&embed=offer&resaleChannelId=internal.ecommerce.consumer.desktop.web.browser.ticketmaster.us"

        self.headers = {
        "sec-ch-ua-platform": '"macOS"',
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "tmps-correlation-id": "bd6ee49a-2ce4-4b19-b9d0-ca3e4f45be09",
        "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "accept": "*/*",
        "origin": "https://www.ticketmaster.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.ticketmaster.com/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "if-none-match": 'W/"0faa261a93dfecf2e4ab4615b2ace9ca4"',
        "if-modified-since": "Sat, 5 Jul 2025 20:33:01 GMT",
        "priority": "u=1, i"
        }

        
        self.cookies = {
            "_ga": "GA1.1.1016188882.1742221016",
            "OptanonGroups": ",C0001,C0003,C0002,C0004,",
            "LANGUAGE": "en-us",
            "BID": "45KOVxwaZ6wdxUJoSZ9Ip8mAjndEYz_-QXgtRCjZRBiJGmF_o0lQGi0tBjA-6qZ74iFE4rmpFD0KnIo",
            "ma.LANGUAGE": "en-us",
            "ma.BID": "7BPjwi9RdTZmgZJgmO8qlWofC8G-d_AI0IMNp61MREKitoGe_e65q1N7xCz6RgyaqkOq6wIvL9bIZIo",
            "_au_1d": "AU1D020000174904511328WT7MZPUL3T",
            "_ga_C5PKG9ERJ0": "GS2.1.s1749046331$o1$g0$t1749046331$j60$l0$h0",
            "_ga_DQETM4Z80E": "GS2.1.s1749046331$o1$g0$t1749046331$j60$l0$h0",
            "mt.v": "5.1313072534.1749046428419",
            "ndcd": "wc1.1.w-729460.1.2.gjhrKVZQkAPa2u07j-tJYg%252C%252C.6TnX6xegAz418teKNE50b0Tx-3D4ZsPhrFw5ZTaNYqGUsytPS9Pv0u3-6X-qBOjyfZtfuvJnGy6IFwMGYNEv_ij_wm-BcG5ZGdgNmZIN2b1J_yp9iIjmAUJulI92AILxV2CgvmlkBKXhugGh-je8EsyDCRxLU7lwy896Wl5V9sRrHwnFpbXeKxHhcJx5hVh-7kwcBLTz_UFNSYPMkga-6A%252C%252C",
            "_ga_2S5MRRZ1RP": "GS2.1.s1749050599$o1$g0$t1749050599$j60$l0$h0",
            "_gcl_au": "1.1.1322168816.1750016275",
            "SID": "RHufXkAh0Cjb1xyTANFa27Cb6dVnBIgnCXatCCYbxwOBgxvprNo0g2p5oZTSanDmFt-EeWPFrhXuKZIzzwaa",
            "ma.SID": "DJa1yvaMuuIYdhCsfxwDdP8gBHEekYY5SMAkyLqwYcCpNn5Ne7_AXj7lN6mXwEVjtDq7DmW2fgOHJ871lJ85",
            "NDMA": "200",
            "_ga_JB9YZH0QT9": "GS2.1.s1750201027$o1$g0$t1750201027$j60$l0$h0",
            "eps_sid": "35fbd48e7c79bce4c8bd8d85793df02632aa7225",
            "TMUO": "west_cpyvXu3f+wsavGUzpT5YVAlH/Urmt/6JjUCkNBqc5+U=",
            "AMCVS_2F2827E253DAF0E10A490D4E%40AdobeOrg": "1",
            "AMCV_2F2827E253DAF0E10A490D4E%40AdobeOrg": "179643557%7CMCIDTS%7C20275%7CMCMID%7C87254358076426338059180500873218343608%7CMCOPTOUT-1751754832s%7CNONE%7CvVersion%7C5.5.0",
            "_ga_4QRYKSS3Z3": "GS2.1.s1751747632$o2$g0$t1751747632$j60$l0$h0",
            "OptanonConsent": "isGpcEnabled=0&datestamp=Sat+Jul+05+2025+14%3A33%3A52+GMT-0600+(Mountain+Daylight+Time)&version=202408.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f87b2c5b-22d7-468f-87ae-0845929efe44&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false",
            "_ga_C1T806G4DF": "GS2.1.s1751744343$o12$g1$t1751748112$j60$l0$h0",
            "_ga_H1KKSGW33X": "GS2.1.s1751744343$o13$g1$t1751748112$j60$l0$h0",
            "tmpt": "0:5077555741000000:1751748115:4455a6f0:fb76dea3bccbe110a9b45706b0dd477c:5bdbaa5b109121c2f526d65841cd2ac859c73fb6baff79649f68648435e7c1e0"
        }
        

    def get_prices(self):
        response = requests.get(self.url, headers=self.headers, cookies=self.cookies)
        print(response.status_code)

        if response.status_code == 200:
            json = response.json()
            for facet in json['facets']:
                if float(facet['listPriceRange'][0]['min']) < self.min:
                    self.min = float(facet['listPriceRange'][0]['min'])
                    self.is_new_min = True
            
            if self.is_new_min:
                self.send_hook()

            print(f"min price: {self.min}")

        else:
            time.sleep(300)

    def send_hook(self):
        webhook_url = "https://discord.com/api/webhooks/1391184550893457530/9f7GdDLqdMs38EASALPUmK9UXqu9gvXxYthbC4ysIQgUdg8Z-msu809EqLrDLOkPDfm2"
        embed = {
        'title': f"https://www.ticketmaster.com/a/event/{self.event_id}",
        'description': f"New minimum price for your event: {self.min}",
        'url': f"https://www.ticketmaster.com/a/event/{self.event_id}",
        }
        data = {
        'embeds': [embed]
        }
        requests.post(webhook_url, json=data)

        if self.min < 130:
            ping_data = {
                "content": f"<@&{1127756848121004092}> price dropped below 130!",
                "allowed_mentions": {
                    "roles": [1127756848121004092]
                }
            }
            requests.post(webhook_url, json=ping_data)
            resp = requests.post(webhook_url, json=ping_data)
            print(resp.status_code, resp.text)

        self.is_new_min = False

    def run(self):
        while True:
                self.get_prices()
                print(time.time())
                time.sleep(60)

monitor = monitor_price()
monitor.run()