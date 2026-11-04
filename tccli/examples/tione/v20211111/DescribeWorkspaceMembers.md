**Example 1: 查询工作空间成员列表**



Input: 

```
tccli tione DescribeWorkspaceMembers --cli-unfold-argument  \
    --TiProjectId 1889353273052233728 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Members": [
            {
                "CreateTime": "2025-12-04T22:15:50+08",
                "NickName": "user1",
                "Roles": [],
                "SubUin": "100032950128"
            },
            {
                "CreateTime": "2025-12-04T16:41:05+08",
                "NickName": "user2",
                "Roles": [],
                "SubUin": "100037061107"
            }
        ],
        "RequestId": "8b1fe2e4-80e5-4c79-9fcc-3a7a14316bb9",
        "TotalCount": 2
    }
}
```

