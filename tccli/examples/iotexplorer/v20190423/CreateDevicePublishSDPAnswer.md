**Example 1: 测试创建设备推流SDP请求**



Input: 

```
tccli iotexplorer CreateDevicePublishSDPAnswer --cli-unfold-argument  \
    --ProductId NKG9ORH8VF \
    --DeviceName nandy_dev_trtc3 \
    --SDPOffer v=0\r\no=- 1234567890 2 IN IP4 127.0.0.1\r\ns=-\r\nt=0 0\r\na=group:BUNDLE 0\r\na=msid-semantic: WMS\r\nm=audio 9 UDP/TLS/RTP/SAVPF 111\r\nc=IN IP4 0.0.0.0\r\na=rtcp:9 IN IP4 0.0.0.0\r\na=ice-ufrag:abcd\r\na=ice-pwd:efghijklmnop\r\na=fingerprint:sha-256 00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD:EE:FF\r\na=setup:actpass\r\na=mid:0\r\na=sendrecv\r\na=rtcp-mux\r\na=
```

Output: 
```
{
    "Response": {
        "SDPAnswer": "v=0\r\no=- 0 0 IN IP4 127.0.0.1\r\ns=mock\r\nt=0 0\r\n",
        "RequestId": "6f1c2470-d805-4270-9494-597182d6cf72"
    }
}
```

