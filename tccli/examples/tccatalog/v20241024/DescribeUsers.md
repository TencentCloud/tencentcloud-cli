**Example 1: 展示用户列表**



Input: 

```
tccli tccatalog DescribeUsers --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --OrderBy create_time \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "TotalCount": 81,
        "UserSet": [
            {
                "CreateBy": "700001601851",
                "CreateTime": "2025-11-07T11:25:19+08:00",
                "Description": "",
                "GrantBy": "",
                "GrantTime": "",
                "PlatformId": 908,
                "RoleIds": null,
                "Source": 4,
                "UserId": 10000030684668,
                "UserIdStr": "10000030684668",
                "UserName": "700001601851",
                "UserType": "common"
            }
        ],
        "RequestId": "94d2cea4-f671-4fb4-9008-82add3556269"
    }
}
```

