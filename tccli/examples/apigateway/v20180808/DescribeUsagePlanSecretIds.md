**Example 1: 查询使用计划绑定的密钥**



Input: 

```
tccli apigateway DescribeUsagePlanSecretIds --cli-unfold-argument  \
    --UsagePlanId usagePlan-quqxvett
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "AccessKeyList": [
                {
                    "SecretName": "test",
                    "AccessKeyId": "AKID***********************************************",
                    "Status": 1
                }
            ]
        },
        "RequestId": "61f694d3-9c8b-4c4e-8d51-b2ab087c0d36"
    }
}
```

