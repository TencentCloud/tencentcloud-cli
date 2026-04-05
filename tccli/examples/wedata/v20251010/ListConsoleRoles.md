**Example 1: demo**



Input: 

```
tccli wedata ListConsoleRoles --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "PageResponse": {
                "PageNumber": 0,
                "PageSize": 0,
                "TotalCount": 2,
                "TotalPageNumber": 0
            },
            "Roles": [
                {
                    "BasicInfo": {
                        "Description": "能够管理工作空间、用户和用户组以及平台设置",
                        "DisplayName": "控制台管理员",
                        "Id": "2001",
                        "Name": "",
                        "RoleType": "console"
                    },
                    "MetaData": {
                        "CreateTime": "",
                        "Creator": "",
                        "UpdateTime": "",
                        "Updater": ""
                    },
                    "Permissions": []
                }
            ]
        },
        "RequestId": "864bde36-0bb7-4737-b7f7-bac8daf383c8"
    }
}
```

