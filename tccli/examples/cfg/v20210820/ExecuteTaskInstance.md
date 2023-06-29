**Example 1: 示例**



Input: 

```
tccli cfg ExecuteTaskInstance --cli-unfold-argument  \
    --TaskId 222 \
    --TaskActionId 1111 \
    --TaskInstanceIds 111 222 33 \
    --IsOperateAll True \
    --ActionType 1 \
    --TaskGroupId 12
```

Output: 
```
{
    "Response": {
        "RequestId": "6549ed1a-911f-46dd-b6cd-2c02d5bd180f"
    }
}
```

