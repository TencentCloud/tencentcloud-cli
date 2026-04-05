**Example 1: 分享嵌出、大数据量批量查询**



Input: 

```
tccli wedata ShareBatchPullExtraAnalysis --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --DashboardKey 800017322219413504 \
    --Items.0.ResourceId res-0aa8c845 \
    --Items.0.PageSize 0 \
    --Items.0.PageNum 0 \
    --Items.0.DataModelKey fc3c9d4d176879276283850d1494e \
    --Items.0.WorkspaceId 17678671667189298 \
    --Items.0.DashboardKey 800017322219413504 \
    --TranId cb4f23c239206d00904a47adc58059ea
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [],
            "ErrorMessage": "",
            "TranId": "cb4f23c239206d00904a47adc58059ea",
            "TranStatus": "0"
        },
        "RequestId": "1f956b06-f949-4d0b-b2ee-b55584f7b114"
    }
}
```

