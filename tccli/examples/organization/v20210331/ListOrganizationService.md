**Example 1: 获取集团服务设置列表**

获取集团服务设置列表

Input: 

```
tccli organization ListOrganizationService --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ServiceId": 1,
                "ProductName": "CloudAudit",
                "IsAssign": 1,
                "CanAssignCount": 5,
                "Description": "",
                "MemberNum": "0",
                "Document": "",
                "ConsoleUrl": "",
                "IsUsageStatus": 2,
                "Product": "cloudaudit",
                "ServiceGrant": 2,
                "GrantStatus": "Disabled",
                "IsSetManagementScope": 2
            }
        ],
        "RequestId": "1d744bef-fa56-40e9-8e3b-5a88b122ad5e",
        "Total": 1
    }
}
```

