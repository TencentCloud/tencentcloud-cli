**Example 1: 获取集团服务委派管理员列表**



Input: 

```
tccli organization ListOrgServiceAssignMember --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --ServiceId 1
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ServiceId": 1,
                "ProductName": "CloudAudit",
                "MemberUin": 111111111111,
                "MemberName": "mamber_name",
                "UsageStatus": 2,
                "CreateTime": "2022-03-12 12:19:12",
                "ManagementScope": 1,
                "ManagementScopeMembers": [],
                "ManagementScopeNodes": []
            }
        ],
        "RequestId": "1d744bef-fa56-40e9-8e3b-5a88b122ad5e",
        "Total": 1
    }
}
```

