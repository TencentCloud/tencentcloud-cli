**Example 1: 请求示例**



Input: 

```
tccli live ModifyLivePullStreamTask --cli-unfold-argument  \
    --TaskId 123 \
    --SourceUrls rtmp://your.domainname.com/live/stream1 \
    --StartTime 2020-04-16T11:02:00Z \
    --EndTime 2020-04-17T12:02:00Z \
    --Operator yourname
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

