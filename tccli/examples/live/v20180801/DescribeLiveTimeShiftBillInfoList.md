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
                "Domain": "x.com",
                "Duration": 1,
                "StoragePeriod": 1,
                "Time": "2022-05-06T10:30:00Z"
            },
            {
                "Domain": "x.com",
                "Duration": 1,
                "StoragePeriod": 1,
                "Time": "2022-05-06T10:35:00Z"
            }
        ],
        "RequestId": "ca0bb85f-6b95-4b9f-b85f-fdsafasds"
    }
}
```

