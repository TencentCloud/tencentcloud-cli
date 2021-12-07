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
        "RequestId": "xx",
        "WhiteListSet": [
            {
                "UpdateTime": "2020-09-22 00:00:00",
                "SyscallNames": [
                    "chroot",
                    "kill"
                ],
                "ImageIds": [
                    "xx"
                ],
                "CreateTime": "2020-09-22 00:00:00",
                "ProcessPath": "xx",
                "Id": "xx",
                "ImageCount": 1,
                "IsGlobal": true
            }
        ]
    }
}
```

