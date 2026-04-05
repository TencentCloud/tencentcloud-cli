**Example 1: ListWorkspaceAddableUsers**

工作空间添加用户时，查询用户列表

Input: 

```
tccli wedata ListWorkspaceAddableUsers --cli-unfold-argument  \
    --WorkspaceId 17621416814092400 \
    --Keywords None \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 5
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1761989539",
                    "IsAdmin": false,
                    "IsOwner": false,
                    "Nickname": "micofywang",
                    "Roles": [
                        {
                            "Description": "",
                            "DisplayName": "",
                            "Id": "2001",
                            "Name": "Console Manager",
                            "RoleType": ""
                        },
                        {
                            "Description": "",
                            "DisplayName": "",
                            "Id": "2002",
                            "Name": "Console Member",
                            "RoleType": ""
                        }
                    ],
                    "Uin": "700002196961",
                    "UpdateTime": "1761989539",
                    "UserName": "micofywang",
                    "UserSource": "",
                    "UserTag": 0
                },
                {
                    "CreateTime": "1761913419",
                    "IsAdmin": false,
                    "IsOwner": false,
                    "Nickname": "erinhong",
                    "Roles": [
                        {
                            "Description": "",
                            "DisplayName": "",
                            "Id": "2002",
                            "Name": "Console Member",
                            "RoleType": ""
                        }
                    ],
                    "Uin": "100044422498",
                    "UpdateTime": "1761913419",
                    "UserName": "erinhong",
                    "UserSource": "",
                    "UserTag": 0
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 5,
                "TotalCount": 2,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "59d5662c-f072-43eb-a724-5299bef24386"
    }
}
```

