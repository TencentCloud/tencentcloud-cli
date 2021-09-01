**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveStreamPublishedList --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com \
    --AppName live \
    --StreamName test \
    --PageNum 1 \
    --PageSize 10 \
    --StartTime 2015-06-25T03:30:50Z \
    --EndTime 2015-12-26T03:30:50Z
```

Output: 
```
{
    "Response": {
        "PublishInfo": [
            {
                "AppName": "live",
                "ClientIp": "180.163.8.244",
                "DomainName": "5000.livepush.myqcloud.com",
                "Duration": 10,
                "Resolution": "640*352",
                "StopReason": "客户端主动断流",
                "StreamEndTime": "2019-01-04T11:59:58Z",
                "StreamName": "test1",
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

