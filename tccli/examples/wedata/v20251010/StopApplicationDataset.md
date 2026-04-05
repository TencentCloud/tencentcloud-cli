**Example 1: 停止查询请求任务**



Input: 

```
tccli wedata StopApplicationDataset --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --TranId 1facc3618f8c1e4c4b9b53aea08c5a6e \
    --DashboardAccessKey 798652297072988160 \
    --Status DRAFT
```

Output: 
```
{
    "Response": {
        "Data": {
            "CancelStatus": "",
            "JobId": "",
            "Jobs": [],
            "TranId": "1facc3618f8c1e4c4b9b53aea08c5a6e"
        },
        "RequestId": "f985e123-5e98-4a76-87c3-400e64e5b57e"
    }
}
```

