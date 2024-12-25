**Example 1: 新增一个推流到第三方配置**



Input: 

```
tccli live AddCasterOutputInfo --cli-unfold-argument  \
    --CasterId 63501 \
    --OutputInfo.OutputIndex 1 \
    --OutputInfo.OutputUrl rtmp://example.third.push.domain/live/push_stream_id
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

