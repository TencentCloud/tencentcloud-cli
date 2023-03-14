**Example 1: 查询自定义账户**

查询自定义账户

Input: 

```
tccli tcr DescribeCustomAccounts --cli-unfold-argument  \
    --RegistryId tcr-xxx \
    --EmbedPermission True \
    --All False \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "CustomAccounts": [
            {
                "Name": "tcr$robot",
                "Disable": false,
                "UpdateTime": "2022-09-22T00:00:00+00:00",
                "Permissions": [
                    {
                        "Resource": "library",
                        "Actions": [
                            "tcr:PushRepository",
                            "tcr:PullRepository"
                        ]
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

