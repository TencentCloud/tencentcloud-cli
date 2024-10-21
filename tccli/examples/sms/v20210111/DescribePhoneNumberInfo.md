**Example 1: 请求示例**



Input: 

```
tccli sms DescribePhoneNumberInfo --cli-unfold-argument  \
    --PhoneNumberSet +8618501234444 +8618501234445
```

Output: 
```
{
    "Response": {
        "PhoneNumberInfoSet": [
            {
                "SubscriberNumber": "18501234444",
                "Message": "Describe success",
                "Code": "Ok",
                "PhoneNumber": "+8618501234444",
                "IsoCode": "CN",
                "IsoName": "China",
                "NationCode": "86"
            },
            {
                "SubscriberNumber": "18501234445",
                "Message": "Describe success",
                "Code": "Ok",
                "PhoneNumber": "+8618501234445",
                "IsoCode": "CN",
                "IsoName": "China",
                "NationCode": "86"
            }
        ],
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279"
    }
}
```

