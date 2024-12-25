**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveTimeShiftBillInfoList --cli-unfold-argument  \
    --PushDomains start-push.elliotxing.com \
    --StartTime 2022-05-06T00:30:00Z \
    --EndTime 2022-05-06T12:30:00Z
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Domain": "start-push.elliotxing.com",
                "Duration": 0,
                "StoragePeriod": 0,
                "Time": "2023-08-10 20:00:00",
                "TotalDuration": 0
            }
        ],
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

