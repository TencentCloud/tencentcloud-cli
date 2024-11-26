**Example 1: 修改Index为1的推流信息**



Input: 

```
tccli live ModifyCasterOutputInfo --cli-unfold-argument  \
    --CasterId 1234 \
    --OutputInfo.OutputIndex 1 \
    --OutputInfo.OutputUrl rtmp://another.third.push.domain/live/another_stream_id
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

