**Example 1: ModifyUsagePlan**



Input: 

```
tccli apigateway ModifyUsagePlan --cli-unfold-argument  \
    --UsagePlanId usagePlan-bxtnltfd
```

Output: 
```
{
    "Response": {
        "Result": {
            "UsagePlanId": "usagePlan-bxtnltfd",
            "UsagePlanName": "xx",
            "UsagePlanDesc": null,
            "MaxRequestNumPreSec": null,
            "MaxRequestNum": null,
            "CreatedTime": "2020-02-26T14:19:52Z",
            "ModifiedTime": "2020-02-26T14:25:30Z",
            "BindSecretIdTotalCount": null,
            "BindSecretIds": null,
            "BindEnvironmentTotalCount": null,
            "BindEnvironments": null
        },
        "RequestId": "d929b56e-d7c3-4929-a103-3302fa9fee2e"
    }
}
```

