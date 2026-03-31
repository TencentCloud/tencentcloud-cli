**Example 1: 停止任务运行示例**



Input: 

```
tccli wedata StopTaskExecutions --cli-unfold-argument  \
    --WorkspaceId 1 \
    --TaskExecutionIdList t_exec_1001_1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ActionResults": [
                {
                    "ItemId": "t_exec_1001_1",
                    "OpStatus": true
                }
            ]
        },
        "RequestId": "087b2b69-0109-4b83-9464-c159d0f6e095"
    }
}
```

