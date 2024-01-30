**Example 1: 修改用户角色信息**

修改用户角色信息

Input: 

```
tccli bi ModifyUserRole --cli-unfold-argument  \
    --UserId abc \
    --RoleIdList 0 \
    --Email abc \
    --UserName abc \
    --PhoneNumber abc \
    --AreaCode abc \
    --AppUserId abc
```

Output: 
```
{
    "Response": {
        "ErrorInfo": {
            "ErrorTip": "abc",
            "ErrorLevel": "abc",
            "DocLink": "abc",
            "FAQ": "abc",
            "ReservedField": "abc"
        },
        "Extra": "abc",
        "Msg": "abc",
        "Data": "abc",
        "RequestId": "abc"
    }
}
```

