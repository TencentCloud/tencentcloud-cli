**Example 1: 请求示例**



Input: 

```
tccli live CreatePullStreamConfig --cli-unfold-argument  \
    --AreaId 1 \
    --ToUrl rtmp://5000.livepush.myqcloud.com/live/stream2 \
    --FromUrl rtmp://5000.liveplay.myqcloud.com/live/stream1 \
    --IspId 1 \
    --StartTime 2018-12-31T11:02:00Z \
    --EndTime 2018-12-31T12:02:00Z
```

Output: 
```
{
    "Response": {
        "ConfigId": "123",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

