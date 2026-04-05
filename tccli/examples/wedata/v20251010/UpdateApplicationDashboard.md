**Example 1: 修改仪表盘名称**



Input: 

```
tccli wedata UpdateApplicationDashboard --cli-unfold-argument  \
    --AccessKey 801469279624839168 \
    --WorkspaceId 17663856806379896 \
    --DisplayName test_name
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessKey": "801469279624839168",
            "DashboardVersion": 29
        },
        "RequestId": "1e4c456c-bf1d-4ea8-9830-b6c615d912a9"
    }
}
```

