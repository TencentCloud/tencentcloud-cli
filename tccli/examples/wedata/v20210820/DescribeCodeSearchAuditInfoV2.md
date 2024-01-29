**Example 1: 示例1**

demo

Input: 

```
tccli wedata DescribeCodeSearchAuditInfoV2 --cli-unfold-argument  \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Keyword": "select",
                "OwnerUserId": 100028448903,
                "ProjectId": 1460947878944567300,
                "TenantId": 1315051789,
                "UserId": 100028579606
            },
            {
                "Keyword": "select1",
                "OwnerUserId": 100028448903,
                "ProjectId": 1460947878944567300,
                "TenantId": 1315051789,
                "UserId": 100028579606
            }
        ],
        "RequestId": "09ef5f1b-4167-4e7a-bcaa-94a9c1ad03cb"
    }
}
```

