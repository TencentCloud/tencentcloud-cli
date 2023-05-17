**Example 1: 请求示例**

查询并发录制路数，对慢直播和普通直播适用。

Input: 

```
tccli live DescribeConcurrentRecordStreamNum --cli-unfold-argument  \
    --PushDomains 5000.livepush.com \
    --EndTime 2019-03-01 T12:00:00+08:00 \
    --StartTime 2019-03-01T00:00:00+08:00 \
    --LiveType NormalLive \
    --MainlandOrOversea Mainland
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01T01:00:00+08:00",
                "Num": 100
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

