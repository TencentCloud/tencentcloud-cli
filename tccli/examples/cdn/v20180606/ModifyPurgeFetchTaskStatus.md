**Example 1: 修改定时刷新预热任务执行状态**



Input: 

```
tccli cdn ModifyPurgeFetchTaskStatus --cli-unfold-argument  \
    --ExecutionTime 2020-09-22T00:00:00+00:00 \
    --ExecutionStatusDesc xx \
    --Id xx \
    --ExecutionStatus xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

