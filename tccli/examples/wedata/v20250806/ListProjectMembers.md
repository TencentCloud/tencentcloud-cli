**Example 1: 成功调用**



Input: 

```
tccli wedata ListProjectMembers --cli-unfold-argument  \
    --ProjectId 2917360018413740032 \
    --UserUin 100028721707
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AppId": null,
                    "CreateTime": "2025-08-29T14:23:17+08:00",
                    "DisplayName": "jianwjwang",
                    "Email": null,
                    "IsCreator": false,
                    "IsProjectOwner": false,
                    "PhoneNum": null,
                    "Roles": [
                        {
                            "Description": null,
                            "RoleDisplayName": "u9879u76eeu7ba1u7406u5458",
                            "RoleId": "308335260274237440",
                            "RoleName": "ProjectManager"
                        }
                    ],
                    "RootAccountId": null,
                    "UserName": "jianwjwang",
                    "UserUin": null
                }
            ],
            "PageNumber": 0,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 0
        },
        "RequestId": "e7b8cab3-1f87-4647-9acf-3da3c7655946"
    }
}
```

