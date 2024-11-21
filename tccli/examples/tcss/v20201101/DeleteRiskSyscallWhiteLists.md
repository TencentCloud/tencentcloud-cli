**Example 1: 删除运行时高危系统调用白名单**



Input: 

```
tccli tcss DeleteRiskSyscallWhiteLists --cli-unfold-argument  \
    --WhiteListIdSet 10001
```

Output: 
```
{
    "Response": {
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

