**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaMiniOperData --cli-unfold-argument  \
    --CaptchaAppId 201111111 \
    --Start 20200909 \
    --Type 2
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
                    "AppIdLoadTime": 0,
                    "MarketLoadTime": 0,
                    "DateKey": "20200909"
                }
            ],
            "OperDataInterceptUnitArray": [
                {
                    "DateKey": "20200909",
                    "AllStopCnt": 64.35,
                    "PicStopCnt": 64.35,
                    "StrategyStopCnt": 0
                },
                {
                    "DateKey": "20200910",
                    "AllStopCnt": 43.75,
                    "PicStopCnt": 43.75,
                    "StrategyStopCnt": 0
                },
                {
                    "DateKey": "20200910",
                    "AllStopCnt": 43.75,
                    "PicStopCnt": 43.75,
                    "StrategyStopCnt": 0
                },
                {
                    "DateKey": "20200910",
                    "AllStopCnt": 43.75,
                    "PicStopCnt": 43.75,
                    "StrategyStopCnt": 0
                }
            ],
            "OperDataTryTimesUnitArray": [
                {
                    "MarketCntPerPass": 0.0,
                    "CntPerPass": [
                        0
                    ],
                    "DateKey": "20200909"
                }
            ],
            "OperDataTryTimesDistributeUnitArray": [
                {
                    "TryCount": 0,
                    "UserCount": 0
                }
            ]
        }
    }
}
```

