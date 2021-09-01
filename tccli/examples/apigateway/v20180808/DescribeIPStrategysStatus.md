**Example 1: DescribeIPStrategysStatus**



Input: 

```
tccli apigateway DescribeIPStrategysStatus --cli-unfold-argument  \
    --ServiceId service-ody35h5e
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "StrategySet": [
                {
                    "ServiceId": "service-ody35h5e",
                    "StrategyId": "IPStrategy-0ez0c8to",
                    "StrategyName": "xx",
                    "StrategyType": "WHITE",
                    "StrategyData": "2.2.2.2",
                    "CreatedTime": "2020-02-13T16:39:08Z",
                    "ModifiedTime": "2020-02-16T07:16:09Z",
                    "BindApiTotalCount": null,
                    "BindApis": null
                }
            ]
        },
        "RequestId": "cc167968-9ada-41b8-8724-62a497eedaad"
    }
}
```

