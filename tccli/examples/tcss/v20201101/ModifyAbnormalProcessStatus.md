**Example 1: 修改异常进程事件状态**



Input: 

```
tccli tcss ModifyAbnormalProcessStatus --cli-unfold-argument  \
    --EventIdSet xx \
    --Status xx \
    --Remark xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

