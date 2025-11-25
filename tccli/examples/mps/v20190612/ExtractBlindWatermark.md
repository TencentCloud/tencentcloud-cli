**Example 1: 发起提取视频数字水印任务**

发起提取视频数字水印任务

Input: 

```
tccli mps ExtractBlindWatermark --cli-unfold-argument  \
    --Type blind-basic \
    --InputInfo.Type URL \
    --InputInfo.UrlInputInfo.Url http://test.cos.com/video.mp4 \
    --ExtractBlindWatermarkConfig.SegmentDuration 5000
```

Output: 
```
{
    "Response": {
        "RequestId": "2134541-fdc5-4b08-bf2d-97f7d6678b44",
        "TaskId": "24000105-ExtractBlindWatermark-xxxxxx"
    }
}
```

