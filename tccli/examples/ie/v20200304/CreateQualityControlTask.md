**Example 1: 创建媒体质检任务**



Input: 

```
tccli ie CreateQualityControlTask --cli-unfold-argument  \
    --DownInfo.Type 0 \
    --DownInfo.UrlInfo.Url http://test.cos.ap-beijing.myqcloud.com/test.mp4 \
    --QualityControlInfo.Interval 1000 \
    --QualityControlInfo.Jitter True \
    --QualityControlInfo.QRCode True \
    --QualityControlInfo.QualityEvaluation True \
    --QualityControlInfo.Voice True
```

Output: 
```
{
    "Response": {
        "TaskId": "1260168002184429568",
        "RequestId": "b228ebf6-5463-429d-8bfe-5c74fb1dc2c5"
    }
}
```

