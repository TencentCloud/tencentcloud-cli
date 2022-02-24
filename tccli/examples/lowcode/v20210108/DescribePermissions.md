**Example 1: 查询资源权限**



Input: 

```
tccli lowcode DescribePermissions --cli-unfold-argument  \
    --Limit 0 \
    --EnvId env-001 \
    --PermissionType 0 \
    --Role 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResourceList": [
                {
                    "AccessAble": false,
                    "ResourceId": "xx",
                    "ModifyTime": "xx",
                    "ResourceName": "xx"
                },
                {
                    "AccessAble": false,
                    "ResourceId": "xx",
                    "ModifyTime": "xx",
                    "ResourceName": "xx"
                },
                {
                    "AccessAble": false,
                    "ResourceId": "xx",
                    "ModifyTime": "xx",
                    "ResourceName": "xx"
                },
                {
                    "AccessAble": false,
                    "ResourceId": "xx",
                    "ModifyTime": "xx",
                    "ResourceName": "xx"
                },
                {
                    "AccessAble": false,
                    "ResourceId": "xx",
                    "ModifyTime": "xx",
                    "ResourceName": "xx"
                },
                {
                    "AccessAble": false,
                    "ResourceId": "xx",
                    "ModifyTime": "xx",
                    "ResourceName": "xx"
                }
            ],
            "TotalCount": 6,
            "PermissionType": 1,
            "Role": 0
        },
        "RequestId": "xx"
    }
}
```

