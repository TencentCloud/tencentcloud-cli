**Example 1: 清除缓存**



Input: 

```
tccli wedata UpdateApplicationDashboardCache --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --AccessKey 801469279624839168 \
    --Status DRAFT
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessKey": "801469279624839168",
            "DashboardVersion": 10
        },
        "RequestId": "6991164f-7984-409c-ac87-4c200889224d"
    }
}
```

