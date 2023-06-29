**Example 1: 添加高危系统调用白名单**



Input: 

```
tccli tcss AddEditRiskSyscallWhiteList --cli-unfold-argument  \
    --WhiteListInfo.ImageIds sha256:xx \
    --WhiteListInfo.SyscallNames chroot \
    --WhiteListInfo.ProcessPath /test/test
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

