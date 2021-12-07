**Example 1: 运行时高危系统调用白名单详细信息**



Input: 

```
tccli tcss DescribeRiskSyscallWhiteListDetail --cli-unfold-argument  \
    --WhiteListId xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "WhiteListDetailInfo": {
            "SyscallNames": [
                "chroot"
            ],
            "ImageIds": [
                "xx"
            ],
            "Id": "xx",
            "ProcessPath": "xx"
        }
    }
}
```

