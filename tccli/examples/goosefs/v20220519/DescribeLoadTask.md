**Example 1: 查询目标预热任务**



Input: 

```
tccli goosefs DescribeLoadTask --cli-unfold-argument  \
    --ClusterId g_cvm_7kg3li69 \
    --TaskId 7f22ba8e-ca92-40e4-a277-18461e481808
```

Output: 
```
{
    "Response": {
        "LoadTaskAttrs": {
            "CreateTime": "2025-10-31T11:36:59+08:00",
            "Description": "ceshi",
            "DistributedLoadAttrs": {
                "LoadByList": "",
                "LoadByPath": "/test",
                "LoadType": "LoadByPath",
                "MetadataSync": false,
                "Replica": "SingleReplica",
                "SkipIfExists": false
            },
            "MetadataLoadAttrs": {
                "LoadByList": "",
                "LoadByPath": "",
                "LoadType": "",
                "SkipIfExists": false
            },
            "ModifyTime": "2025-10-31T11:37:49+08:00",
            "Priority": 66,
            "ReportPath": "",
            "Requester": "100000000001",
            "State": "Completed",
            "TaskId": "7f22ba8e-ca92-40e4-a277-18461e481808",
            "TaskMessage": "",
            "TaskType": "DistributedLoad"
        },
        "RequestId": "5dec7f7b-2b0b-4d1f-b94d-8ac23bc0ed80"
    }
}
```

