**Example 1: 查询工作空间列表**



Input: 

```
tccli wedata ListConsoleWorkspaces --cli-unfold-argument  \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1763638175350",
                    "Creator": {
                        "Nickname": "",
                        "Uin": "600000561778",
                        "UserName": "",
                        "UserTag": ""
                    },
                    "Description": "e'f'er'w",
                    "ErrorReason": "",
                    "Status": 3,
                    "UpdateTime": "1763638176199",
                    "WorkspaceId": "17636381753502681",
                    "WorkspaceName": "hrth",
                    "WorkspaceRegion": "ap-guangzhou"
                }
            ],
            "PageResponse": {
                "ExtendInfo": "",
                "PageNumber": 1,
                "PageSize": 10,
                "TotalCount": 1,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "6a8116d2-25ed-4238-9a1d-61cecce78874"
    }
}
```

