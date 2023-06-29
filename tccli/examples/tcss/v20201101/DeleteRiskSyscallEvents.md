**Example 1: 删除运行时高危系统调用事件**



Input: 

```
tccli tcss DeleteRiskSyscallEvents --cli-unfold-argument  \
    --EventIdSet xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

