**Example 1: 添加高危系统调用白名单**



Input: 

```
tccli tcss AddEditRiskSyscallWhiteList --cli-unfold-argument  \
    --WhiteListInfo.ImageIds sha256:27501aa \
    --WhiteListInfo.SyscallNames chroot \
    --WhiteListInfo.ProcessPath /test/test
```

Output: 
```
{
    "Response": {
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

