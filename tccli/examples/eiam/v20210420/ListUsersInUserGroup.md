**Example 1: 请求示例**



Input: 

```
tccli eiam ListUsersInUserGroup --cli-unfold-argument  \
    --UserGroupId 1453013c-d0e9-424b-b9c7-dabcea3bd0ca
```

Output: 
```
{
    "Response": {
        "TotalNum": 1,
        "RequestId": "123",
        "UserGroupId": "062ee0c6-****-4dba-afb6-815bf5c6b62f",
        "UserInfo": [
            {
                "Status": "NOT_ENABLED",
                "UserName": "用户",
                "Email": "11****44298@qq.com",
                "UserId": "70496920-****-4fad-9e16-a2b99c632753",
                "Phone": "+86-133****2566",
                "DisplayName": "开发人员",
                "DataSource": "SELF_CREATE"
            }
        ]
    }
}
```

