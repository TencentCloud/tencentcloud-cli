**Example 1: 调用示例**



Input: 

```
tccli ai3d SubmitHunyuanTo3DMotionJob --cli-unfold-argument  \
    --Prompt A person walks forward \
    --Model HY-Motion-1.0 \
    --Duration 5 \
    --EnableMesh True \
    --EnableRewrite True \
    --EnableDurationEst True
```

Output: 
```
{
    "Response": {
        "JobId": "1440974607266955264",
        "RequestId": "52038f80-fc7e-4dcd-be4a-eb48a31e8508"
    }
}
```

