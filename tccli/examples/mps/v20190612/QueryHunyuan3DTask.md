**Example 1: 任务不存在**



Input: 

```
tccli mps QueryHunyuan3DTask --cli-unfold-argument  \
    --TaskId 4deda860-a9a0-47e3-81f1-00cadf02a44c
```

Output: 
```
{
    "Response": {
        "ErrorCode": "ResourceNotFound.TaskId",
        "ErrorMessage": "task not found or expired",
        "RequestId": "cec25a1e-0875-44f0-87da-2a1ebabee48b"
    }
}
```

