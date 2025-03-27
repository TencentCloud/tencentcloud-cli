**Example 1: 修改用户角色信息**

修改用户角色信息

Input: 

```
tccli bi ModifyUserRole --cli-unfold-argument  \
    --UserId UserId \
    --RoleIdList 1982493789748932 \
    --Email 123***@qq.com \
    --UserName zhangsan \
    --PhoneNumber PhoneNumber \
    --AreaCode AreaCode \
    --AppUserId AppUserId \
    --LoginSecurityStatus 1982493789748932 \
    --ResetPassWordTip 1982493789748932 \
    --ForceResetPassWord 1982493789748932 \
    --PasswordExpired 1982493789748932
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "9478b0d0-1e95-4d12-88a6-db36fb27a12b",
        "Extra": "Extra",
        "Data": "Data"
    }
}
```

