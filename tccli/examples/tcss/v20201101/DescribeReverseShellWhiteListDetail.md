**Example 1: 运行时反弹shell白名单详细信息**



Input: 

```
tccli tcss DescribeReverseShellWhiteListDetail --cli-unfold-argument  \
    --WhiteListId xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "WhiteListDetailInfo": {
            "ImageIds": [
                "xx"
            ],
            "Id": "xx",
            "ProcessName": "xx"
        }
    }
}
```

