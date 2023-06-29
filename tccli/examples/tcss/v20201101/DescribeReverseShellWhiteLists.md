**Example 1: 运行时反弹shell白名单列表**



Input: 

```
tccli tcss DescribeReverseShellWhiteLists --cli-unfold-argument  \
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
                "ImageIds": [
                    "xx"
                ],
                "IsGlobal": true,
                "CreateTime": "2020-09-22 00:00:00",
                "ProcessName": "xx",
                "DstIp": "xx",
                "DstPort": "xx",
                "Id": "xx",
                "ImageCount": 1
            }
        ]
    }
}
```

