**Example 1: 成功**



Input: 

```
tccli bi CreateUserGroup --cli-unfold-argument  \
    --AdminUserId 700000231283 \
    --Description 用户组描述 \
    --GroupName test0812001 \
    --Location -1 \
    --ParentId -1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AdminUserId": "700000231283",
            "Description": "用户组描述",
            "GroupName": "test0812001",
            "Id": 382,
            "IsDefault": 0,
            "Location": 12,
            "ParentId": -1,
            "ParentName": null,
            "UserList": null
        },
        "Extra": "",
        "Msg": "默认业务成功",
        "RequestId": "25ede453-df25-4cb5-ae6f-e48c4fc87ea7"
    }
}
```

