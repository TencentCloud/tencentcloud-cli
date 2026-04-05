**Example 1: app列表**



Input: 

```
tccli wedata ListApps --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --PageRequest.AllPage True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AppName": "apptest123",
                    "AppType": "AGENT",
                    "CreatedBy": "700002164618",
                    "CreatedOn": "1774267442652",
                    "CurrentVersion": "v1",
                    "Description": "",
                    "Key": "9a4597de1774267442653d6b64857",
                    "ModifiedBy": "700002164618",
                    "ModifiedOn": "1774267471074",
                    "Status": "RUNNING"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 4,
                "TotalCount": 4,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "fdb6eac5-df37-4258-a81e-dc795935227e"
    }
}
```

