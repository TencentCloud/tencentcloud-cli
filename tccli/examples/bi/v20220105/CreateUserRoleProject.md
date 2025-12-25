**Example 1: demo**



Input: 

```
tccli bi CreateUserRoleProject --cli-unfold-argument  \
    --ProjectId 1982493789748932 \
    --RoleIdList 1982493789748932 \
    --UserInfoList.0.UserId zhangsan \
    --UserInfoList.0.UserName 用户名 \
    --UserInfoList.0.Email 邮箱 \
    --UserInfoList.0.PhoneNumber 手机号 \
    --UserInfoList.0.AreaCode 手机号区号 \
    --UserInfoList.0.AppUserId 企微账号id \
    --UserInfoList.0.AppUserName 企微账号名称 \
    --UserList.0.UserId zhangsan \
    --UserList.0.UserName 用户名 \
    --UserList.0.CorpId 企业ID \
    --UserList.0.Email 电子邮箱 \
    --UserList.0.Status 1982493789748932 \
    --UserList.0.FirstModify 1982493789748932 \
    --UserList.0.PhoneNumber 手机号码 \
    --UserList.0.AreaCode 手机区号 \
    --UserList.0.CreatedUser 创建人 \
    --UserList.0.UpdatedUser 更改人 \
    --UserList.0.GlobalUserName 全局角色 \
    --UserList.0.Mobile 手机号 \
    --UserList.0.AppId 1 \
    --UserList.0.AppUserId 1 \
    --UserList.0.AppUserAliasName 1 \
    --UserList.0.AppUserName 1 \
    --UserList.0.InValidateAppRange False
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "6cd11622-b240-40ae-8ec0-86b933aab8da",
        "Extra": "",
        "Data": {
            "Id": 0
        }
    }
}
```

