**Example 1: 分享嵌出、仪表盘更新时间**



Input: 

```
tccli wedata ShareApplicationDashboardRefreshTimeList --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --AccessKey 797848762287833088 \
    --Status PUBLISHED
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessKey": "797848762287833088",
            "DashboardVersion": 81,
            "DatasetRefreshInfos": [
                {
                    "Key": "7de5efd89b97479217680299904139f44838600d8ee0b",
                    "RefreshTime": "1768894258530"
                }
            ],
            "PageRefreshInfos": [
                {
                    "Key": "313f6f3fb4b647da17680299689769e5e0f71e245c60f",
                    "RefreshTime": "1768894258530"
                }
            ]
        },
        "RequestId": "c55c45e2-c36b-477e-9062-d6f8f9a070dc"
    }
}
```

