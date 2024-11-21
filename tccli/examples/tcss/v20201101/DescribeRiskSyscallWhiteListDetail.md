**Example 1: 运行时高危系统调用白名单详细信息**



Input: 

```
tccli tcss DescribeRiskSyscallWhiteListDetail --cli-unfold-argument  \
    --WhiteListId 45645
```

Output: 
```
{
    "Response": {
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677",
        "WhiteListDetailInfo": {
            "SyscallNames": [
                "chroot"
            ],
            "ImageIds": [
                "image-id"
            ],
            "Id": "10001",
            "ProcessPath": "/bin/sh"
        }
    }
}
```

