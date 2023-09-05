**Example 1: 获取实时流地址**

成功响应

Input: 

```
tccli weilingwith DescribeVideoLiveStream --cli-unfold-argument  \
    --WID 76d8109e-64cd-4a85-b011-4a0c29a654e8 \
    --Protocol hls \
    --WorkspaceId 1016 \
    --ApplicationToken ct5E8QNPQEZZqNW7ShPAJQVzrTV9xIbL
```

Output: 
```
{
    "Response": {
        "RequestId": "96233e8f-3a98-470b-8bf2-45fbd4988bd8",
        "Result": {
            "FLV": "",
            "HLS": "https://t-video.twins.tencent.com:443/hls1935/xxx",
            "RAW": {
                "IP": "",
                "InnerIP": "",
                "NATIP": "",
                "Port": 0,
                "SM4Vector": "",
                "StreamEnKey": "",
                "StreamToken": ""
            },
            "RTMP": "",
            "Stream": "76d8109e-64cd-4a85-b011-4a0c29a654e8",
            "WebRTC": ""
        }
    }
}
```

