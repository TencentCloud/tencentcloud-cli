**Example 1: DescribeUsagePlan**



Input: 

```
tccli apigateway DescribeUsagePlan --cli-unfold-argument  \
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
            "BindSecretIdTotalCount": 0,
            "BindSecretIds": [],
            "BindEnvironmentTotalCount": 0,
            "BindEnvironments": []
        },
        "RequestId": "e61705f3-e88a-4311-ada3-526bad10f7ab"
    }
}
```

