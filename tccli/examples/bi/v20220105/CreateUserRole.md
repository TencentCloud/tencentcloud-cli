**Example 1: demo**

创建用户

Input: 

```
tccli bi CreateUserRole --cli-unfold-argument  \
    --RoleIdList 0 \
    --UserList.0.UserId abc \
    --UserList.0.UserName abc \
    --UserList.0.CorpId abc \
    --UserList.0.Email abc \
    --UserList.0.LastLogin 2020-09-22T00:00:00+00:00 \
    --UserList.0.Status 0 \
    --UserList.0.FirstModify 0 \
    --UserList.0.PhoneNumber abc \
    --UserList.0.AreaCode abc \
    --UserList.0.CreatedUser abc \
    --UserList.0.CreatedAt 2020-09-22T00:00:00+00:00 \
    --UserList.0.UpdatedUser abc \
    --UserList.0.UpdatedAt 2020-09-22T00:00:00+00:00 \
    --UserList.0.GlobalUserName abc \
    --UserList.0.Mobile abc \
    --UserInfoList.0.UserId abc \
    --UserInfoList.0.UserName abc \
    --UserInfoList.0.Email abc \
    --UserInfoList.0.PhoneNumber abc \
    --UserInfoList.0.AreaCode abc
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "30672eed-81e6-4d8f-a630-3d472531490b",
        "Extra": "",
        "Data": {
            "Id": 1
        }
    }
}
```

