**Example 1: 查询用户列表**

查询用户列表

Input: 

```
tccli organization ListUsers --cli-unfold-argument  \
    --ZoneId z-2sw22w3
```

Output: 
```
{
    "Response": {
        "TotalCounts": 50,
        "MaxResults": 20,
        "Users": [
            {
                "UserName": "test",
                "FirstName": "test",
                "LastName": "test",
                "DisplayName": "test",
                "Description": "this is user",
                "Email": "test@example",
                "UserStatus": "Enabled",
                "UserType": "Manual",
                "UserId": "u-2s334e3***",
                "CreateTime": "2024-03-12 12:12:12",
                "UpdateTime": "2024-03-12 12:12:12"
            }
        ],
        "NextToken": "OTM0YzE4MzY2ZjdhMWM0MYZDhnYaxsiYTLI=",
        "IsTruncated": true,
        "RequestId": "e297543a-80de-4039-83c8-9d35d4545"
    }
}
```

