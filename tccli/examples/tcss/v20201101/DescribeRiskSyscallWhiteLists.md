**Example 1: 运行时高危系统调用白名单列表**



Input: 

```
tccli tcss DescribeRiskSyscallWhiteLists --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677",
        "WhiteListSet": [
            {
                "UpdateTime": "2020-09-22 00:00:00",
                "SyscallNames": [
                    "chroot",
                    "kill"
                ],
                "ImageIds": [
                    "image-id"
                ],
                "CreateTime": "2020-09-22 00:00:00",
                "ProcessPath": "/usr/bin/sh",
                "Id": "10001",
                "ImageCount": 1,
                "IsGlobal": true
            }
        ]
    }
}
```

