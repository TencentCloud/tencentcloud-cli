**Example 1: 修改高危系统调用事件状态**



Input: 

```
tccli tcss ModifyRiskSyscallStatus --cli-unfold-argument  \
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

