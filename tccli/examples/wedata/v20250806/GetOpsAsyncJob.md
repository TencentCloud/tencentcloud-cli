**Example 1: 查询异步操作状态**



Input: 

```
tccli wedata GetOpsAsyncJob --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --AsyncId c2d687cf-f0a9-4357-bada-942bf43e33b7
```

Output: 
```
{
    "Response": {
        "Data": {
            "AsyncId": "2428908825624145920",
            "AsyncType": "INSTANCE_KILL",
            "CreateTime": "2025-08-28T16:48:19",
            "CreateUserUin": "100032159948",
            "ErrorDesc": null,
            "FinishedSubProcessCount": 4,
            "ProjectId": "2428908825624145920",
            "Status": "SUCCESS",
            "SuccessSubProcessCount": 4,
            "TotalSubProcessCount": 4,
            "UpdateTime": "2025-08-28T16:48:40"
        },
        "RequestId": "e872263f-3100-406e-9728-6823090d93ae"
    }
}
```

