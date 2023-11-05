# Weather alert

## 1. Description
This function is to be used every morning to query data from
weatherbit.io to check for any weather alerts in my area.    
The function will be triggered every morning at 7am and it will send
an email to me providing a weather status update for the day.

## 2. Run
```shell
python lambda_function.py
```

## 3. Deployment
To trigger the email to be sent every morning, the following services
have been used:
* AWS Lambda - Trigger the code
* AWS SNS - Send email
* AWS S3 - Code Storage for Lambda function
* AWS EventBridge - Triggers the Lambda every morning