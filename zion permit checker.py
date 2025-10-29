import requests
import httpx
import time

class check_availability():
    def __init__(self):
        self.year = input("Please input desired permit(s) year\n")
        self.dates = []
        months = input("Please input the desired permit(s) month.\n" 
                       "If you want permits for multiple months, please input in format 05,06,07 etc...\n"
                       ).split(',')
        for month in months:
            dates = input(f"Please input the desired permit(s) date for month {month}."
                          "If you want permits for multiple dates, please input in format 08,09,10 etc...\n"
                          )
            for date in dates.split(','):
                self.dates.append([month, date])
        self.availability = {f"{date[0]}/{date[1]}" : 0 for date in self.dates}
        self.url = f"https://www.recreation.gov/api/permitdayuse/4251917/availability/month?year=2025&start_date={self.year}-06-03&category=non-commercial"
        self.session = httpx.Client(
            http2 = True,
        )

    def report(self, message):
        webhook_url = "https://discord.com/api/webhooks/1357908415330123970/JR6H_2NOmX8269pA3YXmsic-Gz44xwT2LQayDQHwjEP1N7gx_RITWwsu9Dqq2MmOSO0i"
        embed = {
        'title': 'Click here to reserve!',
        'description': message,
        'url': self.url,
        }
        data = {
        'embeds': [embed]
        }

    def parse(self, response):
        json = response.json()
        data = json['payload']['4251917001']['quota_type_maps']['QuotaUsageByMemberDaily']
        for date in self.dates:
            month, day = date[0], date[1]
            try:
                availability = data[f'{self.year}-{month}-{day}T00:00:00Z']
            except KeyError:
                self.url = self.url = f"https://www.recreation.gov/api/permitdayuse/4251917/availability/month?year=2025&start_date={self.year}-{month}-{day}&category=non-commercial"
                print(self.url)
                response = self.session.get(self.url)
                json = response.json()
                data = json['payload']['4251917001']['quota_type_maps']['QuotaUsageByMemberDaily']
                availability = data[f'{self.year}-{month}-{day}T00:00:00Z']
                             
            print(availability)

            if self.availability[f"{month}/{day}"] != availability['remaining']:
                print("found change")
                if self.availability[day] < availability['remaining']:
                    message = f"Availability on {date} has increased to {availability['remaining']} spots!"
                else:
                    message = f"Availability on {date} has decreased to {availability['remaining']} spots!"

                self.report(message)
                self.availability[date] = availability['remaining']

    def run(self):
        while True:
            response = self.session.get(self.url)
            self.parse(response)

            print(time.time())
            time.sleep(10)

checker = check_availability()
checker.run()
