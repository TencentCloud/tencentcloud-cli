**Example 1: 任务删除**

任务删除

Input: 

```
tccli wedata DeleteTaskDs --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --DeleteScript True \
    --OperateInform True \
    --TaskId 20230523111838986 \
    --VirtualTaskId 20230523111838986 \
    --VirtualFlag True \
    --DeleteMode True
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "77b63b69-b3c5-48ea-809e-d1bbfc1b3da0"
    }
}
```

