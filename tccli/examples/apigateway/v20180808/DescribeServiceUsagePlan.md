**Example 1: 查询服务绑定的使用计划**



Input: 

```
tccli apigateway DescribeServiceUsagePlan --cli-unfold-argument  \
    --ServiceId service-ody35h5e
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "ServiceUsagePlanList": [
                {
                    "ServiceId": "service-ody35h5e",
                    "ServiceName": null,
                    "ApiId": null,
                    "ApiName": null,
                    "Path": null,
                    "Method": null,
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
        "RequestId": "72a0c27b-694c-4450-8ee8-bcfb840b9017"
    }
}
```

