**Example 1: 查询服务级账号**

查询服务级账号

Input: 

```
tccli tcr DescribeServiceAccounts --cli-unfold-argument  \
    --RegistryId abc \
    --All True \
    --EmbedPermission True \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "ServiceAccounts": [
            {
                "Name": "abc",
                "Description": "abc",
                "Disable": true,
                "ExpiresAt": 0,
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "UpdateTime": "2020-09-22T00:00:00+00:00",
                "Permissions": [
                    {
                        "Resource": "abc",
                        "Actions": [
                            "abc"
                        ]
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

