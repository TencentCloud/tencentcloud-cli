**Example 1: 展示使用计划绑定详情**

用户在绑定了某个使用计划到环境后，可使用本接口查询这个使用计划绑定的所有服务的环境。

Input: 

```
tccli apigateway DescribeUsagePlanEnvironments --cli-unfold-argument  \
    --UsagePlanId usagePlan-quqxvett \
    --BindType API
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "EnvironmentList": [
                {
                    "ServiceId": "service-ody35h5e",
                    "ServiceName": null,
                    "ApiId": "api-e92i2jds",
                    "ApiName": "test2",
                    "Path": "/users",
                    "Method": "POST",
                    "Environment": "test",
                    "InUseRequestNum": 0,
                    "MaxRequestNum": -1,
                    "MaxRequestNumPreSec": 0,
                    "CreatedTime": "2019-12-23T09:15:17Z",
                    "ModifiedTime": null
                }
            ]
        },
        "RequestId": "6c405f2c-ae4b-4d83-a155-522c4d3c7d3c"
    }
}
```

