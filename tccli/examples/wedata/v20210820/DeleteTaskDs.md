**Example 1: 任务删除**

任务删除

Input: 

```
tccli wedata DeleteTaskDs --cli-unfold-argument  \
    --ProjectId abc \
    --DeleteScript True \
    --OperateInform True \
    --TaskId abc \
    --VirtualTaskId abc \
    --VirtualFlag True \
    --DeleteMode True
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

