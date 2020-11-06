**Example 1: Querying APIs bound to policy**



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
        "TotalCount": 1,
        "ApiIdStatusSet": [
            {
                "ApiId": "api-e92i2jds",
                "ApiName": "test2",
                "ApiType": "NORMAL",
                "Path": "/users",
                "Method": "POST",
                "OtherIPStrategyId": "",
                "OtherEnvironmentName": ""
            }
        ],
        "RequestId": "cd0add5f-e7df-4087-8ccf-e07adca8e5a9"
    }
}
```

