**Example 1: 创建编辑处理/剪切任务**



Input: 

```
tccli ie CreateMediaProcessTask --cli-unfold-argument  \
    --CallbackInfoSet.0.Url http://qq.com \
    --SaveInfoSet.0.CosInfo.Path /video_cutting/test_res/1012_test_sec_video \
    --SaveInfoSet.0.CosInfo.Region ap-beijing \
    --SaveInfoSet.0.CosInfo.Bucket shortvideo-1251820392 \
    --SaveInfoSet.0.CosInfo.CosAuthMode.HostedId internal_test \
    --SaveInfoSet.0.CosInfo.CosAuthMode.Type 1 \
    --SaveInfoSet.0.Type 1 \
    --MediaProcessInfo.MediaCuttingInfo.TargetInfo.Format jpg \
    --MediaProcessInfo.MediaCuttingInfo.TargetInfo.TargetVideoInfo.Width 800 \
    --MediaProcessInfo.MediaCuttingInfo.TargetInfo.TargetVideoInfo.Height 800 \
    --MediaProcessInfo.MediaCuttingInfo.TargetInfo.FileName dstfile-{index|:5|4:x} \
    --MediaProcessInfo.MediaCuttingInfo.ResultListSaveType UseSaveInfo \
    --MediaProcessInfo.MediaCuttingInfo.TimeInfo.IntervalPoint.Interval 5000 \
    --MediaProcessInfo.MediaCuttingInfo.TimeInfo.IntervalPoint.StartTime 20000 \
    --MediaProcessInfo.MediaCuttingInfo.TimeInfo.Type IntervalPoint \
    --MediaProcessInfo.MediaCuttingInfo.OutForm.FillType Gaussian \
    --MediaProcessInfo.MediaCuttingInfo.OutForm.Type Static \
    --MediaProcessInfo.Type MediaCutting \
    --SourceInfoSet.0.DownInfo.CosInfo.Path /video/sar_dar/sar_dar.mov \
    --SourceInfoSet.0.DownInfo.CosInfo.Region ap-beijing \
    --SourceInfoSet.0.DownInfo.CosInfo.Bucket shortvideo-1251820392 \
    --SourceInfoSet.0.DownInfo.CosInfo.CosAuthMode.HostedId internal_test \
    --SourceInfoSet.0.DownInfo.CosInfo.CosAuthMode.Type 1 \
    --SourceInfoSet.0.DownInfo.Type 1 \
    --SourceInfoSet.0.Type Video \
    --SourceInfoSet.0.Id source_video
```

Output: 
```
{
    "Response": {
        "TaskId": "12001326083614739554304",
        "RequestId": "5z1993x8-05y9-14a8-ab55-192ff22297c9"
    }
}
```

