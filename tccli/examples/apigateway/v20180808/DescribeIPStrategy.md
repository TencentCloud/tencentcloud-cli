**Example 1: DescribeIPStrategy**



Input: 

```
tccli apigateway DescribeIPStrategy --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --EnvironmentName test \
    --StrategyId IPStrategy-0ez0c8to
```

Output: 
```
{
    "Response": {
        "Result": {
            "ServiceId": "service-ody35h5e",
            "StrategyId": "IPStrategy-0ez0c8to",
            "StrategyName": "xx",
            "StrategyType": "WHITE",
            "StrategyData": "2.2.2.2",
            "CreatedTime": "2020-02-13T16:39:08Z",
            "ModifiedTime": "2020-02-16T07:16:09Z",
            "BindApiTotalCount": 0,
            "BindApis": []
        },
        "RequestId": "7723481f-45f0-48c1-8b64-03cfaa822116"
    }
}
```

