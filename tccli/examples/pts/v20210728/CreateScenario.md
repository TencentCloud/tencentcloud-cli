**Example 1: 创建场景**

创建场景

Input: 

```
tccli pts CreateScenario --cli-unfold-argument  \
    --Load.VpcLoadDistribution.VpcId xx \
    --Load.VpcLoadDistribution.Region xx \
    --Load.VpcLoadDistribution.RegionId 1 \
    --Load.GeoRegionsLoadDistribution.0.Region xx \
    --Load.GeoRegionsLoadDistribution.0.RegionId 1 \
    --Load.GeoRegionsLoadDistribution.0.Percentage 30 \
    --Load.GeoRegionsLoadDistribution.1.Region xx \
    --Load.GeoRegionsLoadDistribution.1.RegionId 5 \
    --Load.GeoRegionsLoadDistribution.1.Percentage 70 \
    --Load.LoadSpec.RequestsPerSecond.DurationSeconds 0 \
    --Load.LoadSpec.RequestsPerSecond.MaxRequestsPerSecond 0 \
    --Load.LoadSpec.Concurrency.MaxRequestsPerSecond 1000 \
    --Load.LoadSpec.Concurrency.Stages.0.DurationSeconds 60 \
    --Load.LoadSpec.Concurrency.Stages.0.TargetVirtualUsers 1000 \
    --Load.LoadSpec.Concurrency.IterationCount 5 \
    --Datasets.0.HeaderInFile True \
    --Datasets.0.Name xx \
    --Datasets.0.LineCount 0 \
    --Datasets.0.Split True \
    --Datasets.0.UpdatedAt 2020-09-22T00:00:00+00:00 \
    --Datasets.0.HeaderColumns xx \
    --Datasets.0.Size 0 \
    --Name xx \
    --ProjectId xx \
    --Extensions a.jar \
    --Scripts b.js \
    --SLAId xx \
    --Configs c.prop \
    --Type xx \
    --CronId xx \
    --Description xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ScenarioId": "scenario-xx"
    }
}
```

