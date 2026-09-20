**Example 1: 示例1**



Input: 

```
tccli databuddy ListConsoleUsers --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 11 \
    --UserKeyword junzha2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1784861927",
                    "IsAdmin": false,
                    "IsOwner": false,
                    "Nickname": "junzha2",
                    "Roles": [
                        {
                            "Description": "对控制台功能仅有只读权限",
                            "DisplayName": "控制台成员",
                            "Id": "2002",
                            "Name": "Console Member",
                            "RoleType": "console"
                        }
                    ],
                    "UpdateTime": "1784861927",
                    "UserName": "junzha2",
                    "UserSource": "",
                    "UserTag": 0,
                    "UserUin": "700002692363"
                }
            ],
            "PageNumber": 1,
            "PageSize": 11,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "47e28ab5-3d75-41d9-8c82-2f5761960dd1"
    }
}
```

