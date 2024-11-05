**Example 1: 删除运行时高危系统调用事件**



Input: 

```
tccli tcss DeleteRiskSyscallEvents --cli-unfold-argument  \
    --EventIdSet 10001
```

Output: 
```
{
    "Response": {
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

