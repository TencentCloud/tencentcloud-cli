**Example 1: 调用返回成功**



Input: 

```
tccli fmu QueryBeautifyVideoJob --cli-unfold-argument  \
    --JobId Iyjz4Rj3OCt5Az9a
```

Output: 
```
{
    "Response": {
        "JobStatusCode": 7,
        "JobStatus": "处理完成",
        "BeautifyVideoOutput": {
            "VideoUrl": "http://bda-video-bodyseg-1254418846.cos.ap-guangzhou.myqcloud.com/video_beautify_prod/1.0/251006279/20200820144608_6dddf5c7-1828-42b8-8512-419cf16a2d3c_result.mp4",
            "VideoMD5": "8A1737F730437CBFDFD8154F6845919C",
            "CoverImage": "",
            "Width": 540,
            "Height": 960,
            "Fps": 22.847341537476,
            "DurationInSec": 1.6194444894791
        },
        "RequestId": "a2924747-04ca-4810-827d-8d2bd42d45ea"
    }
}
```

