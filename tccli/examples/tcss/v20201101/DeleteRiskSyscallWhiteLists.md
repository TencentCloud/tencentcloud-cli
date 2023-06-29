**Example 1: 删除运行时高危系统调用白名单**



Input: 

```
tccli tcss DeleteRiskSyscallWhiteLists --cli-unfold-argument  \
    --WhiteListIdSet xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

