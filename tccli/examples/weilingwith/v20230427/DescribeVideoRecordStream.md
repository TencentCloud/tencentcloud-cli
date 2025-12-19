**Example 1: 历史流**

成功响应

Input: 

```
tccli weilingwith DescribeVideoRecordStream --cli-unfold-argument  \
    --WID c0e3f641-6ec6-444e-8ac9-3cfecc755cb0 \
    --Protocol hls \
    --StartTime 1693466137 \
    --EndTime 1693466144 \
    --PlayBackRate 1 \
    --WorkspaceId 1016 \
    --ApplicationToken wA9bELuI4oulQCBK876UDBxe00dNcxQW
```

Output: 
```
{
    "Response": {
        "RequestId": "2beb0875-c859-4fde-a46e-5dbdf1421f14",
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
            "Stream": "c0e3f641-6ec6-444e-8ac9-3cfecc755cb0_2beb0875",
            "WebRTC": ""
        }
    }
}
```

