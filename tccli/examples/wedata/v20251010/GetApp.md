**Example 1: 查询app**



Input: 

```
tccli wedata GetApp --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --AppKey 9a4597de1774267442653d6b64857
```

Output: 
```
{
    "Response": {
        "Data": {
            "Detail": {
                "AppName": "apptest123",
                "AppType": "AGENT",
                "CreatedBy": "700002164618",
                "CreatedOn": "1774267442652",
                "CurrentVersion": "v1",
                "Description": "",
                "Key": "9a4597de1774267442653d6b64857",
                "ModifiedBy": "700002164618",
                "ModifiedOn": "1774267471074",
                "Resources": [],
                "Status": "RUNNING",
                "TemplateKey": ""
            }
        },
        "RequestId": "eec8aad8-0d95-46df-8d47-4ab718f8a98d"
    }
}
```

