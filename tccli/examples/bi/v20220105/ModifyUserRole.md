**Example 1: 修改用户角色信息**

修改用户角色信息

Input: 

```
tccli bi ModifyUserRole --cli-unfold-argument  \
    --UserId 21021 \
    --RoleIdList 0 1 231 213 \
    --Email 2313**2312@qq.com \
    --UserName zhangsn \
    --PhoneNumber 86212***12 \
    --AreaCode 086 \
    --AppUserId 123142
```

Output: 
```
{
    "Response": {
        "ErrorInfo": {
            "ErrorTip": "",
            "ErrorLevel": "ERROR",
            "DocLink": "",
            "FAQ": "",
            "ReservedField": ""
        },
        "Extra": "",
        "Msg": "失败",
        "Data": "",
        "RequestId": "sddsdfsbghbwe1-211ds"
    }
}
```

