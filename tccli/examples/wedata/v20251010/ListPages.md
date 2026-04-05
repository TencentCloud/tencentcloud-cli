**Example 1: ListPages**



Input: 

```
tccli wedata ListPages --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --DashboardAccessKey 800017322219413504
```

Output: 
```
{
    "Response": {
        "Data": {
            "Pages": [
                {
                    "CustomerRefId": "f7420ad50171468ab13bb48bbbe3e5c0",
                    "DisplayName": "无标题页面",
                    "PageAccessKey": "b945260d1768546993350aefface7",
                    "PageLayout": "[{\"i\":\"widget-258f1cee-5029-4efa-be39-54ef0d789d52\",\"x\":0,\"y\":0,\"w\":3,\"h\":6,\"type\":\"pie\"},{\"i\":\"widget-7584fca6-45ba-44e2-b1aa-c743d8260745\",\"x\":3,\"y\":0,\"w\":3,\"h\":6,\"type\":\"line\"},{\"i\":\"widget-09ed65f5-9297-4e6e-98c6-c7c949048fab\",\"x\":0,\"y\":6,\"w\":3,\"h\":6,\"type\":\"table\"},{\"i\":\"widget-f7ecd410-a4a5-42c0-8afc-a3173901c665\",\"x\":3,\"y\":6,\"w\":3,\"h\":6,\"type\":\"bar\"}]",
                    "PageType": "PAGE_TYPE_NORMAL",
                    "PageVersion": 8
                }
            ]
        },
        "RequestId": "df34a3b2-8fdc-4a81-a2c2-488a9515c61e"
    }
}
```

