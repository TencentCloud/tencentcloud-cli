**Example 1: DescribeTimeShiftStreamList**

查询时移流列表

Input: 

```
tccli live DescribeTimeShiftStreamList --cli-unfold-argument  \
    --StartTime 1668064484 \
    --EndTime 1668074484
```

Output: 
```
{
    "Response": {
        "RequestId": "27b51725-321e-4347-8906-4e1d94b5a373",
        "TotalSize": 100,
        "StreamList": [
            {
                "DomainGroup": "",
                "Domain": "5000.live.push.com",
                "AppName": "live",
                "StreamName": "livetest",
                "StartTime": 1668064484,
                "EndTime": 1668064584,
                "Duration": 604800,
                "TransCodeId": 330587,
                "StreamType": 2
            }
        ]
    }
}
```

