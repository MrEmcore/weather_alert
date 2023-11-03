from second import mock_weather_response


class WeatherAlert:

    def __init__(self, response_data):
        self.response_data = response_data

    def get_title(self):
        """

        This function takes in the mock API response, and it returns the title for the region
        """
        title = self.response_data["alerts"][0]["title"]
        return title

    def get_severity(self):
        """

        This function takes in the mock API response, and it returns the severity for the region
        """
        return self.response_data["alerts"][0]["severity"]


if __name__ == "__main__":

    # Initilize the class
    weather_alert = WeatherAlert(response_data=mock_weather_response)
    print(weather_alert.response_data)

    title = weather_alert.get_title()
    severity = weather_alert.get_severity()

    print(title)
    print(severity)