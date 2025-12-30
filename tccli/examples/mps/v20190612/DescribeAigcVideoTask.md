**Example 1: 请求示例**



Input: 

```
tccli mps DescribeAigcVideoTask --cli-unfold-argument  \
    --TaskId 4-AigcVideo-c3b145ec764****55b699e63be17d
```

Output: 
```
{
    "Response": {
        "Message": "ok",
        "Resolution": "1920x1088",
        "Status": "DONE",
        "VideoUrls": [
            "https://live-**-video-*****.cos.ap-guangzhou.myqcloud.com/251006278_***_711361***06890375.mp4"
        ],
        "RequestId": "0b9ff3d7-959e-4b9d-8553-7c125305c868"
    }
}
```

