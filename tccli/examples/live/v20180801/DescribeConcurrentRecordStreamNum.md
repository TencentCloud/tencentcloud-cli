**Example 1: 请求示例**



Input: 

```
tccli live DescribeConcurrentRecordStreamNum --cli-unfold-argument  \
    --LiveType NormalLive \
    --MainlandOrOversea Mainland \
    --PushDomains 5000.livepush.com \
    --StartTime '2019-03-01 00:00:00' \
    --EndTime '2019-03-01 12:00:00'
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01 01:00",
                "Num": 100
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

