**Example 1: 获取工作组列表**



Input: 

```
tccli dlc DescribeUsersGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "UsersGroups": {
            "UserAppId": "abc",
            "UserGroupInfo": [
                {
                    "UserId": "abc",
                    "GroupIds": [
                        0
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

