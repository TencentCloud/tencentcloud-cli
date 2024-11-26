**Example 1: 请求示例**



Input: 

```
tccli live CreateCasterInputPushUrl --cli-unfold-argument  \
    --InputIndex 1 \
    --CasterId 1234
```

Output: 
```
{
    "Response": {
        "PushUrl": "rtmp://www.example.com/live/caster_example_stream_id?example_param=example",
        "RequestId": "c8b02a52-1062-4d6d-9837-54d48b17e8f9"
    }
}
```

