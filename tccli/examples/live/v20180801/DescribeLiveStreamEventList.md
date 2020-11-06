**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveStreamEventList --cli-unfold-argument  \
    --DomainName yourdomain.test.com \
    --AppName live \
    --StreamName stream \
    --StartTime 2019-01-04T12:00:00Z \
    --EndTime 2019-01-04T20:00:00Z \
    --PageNum 1 \
    --PageSize 10 \
    --IsFilter 1 \
    --IsStrict 0 \
    --IsAsc 0
```

Output: 
```
{
    "Response": {
        "EventList": [
            {
                "AppName": "live",
                "ClientIp": "180.163.8.244",
                "DomainName": "yourdomain.test.com",
                "Duration": 0,
                "Resolution": "640*352",
                "StopReason": "客户端主动断流",
                "StreamEndTime": "2019-01-04T11:59:58Z",
                "StreamName": "stream",
                "StreamStartTime": "2019-01-04T11:59:58Z"
            }
        ],
        "PageNum": 1,
        "PageSize": 10,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

