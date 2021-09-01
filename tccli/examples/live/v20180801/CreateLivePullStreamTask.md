**Example 1: 请求示例**



Input: 

```
tccli live CreateLivePullStreamTask --cli-unfold-argument  \
    --SourceType PullLivePushLive \
    --SourceUrls rtmp://5000.liveplay.myqcloud.com/live/stream1 \
    --DomainName 5000.livepush.myqcloud.com \
    --AppName live \
    --StreamName test \
    --StartTime 2019-12-16T11:02:00Z \
    --EndTime 2019-12-17T12:02:00Z \
    --Operator vinson
```

Output: 
```
{
    "Response": {
        "TaskId": "10000",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

