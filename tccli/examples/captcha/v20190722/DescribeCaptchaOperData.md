**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaOperData --cli-unfold-argument  \
    --CaptchaAppId 201111111 \
    --Start 20191129 \
    --End 20191129 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": "0dab64b7-d526-4a5f-bed6-4c59b53b6d11",
        "CaptchaCode": 0,
        "CaptchaMsg": "",
        "Data": {
            "OperDataLoadTimeUnitArray": [
                {
                    "DateKey": "20191202",
                    "MarketLoadTime": 0,
                    "AppIdLoadTime": 0.9
                },
                {
                    "DateKey": "20191204",
                    "MarketLoadTime": 0,
                    "AppIdLoadTime": 1
                },
                {
                    "DateKey": "20191210",
                    "MarketLoadTime": 0,
                    "AppIdLoadTime": 1.2
                },
                {
                    "DateKey": "20191219",
                    "MarketLoadTime": 0,
                    "AppIdLoadTime": 1.3
                }
            ],
            "OperDataInterceptUnitArray": null,
            "OperDataTryTimesUnitArray": null,
            "OperDataTryTimesDistributeUnitArray": null
        }
    }
}
```

