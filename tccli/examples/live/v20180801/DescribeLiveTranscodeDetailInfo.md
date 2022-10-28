**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveTranscodeDetailInfo --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 20 \
    --DayTime 20190307
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "StreamName": "test",
                "StartTime": "2019-03-01 01:00",
                "EndTime": "2019-03-01 04:00",
                "Duration": 8,
                "ModuleCodec": "liveprocessor_H264",
                "Bitrate": 120,
                "Type": "混流",
                "PushDomain": "5000.livepush.com",
                "Resolution": "480P",
                "MainlandOrOversea": "Mainland"
            }
        ],
        "PageNum": 1,
        "PageSize": 20,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

