**Example 1: 查询"COMMAND","REGISTER_CODE"资源**



Input: 

```
tccli tat DescribeQuotas --cli-unfold-argument  \
    --ResourceNames COMMAND REGISTER_CODE
```

Output: 
```
{
    "Response": {
        "RequestId": "321a2144-8e11-419e-b33c-6f6bfc25be4d",
        "GeneralResourceQuotaSet": [
            {
                "ResourceName": "COMMAND",
                "ResourceQuotaUsed": 26,
                "ResourceQuotaTotal": 509
            },
            {
                "ResourceName": "REGISTER_CODE",
                "ResourceQuotaUsed": 12,
                "ResourceQuotaTotal": 5000
            }
        ]
    }
}
```

