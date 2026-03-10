**Example 1: 获取刷新时间列表**



Input: 

```
tccli wedata ListApplicationDashboardRefreshTime --cli-unfold-argument  \
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
            "DashboardVersion": 10,
            "DatasetRefreshInfos": [
                {
                    "Key": "fb9e4d1f176889318086406b99645",
                    "RefreshTime": "1769001606187"
                }
            ],
            "PageRefreshInfos": [
                {
                    "Key": "e75774b91768893167246edb97d0f",
                    "RefreshTime": "1769001606187"
                }
            ]
        },
        "RequestId": "1fb95490-6539-48a5-8d46-8d5533eb8477"
    }
}
```

