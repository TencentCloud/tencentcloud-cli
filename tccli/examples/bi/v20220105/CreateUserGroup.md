**Example 1: CreateUserGroup**

添加用户组

Input: 

```
tccli bi CreateUserGroup --cli-unfold-argument  \
    --AdminUserId userId \
    --Description /描述 \
    --GroupName 测试用户组 \
    --Location 0 \
    --ParentId -1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AdminUserId": "userId",
            "Description": "/描述",
            "GroupName": "测试用户组",
            "Id": 273,
            "IsDefault": 0,
            "Location": 7,
            "ParentId": -1,
            "ParentName": null,
            "UserList": null
        },
        "Extra": "",
        "Msg": "默认业务成功",
        "RequestId": "7b8dad84-4285-4717-ac6d-5a76a29cb815"
    }
}
```

