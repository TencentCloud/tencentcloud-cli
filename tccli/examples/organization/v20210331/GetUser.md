**Example 1: 查询用户信息**

查询用户信息

Input: 

```
tccli organization GetUser --cli-unfold-argument  \
    --UserId u-4i293bf3indh \
    --ZoneId z-hfp2qqncf343
```

Output: 
```
{
    "Response": {
        "UserInfo": {
            "UserName": "user1",
            "FirstName": "john",
            "LastName": "smith",
            "DisplayName": "john",
            "Description": "this is user",
            "Email": "test@example.com",
            "UserStatus": "Enabled",
            "UserType": "Manual",
            "UserId": "u-2jsal3jdxk",
            "CreateTime": "2024-03-12 12:12:12",
            "UpdateTime": "2024-03-12 12:12:12"
        },
        "RequestId": "e297543a-80de-4039-83c8-34545s45"
    }
}
```

