**Example 1: 获取仪表盘元数据信息**



Input: 

```
tccli wedata GetApplicationDashboardMetaData --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --Key 801469279624839168
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreatedBy": "700002164618",
            "CreatedOn": "1768893167222",
            "DisplayName": "New Dashboard 2026-01-20 15:12:44",
            "Key": "801469279624839168",
            "ModifiedBy": "700002164618",
            "ModifiedOn": "1768983282238",
            "Owner": "700002164618",
            "Path": "/Workspace/Users/wedata30-dev@tencent.com@700002164618/New Dashboard 2026-01-20 15:12:44"
        },
        "RequestId": "f5dbde3b-4dfd-41fb-a21c-3882faa951a0"
    }
}
```

