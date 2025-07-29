**Example 1: 创建媒体质检模板**



Input: 

```
tccli mps CreateQualityControlTemplate --cli-unfold-argument  \
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
        "Definition": 200090,
        "RequestId": "7bb44c6c-92d0-4dad-99cf-88f569c6d3ad"
    }
}
```

