**Example 1: 呼叫TRTC设备**

呼叫TRTC设备

Input: 

```
tccli iotvideo CallTRTCDevice --cli-unfold-argument  \
    --ProductId product \
    --DeviceName device
```

Output: 
```
{
    "Response": {
        "TRTCParams": {
            "SDKAppId": 123,
            "UserId": "userid",
            "UserSig": "sig",
            "StrRoomId": "roomid",
            "PrivateMapKey": "key"
        },
        "RequestId": "asdf"
    }
}
```

