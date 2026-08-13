**Example 1: 成功**



Input: 

```
tccli bi ModifyUserGroup --cli-unfold-argument  \
    --UpdateList.0.AdminUserId 700000231283 \
    --UpdateList.0.Description 用户组描述 \
    --UpdateList.0.GroupName test0812001 \
    --UpdateList.0.Location 12 \
    --UpdateList.0.ParentId -1 \
    --UpdateList.0.Id 382
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AdminUserId": "700000231283",
                "Description": "用户组描述",
                "GroupName": "test0812001",
                "Id": 382,
                "IsDefault": 0,
                "Location": 12,
                "ParentId": -1,
                "ParentName": null,
                "UserList": null
            }
        ],
        "Extra": "",
        "Msg": "默认业务成功",
        "RequestId": "0e2e19c9-b201-403e-90a9-c7f8a3cd08e7"
    }
}
```

