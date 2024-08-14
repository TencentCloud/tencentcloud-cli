**Example 1: 修改用户信息**

修改用户信息

Input: 

```
tccli organization UpdateUser --cli-unfold-argument  \
    --ZoneId z-343nh23kn \
    --UserId u-3324sfdds \
    --NewFirstName test \
    --NewLastName test \
    --NewDisplayName test \
    --NewDescription this is user. \
    --NewEmail test@example.com
```

Output: 
```
{
    "Response": {
        "UserInfo": {
            "UserName": "test",
            "FirstName": "test",
            "LastName": "test",
            "DisplayName": "test",
            "Description": "this is user",
            "Email": "test@example.com",
            "UserStatus": "test",
            "UserType": "Manual",
            "UserId": "u-33sjadjsk",
            "CreateTime": "2024-01-01 12:12:12",
            "UpdateTime": "2024-01-01 12:12:12"
        },
        "RequestId": "e297543a-80de-4039-83c8-34545s45"
    }
}
```

