**Example 1: 添加高危系统调用白名单**



Input: 

```
tccli tcss AddEditRiskSyscallWhiteList --cli-unfold-argument  \
    --WhiteListInfo.ImageIds xxxx \
    --WhiteListInfo.SyscallNames chroot \
    --WhiteListInfo.ProcessPath xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

**Example 2: 编辑高危系统调用白名单**



Input: 

```
tccli tcss AddEditRiskSyscallWhiteList --cli-unfold-argument  \
    --WhiteListInfo.ImageIds xxxx \
    --WhiteListInfo.SyscallNames chroot \
    --WhiteListInfo.ProcessPath xxx \
    --WhiteListInfo.Id xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

