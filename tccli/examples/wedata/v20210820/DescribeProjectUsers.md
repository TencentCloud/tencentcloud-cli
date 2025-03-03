**Example 1: 成功示例2**

查询项目下用户

Input: 

```
tccli wedata DescribeProjectUsers --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 0,
            "PageSize": 1,
            "Rows": [
                {
                    "AppId": null,
                    "CreateTime": "2024-08-14T17:48:55+08:00",
                    "Creator": true,
                    "DisplayName": "peterpksong",
                    "Email": null,
                    "IsProjectAdmin": true,
                    "OwnerUin": null,
                    "PhoneNum": null,
                    "Roles": [
                        {
                            "Description": null,
                            "MethodPaths": null,
                            "Name": "ProjectManager",
                            "NameCn": "项目管理员",
                            "Params": null,
                            "Privileges": null,
                            "RoleId": "308335260274237440",
                            "RoleType": null,
                            "SystemInit": null
                        }
                    ],
                    "UserId": "100028694266",
                    "UserName": "peterpksong"
                }
            ],
            "TotalCount": 2,
            "TotalPageNumber": 2
        },
        "RequestId": "477b3ec7-afe2-4d3d-a772-52100d60d668"
    }
}
```

