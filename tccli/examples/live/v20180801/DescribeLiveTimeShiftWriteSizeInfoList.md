**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveTimeShiftWriteSizeInfoList --cli-unfold-argument  \
    --StartTime abc \
    --EndTime abc \
    --DomainNames abc \
    --Dimensions abc \
    --StorageDays 0 \
    --Granularity 0 \
    --MainlandOrOversea abc
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Area": "abc",
                "Time": "abc",
                "WriteSize": 0,
                "Domain": "abc",
                "StorageDays": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

