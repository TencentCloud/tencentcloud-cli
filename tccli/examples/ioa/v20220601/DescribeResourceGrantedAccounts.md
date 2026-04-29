**Example 1: 查询直接授权的账号**



Input: 

```
tccli ioa DescribeResourceGrantedAccounts --cli-unfold-argument  \
    --ResourceId 7
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccountId": 5101,
                    "ExpireTime": 1,
                    "GroupId": 2571,
                    "GroupIdPathArray": [
                        2
                    ],
                    "GroupNamePathArray": [
                        "全网账户"
                    ],
                    "MenuId": 2571,
                    "RelationId": 23,
                    "UserId": "lshawn",
                    "UserName": "lshawn"
                }
            ]
        },
        "RequestId": "16fb06f0-6619-4594-b5bd-1f330be83a37"
    }
}
```

