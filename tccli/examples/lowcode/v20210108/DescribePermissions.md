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
            "PermissionType": 0,
            "Role": 0,
            "TotalCount": 0,
            "ResourceList": [
                {
                    "ResourceId": "abc",
                    "ResourceName": "abc",
                    "ModifyTime": "abc",
                    "AccessAble": true,
                    "ResourceKey": "abc",
                    "UserSelfPermission": {
                        "Readable": true,
                        "Writable": true,
                        "WritableCondition": [
                            {
                                "Key": "abc",
                                "Rel": "abc",
                                "Val": "abc",
                                "ValueType": "abc"
                            }
                        ],
                        "ReadableCondition": [
                            {
                                "Key": "abc",
                                "Rel": "abc",
                                "Val": "abc",
                                "ValueType": "abc"
                            }
                        ]
                    },
                    "AllPermission": {
                        "Readable": true,
                        "Writable": true,
                        "WritableCondition": [
                            {
                                "Key": "abc",
                                "Rel": "abc",
                                "Val": "abc",
                                "ValueType": "abc"
                            }
                        ]
                    }
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

