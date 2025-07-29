**Example 1: 修改媒体质检模板**



Input: 

```
tccli mps ModifyQualityControlTemplate --cli-unfold-argument  \
    --Definition 200090 \
    --Name example2 \
    --Comment  \
    --QualityControlItemSet.0.Type LowEvaluation \
    --QualityControlItemSet.0.Switch ON \
    --QualityControlItemSet.0.Threshold 80 \
    --QualityControlItemSet.0.Duration 0 \
    --QualityControlItemSet.0.IntervalTime 1000 \
    --QualityControlItemSet.1.Type Mosaic \
    --QualityControlItemSet.1.Switch ON \
    --QualityControlItemSet.1.Threshold 80 \
    --QualityControlItemSet.1.Duration 0 \
    --QualityControlItemSet.1.IntervalTime 1000 \
    --Strategy.StrategyType TimeSpotCheck \
    --Strategy.TimeSpotCheck.CheckDuration 50 \
    --Strategy.TimeSpotCheck.CheckInterval 10 \
    --Strategy.TimeSpotCheck.SkipDuration 10 \
    --Strategy.TimeSpotCheck.CirclesNumber 10
```

Output: 
```
{
    "Response": {
        "RequestId": "7c43b64a-8f21-4c2e-ab6e-a490ee5c439d"
    }
}
```

