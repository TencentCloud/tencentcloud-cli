**Example 1: 示例**



Input: 

```
tccli databuddy ListWorkspaceUsers --cli-unfold-argument  \
    --WorkspaceId 17841832994128461 \
    --RoleIds 3001
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1784183299474",
                    "IsAdmin": false,
                    "IsOwner": true,
                    "Nickname": "wedata30-dev@tencent.com",
                    "Roles": [
                        {
                            "Description": "",
                            "DisplayName": "",
                            "GroupNames": [],
                            "Id": "3001",
                            "Name": "Workspace Manager",
                            "RoleType": "",
                            "Source": 1
                        }
                    ],
                    "Tags": [],
                    "UpdateTime": "1784183299474",
                    "UserName": "wedata30-dev@tencent.com",
                    "UserSource": "user",
                    "UserTag": 0,
                    "UserUin": "700002164618"
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "77d65215-c743-478c-82f5-dbc14286668f"
    }
}
```

