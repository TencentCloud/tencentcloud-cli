**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveStreamOnlineList --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com \
    --AppName live \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "OnlineInfo": [
            {
                "StreamName": "5000_abcdefg",
                "AppName": "live",
                "DomainName": "5000.livepush.myqcloud.com",
                "PublishTimeList": [
                    {
                        "PublishTime": "2017-10-24T12:00:00Z"
                    }
                ]
            }
        ],
        "TotalNum": 1,
        "TotalPage": 1,
        "PageNum": 1,
        "PageSize": 10,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

