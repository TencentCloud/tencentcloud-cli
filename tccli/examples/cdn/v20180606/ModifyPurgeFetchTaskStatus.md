**Example 1: 修改定时刷新预热任务执行状态**



Input: 

```
tccli cdn ModifyPurgeFetchTaskStatus --cli-unfold-argument  \
    --ExecutionTime 2020-09-22T00:00:00+00:00 \
    --ExecutionStatusDesc 成功 \
    --Id taskId_1 \
    --ExecutionStatus success
```

Output: 
```
{
    "Response": {
        "RequestId": "19d1096d-a4e8-4607-bfca-840a3f515378"
    }
}
```

