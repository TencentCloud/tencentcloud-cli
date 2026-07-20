**Example 1: 创建ai漫剧任务**

创建ai漫剧任务

Input: 

```
tccli mps CreateAiDramaTask --cli-unfold-argument  \
    --Input.Script 从前有一只小兔子，上山采蘑菇 \
    --Input.Style chinese_ink_wash \
    --Input.Ratio 16:9 \
    --Input.Resolution 1080p \
    --CosInfo.CosBucketRegion  \
    --CosInfo.CosBucketName  \
    --CosInfo.CosBucketPath 
```

Output: 
```
{
    "Response": {
        "TaskId": "68459f79-bdce-52c8-4b86-5d446adbbee0",
        "RequestId": "867c9447-772f-48f5-a41c-11fe3c665695"
    }
}
```

