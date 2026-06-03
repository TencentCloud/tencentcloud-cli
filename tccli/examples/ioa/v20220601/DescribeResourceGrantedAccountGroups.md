**Example 1: 查询授权的账号分组**



Input: 

```
tccli ioa DescribeResourceGrantedAccountGroups --cli-unfold-argument  \
    --ResourceId 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccountCount": 3,
                    "AccountGroupId": 96,
                    "ExpireTime": 0,
                    "IdPathArray": [
                        2
                    ],
                    "Name": "旧版-自建-勿删",
                    "NamePathArray": [
                        "全网账户"
                    ],
                    "RelationId": 12
                }
            ]
        },
        "RequestId": "41dc529a-e6d1-434c-9e30-9de07a42097e"
    }
}
```

