**Example 1: 展示使用计划绑定的api列表**



Input: 

```
tccli apigateway DescribeApiUsagePlan --cli-unfold-argument  \
    --ServiceId service-ody35h5e
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "ApiUsagePlanList": [
                {
                    "ServiceId": "service-ody35h5e",
                    "ServiceName": null,
                    "ApiId": "api-e92i2jds",
                    "ApiName": "test2",
                    "Path": "/users",
                    "Method": "POST",
                    "UsagePlanId": "usagePlan-quqxvett",
                    "UsagePlanName": "aaa",
                    "UsagePlanDesc": "xby",
                    "Environment": "test",
                    "InUseRequestNum": 0,
                    "MaxRequestNum": -1,
                    "MaxRequestNumPreSec": null,
                    "CreatedTime": "2020-02-17T11:26:42Z",
                    "ModifiedTime": "2020-02-17T13:47:47Z"
                }
            ]
        },
        "RequestId": "8783bfc8-70e3-494a-97f4-0ccc10987aa8"
    }
}
```

