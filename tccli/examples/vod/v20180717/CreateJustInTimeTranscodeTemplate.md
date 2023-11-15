**Example 1: 创建即时转码模板**



Input: 

```
tccli vod CreateJustInTimeTranscodeTemplate --cli-unfold-argument  \
    --Name testtempaltename \
    --VideoConfigure.Width 720 \
    --VideoConfigure.Height 1080 \
    --VideoConfigure.Bitrate 10000 \
    --VideoConfigure.ResolutionAdaptive open \
    --WatermarkConfigure.Switch ON \
    --WatermarkConfigure.ImageContent 111 \
    --WatermarkConfigure.Width 10% \
    --WatermarkConfigure.Height 10% \
    --WatermarkConfigure.XPos 10% \
    --WatermarkConfigure.YPos 10%
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

