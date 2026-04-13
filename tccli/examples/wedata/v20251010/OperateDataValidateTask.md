**Example 1: example**



Input: 

```
tccli wedata OperateDataValidateTask --cli-unfold-argument  \
    --WorkspaceId 17697667906247629 \
    --TaskId ta-e7d8f2e5 \
    --Operate 1 \
    --OperateVersion tv-0e45ca02 \
    --OperateType STOP
```

Output: 
```
{
    "Response": {
        "Data": {
            "Message": "操作已提交",
            "OperateResult": true
        },
        "RequestId": "8b6e9e3c-b21a-4612-a94b-50720f8f1fab"
    }
}
```

