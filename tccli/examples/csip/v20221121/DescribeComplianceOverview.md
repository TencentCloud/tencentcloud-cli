**Example 1: DescribeComplianceOverview**



Input: 

```
tccli csip DescribeComplianceOverview --cli-unfold-argument  \
    --MemberId mem-00ajshjds \
    --ContentFilter all
```

Output: 
```
{
    "Response": {
        "AllCheckItems": {
            "CheckTypes": [
                {
                    "CheckType": "account_security",
                    "Count": 32
                }
            ],
            "PassRate": 72,
            "TotalCount": 176
        },
        "Standards": [
            {
                "ID": 1,
                "Name": "CIS阿里云基础基准v2.0.0",
                "PassRate": 0,
                "TotalCount": 0
            }
        ],
        "RequestId": "c5045da7-8b88-4fb8-ba69-cfb31a454b0a"
    }
}
```

