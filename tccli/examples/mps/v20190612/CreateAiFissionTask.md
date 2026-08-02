**Example 1: 创建视频裂变任务**

创建视频裂变：产品展示任务

Input: 

```
tccli mps CreateAiFissionTask --cli-unfold-argument  \
    --Input.ImageUrls https://aigc-live-1303333058.cos.ap-guangzhou.myqcloud.com/2600016453-AigcImage-f5f12febe6c44a909e614ceb2ba5c027_0.jpg \
    --Input.Text 时尚百搭服饰，版型修身显瘦，面料亲肤舒适透气，做工考究细节精致 \
    --CosInfo.CosBucketRegion  \
    --CosInfo.CosBucketName  \
    --CosInfo.CosBucketPath  \
    --TaskInfo.Duration 15 \
    --TaskInfo.ModelTier flagship \
    --TaskInfo.Ratio 9:16 \
    --TaskInfo.Resolution 1080p \
    --TaskInfo.Market china \
    --TaskInfo.Language chinese \
    --TaskInfo.VideoType display \
    --TaskInfo.SplitCount 1
```

Output: 
```
{
    "Response": {
        "TaskId": "24000048-AigcScenario-5bb4bbc1c0214685213aac29b01c1155",
        "RequestId": "820528c1-4423-4f7e-b387-7e8960878493"
    }
}
```

