**Example 1: demo**

创建用户

Input: 

```
tccli bi CreateUserRole --cli-unfold-argument  \
    --RoleIdList 0 \
    --UserList.0.UserId 1101 \
    --UserList.0.UserName 张三 \
    --UserList.0.CorpId 150101 \
    --UserList.0.Email 242113***@qq.com \
    --UserList.0.LastLogin 2020-09-22T00:00:00+00:00 \
    --UserList.0.Status 0 \
    --UserList.0.FirstModify 0 \
    --UserList.0.PhoneNumber 86******8998 \
    --UserList.0.AreaCode 001 \
    --UserList.0.CreatedUser 1210201 \
    --UserList.0.CreatedAt 2020-09-22T00:00:00+00:00 \
    --UserList.0.UpdatedUser 1210201 \
    --UserList.0.UpdatedAt 2020-09-22T00:00:00+00:00 \
    --UserList.0.GlobalUserName 张三 \
    --UserList.0.Mobile 139******8998 \
    --UserInfoList.0.UserId 1101 \
    --UserInfoList.0.UserName 张三 \
    --UserInfoList.0.Email 242113***@qq.com \
    --UserInfoList.0.PhoneNumber 86******8998 \
    --UserInfoList.0.AreaCode 001
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

