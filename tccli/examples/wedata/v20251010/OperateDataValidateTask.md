**Example 1: OperateDataValidateTask调用示例**



Input: 

```
tccli wedata OperateDataValidateTask --cli-unfold-argument  \
    --WorkspaceId id_1 \
    --TaskId task_id_1 \
    --Operate 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Message": null,
            "OperateResult": true
        },
        "RequestId": "2e71fa49-9abd-4f02-aff1-d6e55f6fe926"
    }
}
```

