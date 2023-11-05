import os
import requests
import boto3


# TODO: send_email

class WeatherAlert:

    def get_data(self, url, key, city, country):
        r = requests.get(url=url, params={
            "key": key,
            "country": country,
            "city": city
        })

        if r.status_code == 200:
            return r.json()
        else:
            r.raise_for_status()

    def check_for_alert(self, response_data):
        """
        If there is an alert it will return the title and severity. Otherwise it will not return anything
        """
        if len(response_data["alerts"]) > 0:
            title = self.get_title(response_data=response_data)
            severity = self.get_severity(response_data=response_data)
            return title, severity
        else:
            return None, None

    def get_title(self, response_data):
        """

        This function takes in the mock API response, and it returns the title for the region
        """
        title = response_data["alerts"][0]["title"]
        return title

    def get_severity(self, response_data):
        """

        This function takes in the mock API response, and it returns the severity for the region
        """
        return response_data["alerts"][0]["severity"]

    def send_email(self, title, severity):
        """
        Sends email via AWS SNS if alert is present
        """
        if title:
            client = boto3.client('sns', region_name="eu-west-2",
                                  aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
                                  aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"))
            response = client.publish(
                TopicArn="arn:aws:sns:eu-west-2:416241265996:weather_alert",
                Message=title,
                Subject=f"Weather Alert {severity}"
            )
        else:
            client = boto3.client('sns', region_name="eu-west-2",
                                  aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
                                  aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"))
            response = client.publish(
                TopicArn="arn:aws:sns:eu-west-2:416241265996:weather_alert",
                Message="Have a nice day",
                Subject="Clear sky's"
            )
            print(response)

def lambda_handler(event, context):
    weather_alert = WeatherAlert()
    api_data = weather_alert.get_data(
        url="https://api.weatherbit.io/v2.0/alerts",
        key=os.getenv("WEATHER_API_KEY"),
        city="Dundee",
        country="GB"
    )
    print(api_data)
    title, severity = weather_alert.check_for_alert(response_data=api_data)
    print(title, severity)

    weather_alert.send_email(title=title, severity=severity)

if __name__ == "__main__":

    weather_alert = WeatherAlert()

    api_data = weather_alert.get_data(
        url="https://api.weatherbit.io/v2.0/alerts",
        key=os.getenv("WEATHER_API_KEY"),
        city="Dundee",
        country="GB"
    )
    print(api_data)
    title, severity = weather_alert.check_for_alert(response_data=api_data)
    print(title, severity)

    weather_alert.send_email(title=title, severity=severity)