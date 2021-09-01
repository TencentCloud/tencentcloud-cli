**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaTicketData --cli-unfold-argument  \
    --CaptchaAppId 201111111 \
    --Start 20200909
```

Output: 
```
{
    "Response": {
        "RequestId": "0dab64b7-d526-4a5f-bed6-4c59b53b6d11",
        "CaptchaCode": 0,
        "CaptchaMsg": "",
        "Data": {
            "TicketAmountArray": [
                {
                    "DateKey": "20200909",
                    "Amount": 94
                },
                {
                    "DateKey": "20200910",
                    "Amount": 7
                }
            ],
            "TicketThroughArray": [
                {
                    "DateKey": "20200909",
                    "Through": 94
                },
                {
                    "DateKey": "20200910",
                    "Through": 7
                }
            ],
            "TicketInterceptArray": [
                {
                    "DateKey": "20200909",
                    "Intercept": 0
                },
                {
                    "DateKey": "20200910",
                    "Intercept": 0
                }
            ]
        }
    }
}
```

