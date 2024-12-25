**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveTimeShiftWriteSizeInfoList --cli-unfold-argument  \
    --StartTime 2024-12-24T02:28:54Z \
    --EndTime 2024-12-25T02:28:54Z \
    --DomainNames 5000.livepull.com \
    --Dimensions StorageDays \
    --StorageDays 1 \
    --Granularity 0 \
    --MainlandOrOversea Oversea
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Area": "Oversea",
                "Time": "2024-12-25T02:28:54Z",
                "WriteSize": 0,
                "Domain": "5000.livepull.com",
                "StorageDays": 0
            }
        ],
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

