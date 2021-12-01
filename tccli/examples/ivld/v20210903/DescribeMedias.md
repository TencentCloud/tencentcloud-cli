**Example 1: 列举前2个成功完成的媒资文件**



Input: 

```
tccli ivld DescribeMedias --cli-unfold-argument  \
    --MediaFilter.StatusSet 8 \
    --PageNumber 1 \
    --PageSize 2
```

Output: 
```
{
    "Response": {
        "MediaInfoSet": [
            {
                "DownLoadURL": "https://ai-media-1256936300.cos.ap-guangzhou.myqcloud.com/ai-media/test-news.mov",
                "FailedReason": "",
                "MediaId": "media-es88zd2m",
                "Metadata": {
                    "BitRate": 258778,
                    "Duration": 43.211,
                    "FPS": 30,
                    "FileSize": 1397761,
                    "Height": 480,
                    "MD5": "6348474d783a56de32b4b2ac42e74d79",
                    "NumFrames": 0,
                    "Width": 848
                },
                "Name": "demo-video-1",
                "Progress": 0,
                "Status": 8
            },
            {
                "DownLoadURL": "https://ai-media-1256936300.cos.ap-guangzhou.myqcloud.com/ai-media/test-news-1.mov",
                "FailedReason": "",
                "MediaId": "media-t9Igr9jf",
                "Metadata": {
                    "BitRate": 258778,
                    "Duration": 43.211,
                    "FPS": 30,
                    "FileSize": 1397761,
                    "Height": 480,
                    "MD5": "6348474d783a56de32b4b2ac42e74d79",
                    "NumFrames": 0,
                    "Width": 848
                },
                "Name": "demo-video-3.mov",
                "Progress": 0,
                "Status": 8
            }
        ],
        "RequestId": "d56d17ca-fa6f-4040-8627-328a08e7a857",
        "TotalCount": 11
    }
}
```

