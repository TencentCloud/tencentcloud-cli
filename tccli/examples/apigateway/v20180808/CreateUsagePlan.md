**Example 1: 创建使用计划**



Input: 

```
tccli apigateway CreateUsagePlan --cli-unfold-argument  \
    --UsagePlanName xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "UsagePlanId": "usagePlan-quqxvett",
            "UsagePlanName": "xx",
            "UsagePlanDesc": null,
            "MaxRequestNumPreSec": null,
            "MaxRequestNum": null,
            "CreatedTime": "2020-02-17T11:26:42Z",
            "ModifiedTime": "2020-02-17T11:26:42Z",
            "BindSecretIdTotalCount": 0,
            "BindSecretIds": null,
            "BindEnvironmentTotalCount": 0,
            "BindEnvironments": null
        },
        "RequestId": "b30900ef-72e9-4076-a2bd-dc8caab1ef6f"
    }
}
```

