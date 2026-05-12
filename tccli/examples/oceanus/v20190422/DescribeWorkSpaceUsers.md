**Example 1: 空间用户列表**



Input: 

```
tccli oceanus DescribeWorkSpaceUsers --cli-unfold-argument  \
    --WorkSpaceId space-1327
```

Output: 
```
{
    "Response": {
        "RequestId": "EF17520C-A177-404C-9B0A-01EBE4C0E15D",
        "RoleAuths": [
            {
                "AppId": 1257058945,
                "WorkSpaceSerialId": "spc-xxx",
                "OwnerUin": "100006386216",
                "CreatorUin": "100006386219",
                "AuthSubAccountUin": "100006386216",
                "Permission": 0,
                "CreateTime": "2021-12-25 13:30:28",
                "UpdateTime": "2021-12-25 13:30:28",
                "Status": 2
            }
        ]
    }
}
```

