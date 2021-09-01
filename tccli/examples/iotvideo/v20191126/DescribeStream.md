**Example 1: 获取音视频流地址**



Input: 

```
tccli iotvideo DescribeStream --cli-unfold-argument  \
    --Tid ****** \
    --AccessId ****** \
    --Protocol ******
```

Output: 
```
{
    "Response": {
        "RequestId": "43348837-xxxx-xxxx-xxxx-77c333c1b96e",
        "Data": {
            "Protocol": "RTSP",
            "URI": "xxxxxxxxxxxxxxx",
            "ExpireTime": 1602589211,
            "VideoCodec": "H265",
            "AudioCodec": "G711"
        }
    }
}
```

