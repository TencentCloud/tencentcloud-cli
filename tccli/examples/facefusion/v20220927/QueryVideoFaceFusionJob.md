**Example 1: 查询视频人脸融合任务**

查询视频人脸融合任务

Input: 

```
tccli facefusion QueryVideoFaceFusionJob --cli-unfold-argument  \
    --JobId C0a5EXaNR7JzGvlg
```

Output: 
```
{
    "Response": {
        "JobStatusCode": 7,
        "JobStatus": "处理完成",
        "VideoFaceFusionOutput": {
            "VideoUrl": "http://bda-video-bodyseg-1254418846.cos.ap-guangzhou.myqcloud.com/video_fusion_test/1.0/251006455/20210119164402_83ecff39-2e4a-41d5-8562-1f8898326565_qc_300314_789050_75_1611045834157_result.mp4",
            "VideoMD5": "3AA00F9A2914DF3F2268628C45C4E4CE",
            "Width": 720,
            "Height": 1280,
            "FPS": 25,
            "DurationInSec": 15.079999923706,
            "Frame": 375
        },
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "RequestId": "ef13456e-8174-4418-8e51-a724257c9a3a"
    }
}
```

