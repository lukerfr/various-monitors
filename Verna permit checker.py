import requests
import httpx
import time

class check_availability():
    def __init__(self):
        self.year = input("Please input desired permit(s) year\n")
        self.dates = []
        months = input("Please input the desired permit(s) month.\n" 
                       "If you want permits for multiple months, please input in format 5,6,7 etc...\n"
                       ).split(',')
        for month in months:
            dates = input(f"Please input the desired permit(s) date for month {month}."
                          "If you want permits for multiple dates, please input in format 8,9,10 etc...\n"
                          )
            for date in dates.split(','):
                self.dates.append([month, date])
        self.availability = {} 
        for month, day in self.dates:
            key = f"{month.zfill(2)}/{day.zfill(2)}"
            self.availability[key] = 0
        self.url = f"https://www.recreation.gov/api/permititinerary/4675320/division/4675320127/availability/month?month={months[0]}&year={self.year}"
        self.session = httpx.Client(
            http2 = True,
        )

    def report(self, message, url):
        webhook_url = "https://discord.com/api/webhooks/1359142626892447937/lo8AKuWHUJ92S15DHahy4PeTv1acF6c6XVQhpLWnWLB_Yfz6NW9E3bE_jJ5k4S7CBHtv"
        embed = {
        'title': 'Click here to reserve!',
        'description': message,
        'url': url,
        }
        data = {
        'embeds': [embed]
        }
        requests.post(webhook_url, json=data)

    def parse(self, response):
        json = response.json()
        data = json['payload']['quota_type_maps']['ConstantQuotaUsageDaily']
        for date in self.dates:
            month, day = date[0], date[1]
            if len(month) < 2:
                month = "0" + month
            if len(day) < 2:
                day = "0" + day
            try:
                availability = data[f'{self.year}-{month}-{day}']
            except KeyError:
                self.url = self.url = f"https://www.recreation.gov/api/permititinerary/4675320/division/4675320127/availability/month?month={month}&year={self.year}"
                print(self.url)
                response = self.session.get(self.url)
                json = response.json()
                data = json['payload']['4251917001']['quota_type_maps']['QuotaUsageByMemberDaily']
                availability = data[f'{self.year}-{month}-{day}']
                             
            print(availability)

            if self.availability[f"{month}/{day}"] != availability['remaining']:
                print("found change")
                url = f"https://www.recreation.gov/permits/4675320/registration/detailed-availability?date={self.year}-{month}-{day}"
                if self.availability[f"{month}/{day}"] < availability['remaining']:
                    message = f"Availability on {month}/{day} has increased to {availability['remaining']} spots!"
                else:
                    message = f"Availability on {month}/{day} has decreased to {availability['remaining']} spots!"

                self.report(message, url)
                self.availability[f"{month}/{day}"] = availability['remaining']

    def run(self):
        while True:
            response = self.session.get(self.url)
            self.parse(response)

            print(time.time())
            time.sleep(10)

checker = check_availability()
checker.run()
