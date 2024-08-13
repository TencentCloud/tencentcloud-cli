**Example 1: 创建用户**

创建用户

Input: 

```
tccli organization CreateUser --cli-unfold-argument  \
    --ZoneId z-33w3je**** \
    --UserName Alice \
    --FirstName Alice \
    --LastName Alice \
    --DisplayName Alice \
    --Description this is user \
    --Email Alice@example.com \
    --UserStatus Enabled
```

Output: 
```
{
    "Response": {
        "UserInfo": {
            "UserName": "Alice",
            "FirstName": "Alice",
            "LastName": "Alice",
            "DisplayName": "Alice",
            "Description": "this is user",
            "Email": "Alice@example.com",
            "UserStatus": "Enabled",
            "UserType": "Manual",
            "UserId": "u-2342ds2s",
            "CreateTime": "2024-02-02 12:12:12",
            "UpdateTime": "2024-02-02 12:12:12"
        },
        "RequestId": "e297543a-80de-4039-83c8-9d35d4545"
    }
}
```

