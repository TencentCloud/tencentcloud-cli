**Example 1: 调用返回成功**



Input: 

```
tccli ft MorphFace --cli-unfold-argument  \
    --Urls https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/input1.jpeg https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/input2.jpeg \
    --GradientInfos.0.Tempo 2 \
    --GradientInfos.0.MorphTime 1 \
    --Fps 10 \
    --OutputType 0
```

Output: 
```
{
    "Response": {
        "JobId": "HQ3tBY79dsKl65ob",
        "EstimatedProcessTime": 30,
        "RequestId": "327cd4c8-e544-43db-ba0c-3afda873ac73"
    }
}
```

