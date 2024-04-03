**Example 1: demo**



Input: 

```
tccli bi CreateUserRoleProject --cli-unfold-argument  \
    --UserList.0.UserName null \
    --UserList.0.UserId null \
    --ProjectId 000 \
    --RoleIdList 100100 \
    --UserInfoList.0.UserName tommyho \
    --UserInfoList.0.PhoneNumber 123456789 \
    --UserInfoList.0.AreaCode 86 \
    --UserInfoList.0.UserId tommyho \
    --UserInfoList.0.Email 123@qq.com
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

**Example 2: 项目内-创建用户角色示例接口**



Input: 

```
tccli bi CreateUserRoleProject --cli-unfold-argument  \
    --UserList.0.UserName 王成林 \
    --UserList.0.UserId lenwang \
    --ProjectId 1 \
    --RoleIdList 100090
```

Output: 
```
{
    "Response": {
        "RequestId": "ed4d2bd1-ee13-4b67-80cf-a8a2794a82ed",
        "Extra": "",
        "Data": {
            "Id": 1
        },
        "Msg": "success"
    }
}
```

