**Example 1: ListConsoleUsers**

控制台查询用户列表

Input: 

```
tccli wedata ListConsoleUsers --cli-unfold-argument  \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 5 \
    --Keywords None \
    --RoleIds None \
    --SortInfo.SortKey None \
    --SortInfo.IsDesc None
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
                            "Description": "对控制台功能仅有只读权限",
                            "DisplayName": "控制台成员",
                            "Id": "2002",
                            "Name": "ConsoleMember",
                            "RoleType": "console"
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
                            "Description": "对控制台功能仅有只读权限",
                            "DisplayName": "控制台成员",
                            "Id": "2002",
                            "Name": "ConsoleMember",
                            "RoleType": "console"
                        }
                    ],
                    "Uin": "100044422498",
                    "UpdateTime": "1761913419",
                    "UserName": "erinhong",
                    "UserSource": "",
                    "UserTag": 0
                },
                {
                    "CreateTime": "1761913419",
                    "IsAdmin": false,
                    "IsOwner": true,
                    "Nickname": "my_test",
                    "Roles": [
                        {
                            "Description": "对控制台功能仅有只读权限",
                            "DisplayName": "控制台成员",
                            "Id": "2002",
                            "Name": "ConsoleMember",
                            "RoleType": "console"
                        }
                    ],
                    "Uin": "600000561778",
                    "UpdateTime": "1761913419",
                    "UserName": "my_test",
                    "UserSource": "",
                    "UserTag": 0
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 5,
                "TotalCount": 3,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "db78547a-c288-4c5a-bb1c-e6ea4329fb18"
    }
}
```

