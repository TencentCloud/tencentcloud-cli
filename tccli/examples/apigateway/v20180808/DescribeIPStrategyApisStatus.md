**Example 1: 查询策略绑定api**



Input: 

```
tccli apigateway DescribeIPStrategyApisStatus --cli-unfold-argument  \
    --StrategyId IPStrategy-0ez0c8to \
    --EnvironmentName test \
    --ServiceId service-ody35h5e
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "ApiIdStatusSet": [
                {
                    "OtherEnvironmentName": "xx",
                    "ApiId": "xx",
                    "ApiType": "xx",
                    "ApiName": "xx",
                    "OtherIPStrategyId": "xx",
                    "Path": "xx",
                    "Method": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

