**Example 1: 请求示例**

新增一个输入源

Input: 

```
tccli live AddCasterInputInfo --cli-unfold-argument  \
    --InputInfo.Description for_example \
    --InputInfo.InputIndex 1 \
    --InputInfo.InputType 1 \
    --InputInfo.InputUrl http://www.example.com/vod/example.mp4 \
    --CasterId 1234
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "InputPlayUrl": "rtmp://domain/live/input_play",
        "InputWebRTCPlayUrl": "webrtc://webrtc.domain/live/input_play"
    }
}
```

