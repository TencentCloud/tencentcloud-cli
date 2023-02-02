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
        "RequestId": "xxx",
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

