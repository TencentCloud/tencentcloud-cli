**Example 1: 上报训练自定义指标**



Input: 

```
tccli tione PushTrainingMetrics --cli-unfold-argument  \
    --Data.0.Timestamp 1641002400 \
    --Data.0.TaskId taskid-xyz \
    --Data.0.Epoch 12 \
    --Data.0.Step 1200 \
    --Data.0.TotalSteps 10000 \
    --Data.0.Points.0.Name loss \
    --Data.0.Points.0.Value 189.30 \
    --Data.0.Points.1.Name accuracy \
    --Data.0.Points.1.Value 82.01 \
    --Data.1.Timestamp 1641002460 \
    --Data.1.TaskId taskid-xyz \
    --Data.1.Epoch 13 \
    --Data.1.Step 1300 \
    --Data.1.TotalSteps 10000 \
    --Data.1.Points.0.Name loss \
    --Data.1.Points.0.Value 159.31 \
    --Data.1.Points.1.Name accuracy \
    --Data.1.Points.1.Value 89.39
```

Output: 
```
{
    "Response": {
        "RequestId": "123fa8123"
    }
}
```

