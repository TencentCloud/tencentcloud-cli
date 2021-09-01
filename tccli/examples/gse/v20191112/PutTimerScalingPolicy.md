**Example 1: 创建或更新定时器**



Input: 

```
tccli gse PutTimerScalingPolicy --cli-unfold-argument  \
    --TimerScalingPolicy.TimerId  \
    --TimerScalingPolicy.TimerStatus 1 \
    --TimerScalingPolicy.TimerName 11111111 \
    --TimerScalingPolicy.TimerFleetCapacity.FleetId fleet-qp3g3caa-mkurlvoa \
    --TimerScalingPolicy.TimerFleetCapacity.DesiredInstances 1 \
    --TimerScalingPolicy.TimerFleetCapacity.MinSize 0 \
    --TimerScalingPolicy.TimerFleetCapacity.MaxSize 1 \
    --TimerScalingPolicy.TimerFleetCapacity.ScalingInterval 10 \
    --TimerScalingPolicy.TimerFleetCapacity.ScalingType ScalingTypeAuto \
    --TimerScalingPolicy.TimerFleetCapacity.TargetConfiguration.TargetValue 23 \
    --TimerScalingPolicy.TimerConfiguration.TimerType TimerTypeDay \
    --TimerScalingPolicy.TimerConfiguration.TimerValue.Day 1 \
    --TimerScalingPolicy.TimerConfiguration.TimerValue.FromDay 0 \
    --TimerScalingPolicy.TimerConfiguration.TimerValue.ToDay 0 \
    --TimerScalingPolicy.TimerConfiguration.BeginTime 2021-01-14T14:04:29.496Z \
    --TimerScalingPolicy.TimerConfiguration.EndTime 2022-01-14T14:04:29.496Z
```

Output: 
```
{
    "Response": {
        "RequestId": "s1610633051302940772"
    }
}
```

