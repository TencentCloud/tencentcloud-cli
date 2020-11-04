**Example 1: 创建画质重生任务**

对视频进行转码、去噪、去划痕、去毛刺、超分、细节增强和色彩增强。

Input: 

```
tccli ie CreateMediaQualityRestorationTask --cli-unfold-argument  \
    --DownInfo.Type 0\
    --DownInfo.UrlInfo.Url http://test.video.myqcloud.com/testA.mp4\
    --TransInfo.0.TaskName src_file.mp4\
    --TransInfo.0.TargetInfo.FileName dst_file.mp4\
    --TransInfo.0.VideoInfo.VideoEnhance.ColorEnhance.Type strong\
    --SaveInfo.Type 1\
    --SaveInfo.CosInfo.Region ap-beijing\
    --SaveInfo.CosInfo.Bucket test-123456\
    --SaveInfo.CosInfo.Path /out_file/
```

Output: 
```
{
    "Response": {
        "TaskId": "b8dc83ef-7ce4-4d76-94b5-a8cfe73d40e3",
        "RequestId": "5z1993x8-05y9-14a8-ab55-192ff22297c9"
    }
}
```

