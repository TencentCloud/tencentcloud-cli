**Example 1: 请求示例**



Input: 

```
tccli sms DescribePhoneNumberInfo --cli-unfold-argument  \
    --PhoneNumberSet +8618511122266 +8618511122233
```

Output: 
```
{
    "Response": {
        "PhoneNumberInfoSet": [
            {
                "SubscriberNumber": "18511122266",
                "Message": "Describe success",
                "Code": "Ok",
                "PhoneNumber": "+8618511122266",
                "IsoCode": "CN",
                "IsoName": "China",
                "NationCode": "86"
            },
            {
                "SubscriberNumber": "18511122233",
                "Message": "Describe success",
                "Code": "Ok",
                "PhoneNumber": "+8618511122233",
                "IsoCode": "CN",
                "IsoName": "China",
                "NationCode": "86"
            }
        ],
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279"
    }
}
```

