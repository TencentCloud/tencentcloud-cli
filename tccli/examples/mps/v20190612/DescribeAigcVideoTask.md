**Example 1: 请求示例**



Input: 

```
tccli mps DescribeAigcVideoTask --cli-unfold-argument  \
    --TaskId 2147483790
```

Output: 
```
{
    "Response": {
        "Message": "",
        "Resolution": "1920x1088",
        "Status": "DONE",
        "VideoUrls": [
            "https://live-xxx-video-1311402212.cos.ap-guangzhou.myqcloud.com/251006278_xxx_711361074106890375.mp4"
        ],
        "RequestId": "0b9ff3d7-959e-4b9d-8553-7c125305c868"
    }
}
```

