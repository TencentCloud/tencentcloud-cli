**Example 1: 查询用户组中的用户列表**

查询用户组中的用户列表

Input: 

```
tccli organization ListGroupMembers --cli-unfold-argument  \
    --ZoneId z-ds932j9m3 \
    --GroupId g29sn2389e \
    --NextToken  \
    --MaxResults 10
```

Output: 
```
{
    "Response": {
        "NextToken": "OTM0YzE4MzY2ZjdhMWM0MYZDhnYaxsiYTLI=",
        "TotalCounts": 20,
        "MaxResults": 10,
        "IsTruncated": true,
        "GroupMembers": [
            {
                "UserName": "user1",
                "DisplayName": "john",
                "Description": "this is test user",
                "Email": "123456@qq.com",
                "UserStatus": "Enabled",
                "UserType": "Manual",
                "UserId": "u-d032med3",
                "JoinTime": "2024-01-01 12:12:12"
            }
        ],
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

