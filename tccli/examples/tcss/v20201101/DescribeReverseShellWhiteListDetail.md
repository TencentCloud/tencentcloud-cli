**Example 1: 运行时反弹shell白名单详细信息**



Input: 

```
tccli tcss DescribeReverseShellWhiteListDetail --cli-unfold-argument  \
    --WhiteListId 3hg7edh873hf
```

Output: 
```
{
    "Response": {
        "RequestId": "6281f7822403e60601d1dba6",
        "WhiteListDetailInfo": {
            "ImageIds": [
                "sha256:80beff5ff34259ceb7fbe9cd10b2d94912618f5b5595f234349c5bb0cd4f9211"
            ],
            "ProcessName": "/bin/apitest",
            "DstIp": "1.1.1.1",
            "Id": "3hg7edh873hf",
            "DstPort": "1222"
        }
    }
}
```

