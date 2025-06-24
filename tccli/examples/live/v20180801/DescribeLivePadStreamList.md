**Example 1: 请求示例**



Input: 

```
tccli live DescribeLivePadStreamList --cli-unfold-argument  \
    --DomainName 5000.livepush.com
```

Output: 
```
{
    "Response": {
        "StreamInfoList": [
            {
                "DomainName": "5000.livepush.com",
                "AppName": "live",
                "StreamName": "stream",
                "PublishTime": "2025-04-01T00:00:00Z",
                "PadStreamType": "1"
            }
        ],
        "TotalPage": 1,
        "TotalNum": 1,
        "PageNum": 1,
        "PageSize": 10,
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

