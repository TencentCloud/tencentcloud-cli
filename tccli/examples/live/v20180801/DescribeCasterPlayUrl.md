**Example 1: 请求示例**

获取某个输入或者预监、主监的播放地址

Input: 

```
tccli live DescribeCasterPlayUrl --cli-unfold-argument  \
    --PlayUrlType 1 \
    --CasterId 63501 \
    --PlayUrlIndex 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "PlayUrl": "http://domain/live/test.flv",
        "WebRTCPlayUrl": "webrtc://webrtc.domain.com/live/test"
    }
}
```

