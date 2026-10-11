**Example 1: 查询沙箱快照列表**



Input: 

```
tccli ags DescribeSandboxSnapshotList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SnapshotSet": [
            {
                "CreateTime": "2026-08-06T04:59:06.164Z",
                "MemoryIncluded": false,
                "SnapshotId": "snapshot-019fd570-7a32-8013-8e9b-800f8082a260",
                "SourceInstanceId": "ap35sxr52gtvkutvzfbjskfw45vsh3cn2atrkglf",
                "Status": "ACTIVE",
                "StatusReason": "",
                "Tags": [],
                "UpdateTime": "2026-08-06T04:59:06.304Z"
            }
        ],
        "TotalCount": 3,
        "RequestId": "f360264d-452f-4fe7-a71c-02e43f0c32a8"
    }
}
```

