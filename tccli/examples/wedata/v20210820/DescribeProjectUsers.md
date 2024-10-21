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
        "RequestId": "f59ff4b5-6999-484a-a7e2-960605d68333",
        "Data": {
            "Rows": [
                {
                    "UserId": "100006908545",
                    "UserName": "3193772711_WeData",
                    "DisplayName": "3193772711_WeData",
                    "Roles": [
                        {
                            "RoleId": "308335260274237440",
                            "Name": null,
                            "NameCn": "空间管理员",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        },
                        {
                            "RoleId": "308335260676890624",
                            "Name": null,
                            "NameCn": "数据科学家",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        },
                        {
                            "RoleId": "308335260844662784",
                            "Name": null,
                            "NameCn": "运维工程师",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        },
                        {
                            "RoleId": "308335260945326080",
                            "Name": null,
                            "NameCn": "访客",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        }
                    ],
                    "CreateTime": "2021-06-16 16:44:51",
                    "Creator": true
                },
                {
                    "UserId": "100015684538",
                    "UserName": "zhiqinzhang",
                    "DisplayName": "zhiqinzhang",
                    "Roles": [
                        {
                            "RoleId": "308335260676890624",
                            "Name": null,
                            "NameCn": "数据科学家",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        }
                    ],
                    "CreateTime": "2021-07-29 15:15:41",
                    "Creator": false
                }
            ],
            "PageNumber": 0,
            "PageSize": 10,
            "TotalCount": 7,
            "TotalPageNumber": 0
        }
    }
}
```

**Example 2: 成功示例-filter**

查询项目下所有用户

Input: 

```
tccli wedata DescribeProjectUsers --cli-unfold-argument  \
    --PageNumber 1 \
    --OrderFields.0.Direction DESC \
    --OrderFields.0.Name CreateTime \
    --PageSize 10 \
    --Filters.0.Values  \
    --Filters.0.Name DisplayName
```

Output: 
```
{
    "Response": {
        "RequestId": "4c659efc-0372-4e3d-a484-0476b564420d",
        "Data": {
            "Rows": [
                {
                    "UserId": "100013890962",
                    "UserName": "",
                    "DisplayName": "sundyang",
                    "Roles": [
                        {
                            "RoleId": "308335260676890624",
                            "Name": null,
                            "NameCn": "数据工程师",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        }
                    ],
                    "CreateTime": "2021-07-29 15:14:54",
                    "Creator": false
                },
                {
                    "UserId": "100020026287",
                    "UserName": "",
                    "DisplayName": "v_huangaluo",
                    "Roles": [
                        {
                            "RoleId": "308335260274237440",
                            "Name": null,
                            "NameCn": "项目管理员",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        },
                        {
                            "RoleId": "308335260676890624",
                            "Name": null,
                            "NameCn": "数据工程师",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        },
                        {
                            "RoleId": "308335260844662784",
                            "Name": null,
                            "NameCn": "运维工程师",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        },
                        {
                            "RoleId": "308335260945326080",
                            "Name": null,
                            "NameCn": "访客",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        }
                    ],
                    "CreateTime": "2021-07-09 15:20:22",
                    "Creator": false
                },
                {
                    "UserId": "100019904305",
                    "UserName": "",
                    "DisplayName": "kuanliu",
                    "Roles": [
                        {
                            "RoleId": "308335260274237440",
                            "Name": null,
                            "NameCn": "项目管理员",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        },
                        {
                            "RoleId": "308335260676890624",
                            "Name": null,
                            "NameCn": "数据工程师",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        },
                        {
                            "RoleId": "308335260844662784",
                            "Name": null,
                            "NameCn": "运维工程师",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        },
                        {
                            "RoleId": "308335260945326080",
                            "Name": null,
                            "NameCn": "访客",
                            "Description": null,
                            "Privileges": [],
                            "MethodPaths": null
                        }
                    ],
                    "CreateTime": "2021-07-09 15:20:22",
                    "Creator": false
                }
            ],
            "PageNumber": 0,
            "PageSize": 10,
            "TotalCount": 3,
            "TotalPageNumber": 0
        }
    }
}
```

