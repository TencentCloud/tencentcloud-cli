**Example 1: 创建使用计划**

用户在使用 API 网关时，需要创建使用计划并将其绑定到服务的环境中使用。

Input: 

```
tccli apigateway CreateUsagePlan --cli-unfold-argument  \
    --UsagePlanName auto_CreateAndUpdateUsageplan_Test_yu2hLs4d
```

Output: 
```
{
    "Response": {
        "Result": {
            "UsagePlanId": "usagePlan-quqxvett",
            "UsagePlanName": "auto_CreateAndUpdateUsageplan_Test_yu2hLs4d",
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

