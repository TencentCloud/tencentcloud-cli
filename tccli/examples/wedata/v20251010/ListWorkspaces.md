**Example 1: 成功调用**



Input: 

```
tccli wedata ListWorkspaces --cli-unfold-argument  \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 1 \
    --WorkspaceId 1769**10*6*8***90
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "2025-11-05 17:05:49",
                    "Creator": {
                        "Nickname": "weda*a3**de*@*******.com",
                        "Uin": "70*0*2*****8",
                        "UserName": "wedat*3*-**v*t****nt.com"
                    },
                    "Description": "ab***1*05",
                    "ErrorReason": "",
                    "Status": 1,
                    "UpdateTime": "2025-11-05 17:05:49",
                    "WorkspaceId": "176**3*5*9**72931",
                    "WorkspaceName": "****_*105",
                    "WorkspaceRegion": "ap**ua*g**ou"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 1,
                "TotalCount": 35,
                "TotalPageNumber": 35
            }
        },
        "RequestId": "6b6335ea-4d28-43b3-91fb-92e6d738fa01"
    }
}
```

