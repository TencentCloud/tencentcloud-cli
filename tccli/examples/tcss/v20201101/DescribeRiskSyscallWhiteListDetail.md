**Example 1: 运行时高危系统调用白名单详细信息**



Input: 

```
tccli tcss DescribeRiskSyscallWhiteListDetail --cli-unfold-argument  \
    --WhiteListId 1002
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
                "sha256:707540fd8a54ab3ebc086ecc96d2d6143fd92c1cac4d0b23353e1b7078b5937b"
            ],
            "Id": "10001",
            "ProcessPath": "/bin/sh"
        }
    }
}
```

