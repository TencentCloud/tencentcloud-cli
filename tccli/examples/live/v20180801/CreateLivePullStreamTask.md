**Example 1: 请求示例**

用于创建直播拉流任务。

Input: 

```
tccli live CreateLivePullStreamTask --cli-unfold-argument  \
    --SourceType PullLivePushLive \
    --DomainName 5000.livepush.myqcloud.com \
    --SourceUrls rtmp://5000.liveplay.myqcloud.com/live/stream1 \
    --StreamName test \
    --AppName live \
    --StartTime 2019-12-16T11:02:00Z \
    --Operator vinson \
    --EndTime 2019-12-17T12:02:00Z
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

