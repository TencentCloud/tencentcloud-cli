**Example 1: 项目-修改用户信息**

项目-修改用户信息

Input: 

```
tccli bi ModifyUserRoleProject --cli-unfold-argument  \
    --ProjectId 1982493789748932 \
    --UserId UserId \
    --RoleIdList 1982493789748932 \
    --Email 123***@qq.com \
    --UserName zhangsan \
    --AppUserId AppUserId
```

Output: 
```
{
    "Response": {
        "ErrorInfo": {
            "ErrorTip": "",
            "ErrorLevel": "INFO",
            "DocLink": "",
            "FAQ": "",
            "ReservedField": ""
        },
        "Extra": "",
        "Msg": "成功",
        "Data": "",
        "RequestId": "sadd23jdsh-123cdjds"
    }
}
```

