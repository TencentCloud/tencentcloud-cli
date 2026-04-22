**Example 1: DescribeUserGroupInfo**

DescribeUserGroupInfo

Input: 

```
tccli bi DescribeUserGroupInfo --cli-unfold-argument  \
    --Id 261
```

Output: 
```
{
    "Response": {
        "Msg": "默认业务成功",
        "RequestId": "c86741ff-3639-429a-b2e7-045a6ba4f7a6",
        "Extra": "",
        "Data": {
            "Id": 261,
            "GroupName": "aaa",
            "ParentId": 29,
            "ParentName": "默认用户组",
            "IsDefault": 0,
            "AdminUserId": "700000280185,700000818998",
            "UserList": [
                {
                    "UserId": "700000818998",
                    "UserName": "bi_viewer_user"
                },
                {
                    "UserId": "700000280185",
                    "UserName": "power_sub_user"
                }
            ],
            "Description": "",
            "Location": 0
        }
    }
}
```

