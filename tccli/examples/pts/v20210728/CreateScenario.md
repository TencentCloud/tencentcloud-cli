**Example 1: 创建场景**

创建场景

Input: 

```
tccli pts CreateScenario --cli-unfold-argument  \
    --Load.GeoRegionsLoadDistribution.0.Region ap-guangzhou \
    --Load.GeoRegionsLoadDistribution.0.RegionId 1 \
    --Load.GeoRegionsLoadDistribution.0.Percentage 30 \
    --Load.GeoRegionsLoadDistribution.1.Region ap-shanghai \
    --Load.GeoRegionsLoadDistribution.1.RegionId 5 \
    --Load.GeoRegionsLoadDistribution.1.Percentage 70 \
    --Load.LoadSpec.Concurrency.Stages.0.DurationSeconds 60 \
    --Load.LoadSpec.Concurrency.Stages.0.TargetVirtualUsers 1000 \
    --Name name \
    --ProjectId project-1a2b3c4d \
    --Type pts-js
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-123-xyz",
        "ScenarioId": "scenario-1a2b3c4d"
    }
}
```

