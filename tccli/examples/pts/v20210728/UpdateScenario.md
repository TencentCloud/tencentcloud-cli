**Example 1: 更新场景**



Input: 

```
tccli pts UpdateScenario --cli-unfold-argument  \
    --Load.VpcLoadDistribution.VpcId xx \
    --Load.VpcLoadDistribution.Region xx \
    --Load.VpcLoadDistribution.RegionId 1 \
    --Load.GeoRegionsLoadDistribution.0.Region xx \
    --Load.GeoRegionsLoadDistribution.0.RegionId 0 \
    --Load.GeoRegionsLoadDistribution.0.Percentage 30 \
    --Load.GeoRegionsLoadDistribution.1.Region xx \
    --Load.GeoRegionsLoadDistribution.1.RegionId 0 \
    --Load.GeoRegionsLoadDistribution.1.Percentage 70 \
    --Load.LoadSpec.RequestsPerSecond.DurationSeconds 0 \
    --Load.LoadSpec.RequestsPerSecond.MaxRequestsPerSecond 0 \
    --Load.LoadSpec.Concurrency.MaxRequestsPerSecond 0 \
    --Load.LoadSpec.Concurrency.Stages.0.DurationSeconds 60 \
    --Load.LoadSpec.Concurrency.Stages.0.TargetVirtualUsers 1000 \
    --Load.LoadSpec.Concurrency.IterationCount 0 \
    --Status 0 \
    --Datasets.0.HeaderInFile True \
    --Datasets.0.Name xx \
    --Datasets.0.LineCount 0 \
    --Datasets.0.Split True \
    --Datasets.0.UpdatedAt 2020-09-22T00:00:00+00:00 \
    --Datasets.0.HeaderColumns xx \
    --Datasets.0.Size 0 \
    --Name xx \
    --ScenarioId xx \
    --ProjectId xx \
    --Extensions xx \
    --EncodedScripts WyJhYmMiLCAiZGVmIl0K \
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
        "RequestId": "xx"
    }
}
```

