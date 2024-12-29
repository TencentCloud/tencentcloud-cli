**Example 1: 请求示例**

将Index为1的输入源修改为一个导播台推流地址

Input: 

```
tccli live ModifyCasterInputInfo --cli-unfold-argument  \
    --InputInfo.Description modify example \
    --InputInfo.InputIndex 1 \
    --InputInfo.InputType 0 \
    --InputInfo.InputUrl rtmp://caster.push.example.com/live/example \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "InputPlayUrl": "http://play.example.com/live/example_stream_id",
        "InputWebRTCPlayUrl": "webrtc://webrtc.play.example.com/live/example_stream_id"
    }
}
```

