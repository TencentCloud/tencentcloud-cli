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
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe",
        "WhiteListSet": [
            {
                "UpdateTime": "2020-09-22 00:00:00",
                "ImageIds": [
                    "sha256:80beff5ff34259ceb7fbe9cd10b2d94912618f5b5595f234349c5bb0cd4f9211"
                ],
                "IsGlobal": true,
                "CreateTime": "2020-09-22 00:00:00",
                "ProcessName": "/bin/apitest",
                "DstIp": "1.1.1.1",
                "DstPort": "1222",
                "Id": "6281f7822403e60601d1dba6",
                "ImageCount": 1
            }
        ]
    }
}
```

