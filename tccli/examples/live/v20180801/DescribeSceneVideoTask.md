**Example 1: 请求示例**



Input: 

```
tccli live DescribeSceneVideoTask --cli-unfold-argument  \
    --TaskId 2*****278-*********Video-721d18cefa094ba4a6*******cbbacab
```

Output: 
```
{
    "Response": {
        "Message": "role not exist",
        "Resolution": "1920x1080",
        "Status": "DONE",
        "VideoUrls": [
            "https://a*****u**ut-video-file-1326893053.cos.ap-guangzhou.myqcloud.com/251006278/251006278-live-AigcVideo-721d18cefa094ba4****6****cbbacab_0.mp4?q-sign-algorithm=sha1&q-ak=AKIDLm***5**********k04*****keLrAG9C&q-sign-time=1778220128;1778**********ey-time=1778220128;1778263338&q-h**de*-list=ho***q-url-param-list=&q-signature=*f0133***fdf5d****f6366c98b95736b7293d8c"
        ],
        "RequestId": "e76ec0ff-6faa-4f16-8e81-d7c160457496"
    }
}
```

