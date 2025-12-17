**Example 1: 展示角色列表**



Input: 

```
tccli tccatalog DescribeRoles --cli-unfold-argument  \
    --PlatformId 100008882712
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RoleSet": [
            {
                "RoleId": 10234,
                "RoleName": "DataAudit",
                "UserCount": 15,
                "CreateTime": "2024-03-15T08:30:00Z",
                "CreateBy": "100008882712",
                "Description": "财务审计专用角色"
            },
            {
                "RoleId": 10235,
                "RoleName": "RiskControl",
                "UserCount": 8,
                "CreateTime": "2024-03-16T14:20:00Z",
                "CreateBy": "100008882712",
                "Description": "风控合规操作组"
            }
        ],
        "RequestId": "d6e4a9b1-7f2c-4a8d-b5e3-1c9f8a6b2d0e"
    }
}
```

