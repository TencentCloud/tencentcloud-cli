**Example 1: 创建沙箱快照**



Input: 

```
tccli ags CreateSandboxSnapshot --cli-unfold-argument  \
    --InstanceId ap35sxr52gtvkutvzfbjskfw45vsh3cn2atrkglf \
    --Memory False
```

Output: 
```
{
    "Response": {
        "Snapshot": {
            "CreateTime": "2026-08-06T04:59:06.162636734Z",
            "MemoryIncluded": false,
            "SnapshotId": "snapshot-019fd570-7a32-8013-8e9b-800f8082a260",
            "SourceInstanceId": "ap35sxr52gtvkutvzfbjskfw45vsh3cn2atrkglf",
            "Status": "ACTIVE",
            "StatusReason": "",
            "Tags": [],
            "UpdateTime": "2026-08-06T04:59:06.162636734Z"
        },
        "RequestId": "cf9da8d3-98c7-42f8-b014-6a3bbaf3e06f"
    }
}
```

