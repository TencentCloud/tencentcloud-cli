**Example 1: 示例1**



Input: 

```
tccli databuddy ListConsoleRoles --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 11 \
    --RoleKeyword 控制台
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
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
            ],
            "PageNumber": 0,
            "PageSize": 0,
            "TotalCount": 2,
            "TotalPageNumber": 1
        },
        "RequestId": "fdf47a6b-a09e-4773-b3dd-2ba6e80da36f"
    }
}
```

